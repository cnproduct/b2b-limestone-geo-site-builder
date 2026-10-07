/**
 * Tianya Limestone Architectural Portal - Client Engine
 * 1:1 Design Replication of Eco Outdoor Limestone Experience
 * Branded for Fujian Tianya Cultural Stone Co., Ltd.
 */

// Global state & product dataset for instant search
let productsRegistry = [];

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileMenu();
  initSearch();
  initHeroSlider();
  initGalleryModal();
  initSizingToggle();
  initSampleForms();
  initSmoothScroll();
});

// Sticky Header
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

// Mobile Menu Drawer
function initMobileMenu() {
  const openBtn = document.getElementById('mobileMenuBtn');
  const closeBtn = document.getElementById('mobileMenuClose');
  const drawer = document.getElementById('mobileNavDrawer');
  const backdrop = document.getElementById('mobileNavBackdrop');

  if (!drawer || !backdrop) return;

  function openDrawer() {
    drawer.classList.add('open');
    backdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    backdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (openBtn) openBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);
}

// Live Search Engine
function initSearch() {
  const triggerBtn = document.getElementById('searchTriggerBtn');
  const modal = document.getElementById('searchModal');
  const closeBtn = document.getElementById('searchCloseBtn');
  const input = document.getElementById('searchInput');
  const resultsContainer = document.getElementById('searchResults');

  if (!modal || !input) return;

  function openSearch() {
    modal.classList.add('active');
    input.value = '';
    input.focus();
    renderSearchResults('');
    document.body.style.overflow = 'hidden';
  }

  function closeSearch() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (triggerBtn) triggerBtn.addEventListener('click', openSearch);
  if (closeBtn) closeBtn.addEventListener('click', closeSearch);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeSearch();
  });

  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSearch();
    }
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeSearch();
    }
  });

  input.addEventListener('input', (e) => {
    renderSearchResults(e.target.value.trim().toLowerCase());
  });

  function renderSearchResults(query) {
    if (!resultsContainer) return;
    if (!window.TIANYA_PRODUCTS || !window.TIANYA_PRODUCTS.length) {
      resultsContainer.innerHTML = '<div class="p-4 text-center text-primary-40">Loading collections...</div>';
      return;
    }

    const matches = window.TIANYA_PRODUCTS.filter(p => {
      if (!query) return true;
      return p.name.toLowerCase().includes(query) ||
             p.finish.toLowerCase().includes(query) ||
             (p.desc && p.desc.toLowerCase().includes(query));
    }).slice(0, 8);

    if (matches.length === 0) {
      resultsContainer.innerHTML = `<div class="p-8 text-center text-primary-40">No limestone collections found matching "${query}".</div>`;
      return;
    }

    resultsContainer.innerHTML = `
      <div class="p-2 border-b border-primary-10 text-xs text-primary-40 uppercase tracking-wider px-4">
        ${query ? `Matching Collections (${matches.length})` : 'Popular Limestone Collections'}
      </div>
      <div class="divide-y divide-primary-10 max-h-[60vh] overflow-y-auto">
        ${matches.map(m => `
          <a href="${m.url}" class="flex items-center gap-4 p-3 hover:bg-chartreuse-100 transition-colors group">
            <div class="w-14 h-14 bg-primary-10 flex-shrink-0 overflow-hidden">
              <img src="${m.image}" alt="${m.name}" class="w-full h-full object-cover">
            </div>
            <div class="flex-grow min-w-0">
              <div class="font-heading font-medium text-base text-primary-100 group-hover:underline flex items-center gap-2">
                <span>${m.name}</span>
                <span class="text-xs font-copy uppercase tracking-wider text-primary-70 bg-primary-10 px-2 py-0.5 rounded">${m.finish}</span>
              </div>
              <p class="text-xs text-primary-70 truncate font-copy">${m.desc || 'Natural architectural limestone pavers & tiles'}</p>
            </div>
            <div class="text-primary-70 pr-2">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 12L10 8L6 4" stroke="currentColor" stroke-width="1.5"/></svg>
            </div>
          </a>
        `).join('')}
      </div>
    `;
  }
}

