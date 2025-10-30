const NAV_DELAY = 120;

const tooltipData = {
  biocontrol: {
    Ecoza: "Azadirachtin",
    "Margoshine": "Neem Oil",
    "K-Guard": "Karanjin",
    "WeedX": "MCT",
    "Admira": "Essential Oil",
    "Spindura": "Spinosad",
    "Margospin": "Neem Oil + Spinosad",
    "Mycova": "Beauveria bassiana",
    "Rexora": "Metarhizium anisopliae",
    "Biota (V/H)": "Trichoderma viride",
    "Seira": "Verticillium lecanii",
    "EnCilo": "Paecilomyces fumosoroseus",
    "Neuvita": "Ampelomyces quisqualis"
  },
  biostimulants: {
    IGreen: "Microbial Consortium",
    Zenita: "Neem Limonoids based PGP",
    Cropsia: "Plant Extract based PGP",
    Enrhize: "Arbuscular Mycorrhizal",
    Orgocare: "Stress Management",
    Blooma: "Seaweed based PGP",
    Envicta: "Humic based PGP"
  },
  substrates: {
    Maxineem: "Neem Cake",
    "K-Mix": "Karanja Cake",
    Mystica: "Wetting & Spreading",
    Engrow: "Seed Coating"
  },
  technology: {
    Karyo: "Delivery Platform",
    Wynn: "Microbial Platform"
  }
};

function initDesktopNav() {
  const triggers = document.querySelectorAll('[data-nav-trigger]');
  let closeTimeout;
  let activeDropdown;

  triggers.forEach((trigger) => {
    const dropdown = trigger.parentElement.querySelector('.dropdown');
    if (!dropdown) return;

    trigger.addEventListener('mouseenter', () => openDropdown(dropdown));
    trigger.addEventListener('focus', () => openDropdown(dropdown));

    trigger.parentElement.addEventListener('mouseleave', scheduleClose);
    trigger.parentElement.addEventListener('mouseenter', () => {
      if (closeTimeout) {
        clearTimeout(closeTimeout);
      }
      openDropdown(dropdown);
    });

    dropdown.addEventListener('mouseenter', () => {
      if (closeTimeout) clearTimeout(closeTimeout);
    });

    dropdown.addEventListener('mouseleave', scheduleClose);
  });

  function openDropdown(dropdown) {
    if (activeDropdown && activeDropdown !== dropdown) {
      activeDropdown.classList.remove('show');
    }
    dropdown.classList.add('show');
    activeDropdown = dropdown;
  }

  function scheduleClose() {
    if (closeTimeout) clearTimeout(closeTimeout);
    closeTimeout = setTimeout(() => {
      if (activeDropdown) {
        activeDropdown.classList.remove('show');
        activeDropdown = null;
      }
    }, NAV_DELAY);
  }
}

function populateTooltips() {
  document.querySelectorAll('[data-tooltip-category]').forEach((el) => {
    const category = el.dataset.tooltipCategory;
    const key = el.dataset.tooltipKey;
    const copy = tooltipData[category]?.[key];
    if (!copy) return;

    if (!el.querySelector('.tooltip')) {
      const tip = document.createElement('span');
      tip.className = 'tooltip';
      tip.textContent = copy;
      el.appendChild(tip);
    }
  });
}

function initMobileNav() {
  const toggle = document.querySelector('[data-mobile-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (!toggle || !menu) return;

  toggle.addEventListener('click', () => {
    menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', menu.classList.contains('open'));
  });

  menu.querySelectorAll('[data-accordion]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
      const panel = btn.nextElementSibling;
      if (panel) {
        panel.style.maxHeight = expanded ? null : `${panel.scrollHeight}px`;
      }
    });
  });
}

function initContactForm() {
  const form = document.querySelector('[data-contact-form]');
  if (!form) return;

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const name = formData.get('name');
    const company = formData.get('company');
    const country = formData.get('country');
    const email = formData.get('email');
    const whatsapp = formData.get('whatsapp');
    const interest = formData.get('interest');
    const message = formData.get('message');

    const subject = encodeURIComponent(`Contact Sales Enquiry – ${name || 'Prospect'}`);
    const bodyLines = [
      `Name: ${name}`,
      `Company: ${company}`,
      `Country: ${country}`,
      `Email: ${email}`,
      `WhatsApp: ${whatsapp || 'Not provided'}`,
      `Product Interest: ${interest}`,
      '',
      'Message:',
      message
    ];

    const mailto = `mailto:info@kriya.ltd?subject=${subject}&body=${encodeURIComponent(bodyLines.join('\n'))}`;
    window.location.href = mailto;
    form.reset();
  });
}

function init() {
  populateTooltips();
  initDesktopNav();
  initMobileNav();
  initContactForm();
}

document.addEventListener('DOMContentLoaded', init);
