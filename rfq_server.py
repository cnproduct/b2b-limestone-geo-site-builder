#!/usr/bin/env python3
"""
Fujian Tianya Cultural Stone Co., Ltd.
Tianya Limestone (tianyalimestone.com) B2B RFQ & Inquiry Server
Port: 8011
Target Email: info@tianyastone.com
"""

import http.server
import socketserver
import json
import os
import csv
import urllib.parse
import urllib.request
import threading
from datetime import datetime
import secrets

PORT = 8011
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
JSON_FILE = os.path.join(DATA_DIR, 'inquiries.json')
CSV_FILE = os.path.join(DATA_DIR, 'inquiries.csv')
ADMIN_KEY = 'tianya2026admin'
FORWARD_EMAIL = 'info@tianyastone.com'

os.makedirs(DATA_DIR, exist_ok=True)

class InquiryHandler(http.server.BaseHTTPRequestHandler):
    def _set_cors_headers(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_cors_headers(204)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)

        # Health check
        if parsed.path in ('/api/health', '/api/status'):
            self._set_cors_headers(200)
            self.wfile.write(json.dumps({
                "status": "healthy",
                "service": "Tianya Limestone Inquiry Server",
                "forward_email": FORWARD_EMAIL,
                "timestamp": datetime.now().isoformat()
            }).encode('utf-8'))
            return

        # Admin View Leads / Inquiries
        if parsed.path == '/api/inquiries':
            key = query.get('key', [''])[0]
            if key != ADMIN_KEY:
                self._set_cors_headers(401)
                self.wfile.write(json.dumps({"error": "Unauthorized. Provide valid ?key="}).encode('utf-8'))
                return

            inquiries = []
            if os.path.exists(JSON_FILE):
                try:
                    with open(JSON_FILE, 'r', encoding='utf-8') as f:
                        inquiries = json.load(f)
                except Exception:
                    inquiries = []

            # Format=html for browser convenience
            if query.get('format', [''])[0] == 'html':
                self._set_cors_headers(200, "text/html; charset=utf-8")
                rows = ""
                for inq in reversed(inquiries):
                    rows += f"""<tr>
                        <td style='border:1px solid #ddd;padding:8px;'>{inq.get('inquiry_id','')}</td>
                        <td style='border:1px solid #ddd;padding:8px;'>{inq.get('created_at','')}</td>
                        <td style='border:1px solid #ddd;padding:8px;'><strong>{inq.get('name','')}</strong><br><small>{inq.get('company','')}</small></td>
                        <td style='border:1px solid #ddd;padding:8px;'><a href='mailto:{inq.get('email','')}'>{inq.get('email','')}</a><br><small>{inq.get('phone','')}</small></td>
                        <td style='border:1px solid #ddd;padding:8px;'>{inq.get('product','')}</td>
                        <td style='border:1px solid #ddd;padding:8px;'>{inq.get('project_area','')}</td>
                        <td style='border:1px solid #ddd;padding:8px;'>{inq.get('sample_box','')}</td>
                        <td style='border:1px solid #ddd;padding:8px;'>{inq.get('message','')}</td>
                        <td style='border:1px solid #ddd;padding:8px;'><span style='color:green;'>{inq.get('routed_to','')}</span></td>
                    </tr>"""
                html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'><title>Tianya Limestone Leads</title>
                <style>body{{font-family:sans-serif;margin:30px;background:#f9fafb;}} table{{width:100%;border-collapse:collapse;background:#fff;}} th{{background:#111;color:#fff;padding:10px;text-align:left;}}</style>
                </head><body>
                <h2>Tianya Limestone B2B Inquiries Desk ({len(inquiries)} Leads)</h2>
                <p>Forwarding destination: <strong>{FORWARD_EMAIL}</strong></p>
                <table><thead><tr><th>ID</th><th>Date</th><th>Buyer / Company</th><th>Contact</th><th>Stone / Product</th><th>Area</th><th>Sample Box</th><th>Message</th><th>Routed To</th></tr></thead>
                <tbody>{rows}</tbody></table></body></html>"""
                self.wfile.write(html.encode('utf-8'))
                return

            self._set_cors_headers(200)
            self.wfile.write(json.dumps({
                "count": len(inquiries),
                "routed_to": FORWARD_EMAIL,
                "inquiries": inquiries
            }, indent=2).encode('utf-8'))
            return

        self._set_cors_headers(404)
        self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        data = {}
        content_type = self.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            try:
                data = json.loads(body.decode('utf-8'))
            except Exception:
                data = {}
        else:
            try:
                parsed_qs = urllib.parse.parse_qs(body.decode('utf-8', errors='ignore'))
                for k, v in parsed_qs.items():
                    data[k] = v[0] if len(v) == 1 else v
            except Exception:
                data = {}

        valid_paths = ('/api/inquiry', '/api/submit-rfq', '/api/rfq')
        if parsed.path not in valid_paths:
            self._set_cors_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))
            return

        # Extract fields
        email = data.get('email') or data.get('work_email') or data.get('buyer_email') or ''
        first_name = data.get('firstName') or data.get('first_name') or ''
        last_name = data.get('lastName') or data.get('last_name') or ''
        name = data.get('name') or (f"{first_name} {last_name}".strip()) or 'B2B Client'
        phone = data.get('phone') or data.get('whatsapp') or data.get('tel') or ''
        company = data.get('company') or data.get('firm') or ''
        project_area = data.get('projectArea') or data.get('area') or ''
        message = data.get('message') or data.get('content') or data.get('notes') or ''
        product = data.get('stoneOfInterest') or data.get('product') or 'Tianya Limestone Architectural Stone'
        sample_box = data.get('sampleBox') or data.get('sample_box') or 'Yes'
        source_page = data.get('source_page') or data.get('url') or self.headers.get('Referer', '')

        if not email:
            self._set_cors_headers(400)
            self.wfile.write(json.dumps({"success": False, "error": "Email address is required."}).encode('utf-8'))
            return

        client_ip = self.headers.get('X-Real-IP') or self.headers.get('X-Forwarded-For') or self.client_address[0]
        if ',' in client_ip:
            client_ip = client_ip.split(',')[0].strip()

        inquiry_id = f"TYL-{datetime.now().strftime('%Y%m%d')}-{secrets.token_hex(2).upper()}"
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')

        record = {
            "inquiry_id": inquiry_id,
            "created_at": created_at,
            "email": email.strip(),
            "name": name.strip(),
            "company": company.strip(),
            "phone": phone.strip(),
            "product": product.strip(),
            "project_area": project_area.strip(),
            "sample_box": str(sample_box),
            "message": message.strip(),
            "source_page": source_page,
            "ip": client_ip,
            "routed_to": FORWARD_EMAIL
        }

        # 1. Save to data/inquiries.json
        inquiries = []
        if os.path.exists(JSON_FILE):
            try:
                with open(JSON_FILE, 'r', encoding='utf-8') as f:
                    inquiries = json.load(f)
            except Exception:
                inquiries = []
        inquiries.append(record)
        try:
            with open(JSON_FILE, 'w', encoding='utf-8') as f:
                json.dump(inquiries, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving inquiries.json: {e}")

        # 2. Save to data/inquiries.csv
        try:
            file_exists = os.path.exists(CSV_FILE)
            with open(CSV_FILE, 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Inquiry ID", "Created At", "Buyer Email", "Contact Name", "Company", "Phone/WhatsApp", "Stone Product", "Area m2", "Sample Box", "Message", "Source Page", "Client IP", "Routed To"])
                writer.writerow([
                    record["inquiry_id"],
                    record["created_at"],
                    record["email"],
                    record["name"],
                    record["company"],
                    record["phone"],
                    record["product"],
                    record["project_area"],
                    record["sample_box"],
                    record["message"],
                    record["source_page"],
                    record["ip"],
                    record["routed_to"]
                ])
        except Exception as e:
            print(f"Error writing inquiries.csv: {e}")

        print(f"✅ [TIANYA LIMESTONE] Logged inquiry {inquiry_id} from {email} for '{product}' -> Forwarding to {FORWARD_EMAIL}")

        # 3. Asynchronously dispatch notification email to info@tianyastone.com
        def dispatch_email(rec):
            try:
                url = f"https://formsubmit.co/ajax/{FORWARD_EMAIL}"
                email_payload = json.dumps({
                    "Inquiry ID": rec["inquiry_id"],
                    "Timestamp (UTC)": rec["created_at"],
                    "Target Stone / Product": rec["product"],
                    "Buyer Email": rec["email"],
                    "Contact Name": rec["name"],
                    "Company / Architecture Firm": rec["company"] or "Not specified",
                    "Phone / WhatsApp": rec["phone"] or "Not specified",
                    "Project Estimated Area": rec["project_area"] or "Not specified",
                    "Sample Kit Requested": rec["sample_box"],
                    "Inquiry Message & Port": rec["message"] or "Factory inquiry from tianyalimestone.com",
                    "Source Page URL": rec["source_page"],
                    "Buyer IP": rec["ip"],
                    "_subject": f"[Tianya Limestone RFQ] {rec['product']} - {rec['name']} ({rec['company'] or rec['email']})",
                    "_template": "table"
                }).encode('utf-8')

                req = urllib.request.Request(
                    url,
                    data=email_payload,
                    headers={
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Origin': 'https://www.tianyalimestone.com',
                        'Referer': rec["source_page"] or 'https://www.tianyalimestone.com/contact-us/',
                        'User-Agent': 'TianyaLimestone-RFQ-Dispatcher/1.0'
                    }
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    resp_data = resp.read().decode('utf-8', errors='ignore')
                    print(f"📧 [TIANYA LIMESTONE] Email dispatched to {FORWARD_EMAIL} (HTTP {resp.status}): {resp_data}")
            except Exception as e:
                print(f"⚠️ [TIANYA LIMESTONE] Email forwarding error: {e}")

        t = threading.Thread(target=dispatch_email, args=(record,))
        t.daemon = True
        t.start()

        self._set_cors_headers(200)
        self.wfile.write(json.dumps({
            "code": 1,
            "success": True,
            "inquiry_id": inquiry_id,
            "message": f"Inquiry received successfully and dispatched to {FORWARD_EMAIL}.",
            "routed_to": FORWARD_EMAIL
        }).encode('utf-8'))

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    server_address = ('127.0.0.1', PORT)
    httpd = socketserver.TCPServer(server_address, InquiryHandler)
    print(f"🚀 Tianya Limestone RFQ Service listening on http://127.0.0.1:{PORT}")
    print(f"   Forwarding all inquiries to: {FORWARD_EMAIL}")
    print(f"   Admin Console: http://127.0.0.1:{PORT}/api/inquiries?key={ADMIN_KEY}&format=html")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