// Gallery Lightbox & Thumbnail Swapper
function initGalleryModal() {
  const modal = document.getElementById('galleryModal');
  const modalImg = document.getElementById('galleryModalImg');
  const closeBtn = document.getElementById('galleryModalClose');
  const mainSpotlight = document.getElementById('mainSpotlightImg');
  const heroContainer = mainSpotlight ? mainSpotlight.closest('[data-gallery-img]') : null;
  const thumbButtons = document.querySelectorAll('button[data-gallery-img]');

  if (!modal || !modalImg) return;

  function openModal(src, alt) {
    modalImg.src = src;
    modalImg.alt = alt || 'Limestone architectural photo';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Thumbnails swap the main spotlight image and highlight active thumb
  thumbButtons.forEach((btn, idx) => {
    if (idx === 0) {
      btn.classList.add('ring-2', 'ring-black', 'border-black');
    }
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const src = btn.getAttribute('data-gallery-img');
      const alt = btn.getAttribute('data-gallery-alt');
      
      if (mainSpotlight) {
        mainSpotlight.src = src;
        mainSpotlight.alt = alt || 'Limestone architectural stone';
      }
      if (heroContainer) {
        heroContainer.setAttribute('data-gallery-img', src);
        heroContainer.setAttribute('data-gallery-alt', alt);
      }
      
      thumbButtons.forEach(b => b.classList.remove('ring-2', 'ring-black', 'border-black'));
      btn.classList.add('ring-2', 'ring-black', 'border-black');
    });
  });

  // Clicking the main hero container opens the full-screen lightbox
  if (heroContainer) {
    heroContainer.addEventListener('click', (e) => {
      e.preventDefault();
      const src = heroContainer.getAttribute('data-gallery-img') || (mainSpotlight ? mainSpotlight.src : '');
      const alt = heroContainer.getAttribute('data-gallery-alt') || (mainSpotlight ? mainSpotlight.alt : '');
      openModal(src, alt);
    });
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target === closeBtn) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
}

// Sizing Specification "View More" Toggle
function initSizingToggle() {
  const toggleBtn = document.getElementById('toggleSizingBtn');
  const hiddenRows = document.querySelectorAll('.sizing-row-hidden');

  if (!toggleBtn || hiddenRows.length === 0) return;

  let isExpanded = false;
  toggleBtn.addEventListener('click', (e) => {
    e.preventDefault();
    isExpanded = !isExpanded;
    hiddenRows.forEach(row => {
      row.style.display = isExpanded ? 'table-row' : 'none';
    });
    toggleBtn.textContent = isExpanded ? 'View Less Sizes' : 'View More Sizes';
  });
}

// RFQ & Sample Kit Form Submission Handlers
function initSampleForms() {
  const forms = document.querySelectorAll('form[data-tianya-form]');

  forms.forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const statusDiv = form.querySelector('[data-form-status]');
      const originalText = submitBtn ? submitBtn.textContent : 'Submit';

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Transmitting to Factory Export Desk...';
      }
      if (statusDiv) {
        statusDiv.innerHTML = '<span class="text-primary-60 text-xs">Sending enquiry to info@tianyastone.com...</span>';
      }

      const formData = new FormData(form);
      const firstName = formData.get('firstName') || '';
      const lastName = formData.get('lastName') || '';
      const fullName = (firstName + ' ' + lastName).trim() || formData.get('name') || 'B2B Client';
      const email = formData.get('email') || '';
      const phone = formData.get('phone') || '';
      const company = formData.get('company') || '';
      const projectArea = formData.get('projectArea') || '';
      const message = formData.get('message') || '';
      const stoneOfInterest = formData.get('stoneOfInterest') || 'Tianya Limestone Architectural Stone';
      const sampleBox = formData.get('sampleBox') ? 'Yes (Requested)' : 'No';

      const payload = {
        firstName: firstName,
        lastName: lastName,
        name: fullName,
        email: email,
        phone: phone,
        company: company,
        projectArea: projectArea,
        message: message,
        stoneOfInterest: stoneOfInterest,
        product: stoneOfInterest,
        sampleBox: sampleBox,
        source_page: window.location.href,
        target_email: 'info@tianyastone.com',
        'cf-turnstile-response': formData.get('cf-turnstile-response') || ''
      };

      let sentSuccess = false;
      let captchaError = false;

      // 1. Try Cloudflare Worker backend /api/inquiry (Turnstile-protected)
      try {
        const response = await fetch('/api/inquiry', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        let resJson = {};
        try { resJson = await response.json(); } catch (e) { /* non-JSON */ }
        if (response.ok && (resJson.success || resJson.code === 1)) {
          sentSuccess = true;
          if (window.turnstile) { try { turnstile.reset(); } catch (e) {} }
        } else if (resJson.error === 'captcha_required' || resJson.error === 'captcha_failed') {
          captchaError = true;
        }
      } catch (err) {
        console.warn('Backend API note:', err);
      }

      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }

      if (sentSuccess) {
        showToast(`Thank you, ${fullName}! Your inquiry for ${stoneOfInterest} has been successfully sent to info@tianyastone.com. Our export team will provide pricing & sample confirmation within 2-4 hours.`);
        if (statusDiv) {
          statusDiv.innerHTML = '<span class="text-green-700 font-medium text-xs">✓ Inquiry dispatched to <strong>info@tianyastone.com</strong>. You will receive an export quotation shortly.</span>';
        }
        form.reset();
      } else if (captchaError) {
        showToast('Security verification incomplete. Please complete the captcha and resubmit.');
        if (statusDiv) {
          statusDiv.innerHTML = '<span class="text-red-700 font-medium text-xs">Please complete the security verification (captcha) and try again — your message is kept.</span>';
        }
      } else {
        showToast('Sorry, sending failed. Please try again or reach us via WhatsApp.');
        if (statusDiv) {
          statusDiv.innerHTML = '<span class="text-red-700 font-medium text-xs">Sorry, the enquiry could not be sent. Please try again or contact us via WhatsApp.</span>';
        }
      }
    });
  });
}

