/**
 * Tianya Limestone RFQ Worker (service worker format)
 * Secrets: TURNSTILE_SECRET_KEY, NOTIFICATION_EMAIL
 */

async function verifyTurnstile(token, secretKey, remoteIp) {
  const formData = new FormData();
  formData.append('secret', secretKey);
  formData.append('response', token);
  if (remoteIp) formData.append('remoteip', remoteIp);
  const res = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST', body: formData,
  });
  const data = await res.json();
  return data.success === true;
}

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': 'https://www.tianyalimestone.com',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Accept',
  };
}

function jsonResponse(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: Object.assign({ 'Content-Type': 'application/json' }, corsHeaders()),
  });
}

async function sendNotificationEmail(inquiry, toEmail) {
  const subject = '[Tianya RFQ] ' + (inquiry.stoneOfInterest || 'General') + ' - ' + inquiry.name;
  const textBody = [
    'New RFQ Inquiry - Tianya Limestone', '================================',
    'Name: ' + inquiry.name, 'Email: ' + inquiry.email,
    'Phone/WhatsApp: ' + inquiry.phone, 'Company: ' + inquiry.company,
    'Project Area: ' + inquiry.projectArea, 'Stone: ' + inquiry.stoneOfInterest,
    'Sample Box: ' + inquiry.sampleBox, 'Source: ' + inquiry.source_page, '',
    'Message:', inquiry.message, '', 'Received: ' + inquiry.timestamp,
  ].join('\n');
  const res = await fetch('https://api.mailchannels.net/tx/v1/send', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      personalizations: [{ to: [{ email: toEmail }] }],
      from: { email: 'rfq@tianyalimestone.com', name: 'Tianya Limestone RFQ' },
      subject: subject,
      content: [{ type: 'text/plain', value: textBody }],
    }),
  });
  if (!res.ok) {
    console.error('Email failed: ' + await res.text());
    return false;
  }
  return true;
}

async function handleRequest(request) {
  const url = new URL(request.url);
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders() });
  }
  if (url.pathname === '/api/health' && request.method === 'GET') {
    return jsonResponse({ ok: true, service: 'tianya-rfq-worker', time: new Date().toISOString() });
  }
  if (url.pathname === '/api/inquiry' && request.method === 'POST') {
    try {
      const payload = await request.json();
      if (payload._honeypot) return jsonResponse({ success: true });
      const token = payload['cf-turnstile-response'] || payload.turnstileToken || '';
      if (!token) return jsonResponse({ success: false, error: 'captcha_required' }, 400);
      const clientIp = request.headers.get('CF-Connecting-IP') || '';
      const valid = await verifyTurnstile(token, TURNSTILE_SECRET_KEY, clientIp);
      if (!valid) return jsonResponse({ success: false, error: 'captcha_failed' }, 403);
      const inquiry = {
        id: (typeof crypto !== 'undefined' && crypto.randomUUID) ? crypto.randomUUID() : String(Date.now()),
        timestamp: new Date().toISOString(),
        name: payload.name || '', email: payload.email || '', phone: payload.phone || '',
        company: payload.company || '', projectArea: payload.projectArea || '',
        message: payload.message || '',
        stoneOfInterest: payload.stoneOfInterest || payload.product || '',
        sampleBox: payload.sampleBox || '', source_page: payload.source_page || '',
        client_ip: clientIp,
      };
      const notifyEmail = (typeof NOTIFICATION_EMAIL !== 'undefined') ? NOTIFICATION_EMAIL : 'info@tianyastone.com';
      const emailed = await sendNotificationEmail(inquiry, notifyEmail);
      if (!emailed) return jsonResponse({ success: false, error: 'email_failed' }, 502);
      return jsonResponse({ success: true, code: 1, id: inquiry.id });
    } catch (err) {
      return jsonResponse({ success: false, error: 'server_error' }, 500);
    }
  }
  return jsonResponse({ error: 'not_found' }, 404);
}

addEventListener('fetch', function(event) {
  event.respondWith(handleRequest(event.request));
});