// Toast Notification
function showToast(message) {
  let toast = document.getElementById('tianyaToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'tianyaToast';
    toast.className = 'tianya-toast';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" class="text-chartreuse-100 flex-shrink-0">
      <circle cx="10" cy="10" r="9" stroke="#E9F551" stroke-width="2"/>
      <path d="M6 10L9 13L14 7" stroke="#E9F551" stroke-width="2" stroke-linecap="round"/>
    </svg>
    <span class="font-copy text-sm leading-tight text-white">${message}</span>
  `;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 6000);
}

// Smooth Anchor Scrolling
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || !targetId.startsWith('#')) return;
      const targetElem = document.querySelector(targetId);
      if (targetElem) {
        e.preventDefault();
        targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

// Interactive 3-Banner Hero Slider (Fusing 127.0.0.1:8796 with Eco Outdoor)
function initHeroSlider() {
  const slider = document.getElementById('heroSlider');
  if (!slider) return;

  const slides = slider.querySelectorAll('.hero-slide');
  const tabs = slider.querySelectorAll('.hero-slider-tab');
  const dynamicLink = document.getElementById('heroDynamicLink');
  const dynamicLinkText = document.getElementById('heroDynamicLinkText');

  if (slides.length === 0 || tabs.length === 0) return;

  let currentIndex = 0;
  let timer = null;
  const ROTATE_INTERVAL = 6500; // 6.5s per scene

  function showSlide(index) {
    currentIndex = (index + slides.length) % slides.length;

    slides.forEach((slide, i) => {
      if (i === currentIndex) {
        slide.classList.add('active');
        slide.setAttribute('aria-hidden', 'false');
      } else {
        slide.classList.remove('active');
        slide.setAttribute('aria-hidden', 'true');
      }
    });

    tabs.forEach((tab, i) => {
      const isSelected = i === currentIndex;
      tab.classList.toggle('active', isSelected);
      tab.setAttribute('aria-selected', String(isSelected));
      tab.setAttribute('aria-pressed', String(isSelected));
    });

    const activeSlide = slides[currentIndex];
    if (dynamicLink && activeSlide) {
      const linkTarget = activeSlide.dataset.link || '#collections';
      const label = activeSlide.dataset.label || 'this space';
      dynamicLink.href = linkTarget;
      if (dynamicLinkText) {
        dynamicLinkText.textContent = `Explore ${label.toLowerCase()}`;
      }
    }
  }

  function nextSlide() {
    showSlide(currentIndex + 1);
  }

  function startAutoPlay() {
    stopAutoPlay();
    timer = setInterval(nextSlide, ROTATE_INTERVAL);
  }

  function stopAutoPlay() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', (e) => {
      e.preventDefault();
      const tabIdx = parseInt(tab.dataset.tabIndex, 10);
      showSlide(tabIdx);
      startAutoPlay(); // Reset timer after user interaction
    });
  });

  // Pause on hover or focus
  slider.addEventListener('mouseenter', stopAutoPlay);
  slider.addEventListener('mouseleave', startAutoPlay);
  slider.addEventListener('focusin', stopAutoPlay);
  slider.addEventListener('focusout', startAutoPlay);

  // Keyboard accessibility
  slider.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      e.preventDefault();
      nextSlide();
      startAutoPlay();
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault();
      showSlide(currentIndex - 1);
      startAutoPlay();
    }
  });

  // Initial show
  showSlide(0);
  startAutoPlay();
}
