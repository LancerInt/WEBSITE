import os
from pathlib import Path

ROOT = Path('.')


def slugify(value: str) -> str:
    cleaned = (
        value.lower()
        .replace('&', 'and')
        .replace('+', 'plus')
        .replace('(', '')
        .replace(')', '')
        .replace('/', '-')
    )
    result = []
    for ch in cleaned:
        if ch.isalnum():
            result.append(ch)
        elif ch in {' ', '-', '_'}:
            result.append('-')
    slug = ''.join(result)
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug.strip('-')


def ensure_doc_placeholders(name: str):
    base = slugify(name)
    for suffix in ('tech-sheet', 'regulatory-pack'):
        path = Path('docs') / f"{base}-{suffix}.pdf"
        if not path.exists():
            path.write_text(f"Placeholder for {name} {suffix.replace('-', ' ').title()}\n", encoding='utf-8')

NAV_STRUCTURE = {
    "Products": {
        "Biocontrol": {
            "path": "products/biocontrol.html",
            "items": [
                ("Ecoza", "products/biocontrol/ecoza.html"),
                ("Margoshine", "products/biocontrol/margoshine.html"),
                ("K-Guard", "products/biocontrol/k-guard.html"),
                ("WeedX", "products/biocontrol/weedx.html"),
                ("Admira", "products/biocontrol/admira.html"),
                ("Spindura", "products/biocontrol/spindura.html"),
                ("Margospin", "products/biocontrol/margospin.html"),
                ("Mycova", "products/biocontrol/mycova.html"),
                ("Rexora", "products/biocontrol/rexora.html"),
                ("Biota (V/H)", "products/biocontrol/biota.html"),
                ("Seira", "products/biocontrol/seira.html"),
                ("EnCilo", "products/biocontrol/encilo.html"),
                ("Neuvita", "products/biocontrol/neuvita.html"),
            ],
        },
        "Biostimulants": {
            "path": "products/biostimulants.html",
            "items": [
                ("IGreen", "products/biostimulants/igreen.html"),
                ("Zenita", "products/biostimulants/zenita.html"),
                ("Cropsia", "products/biostimulants/cropsia.html"),
                ("Blooma", "products/biostimulants/blooma.html"),
                ("Enrhize", "products/biostimulants/enrhize.html"),
                ("Orgocare", "products/biostimulants/orgocare.html"),
                ("Envicta", "products/biostimulants/envicta.html"),
            ],
        },
        "Substrates": {
            "path": "products/substrates.html",
            "items": [
                ("Maxineem", "products/substrates/maxineem.html"),
                ("K-Mix", "products/substrates/kmix.html"),
                ("Mystica", "products/substrates/mystica.html"),
                ("Engrow", "products/substrates/engrow.html"),
            ],
        },
        "Home & Garden": {
            "path": "products/home-garden.html",
            "items": [],
        },
    },
    "Technology": {
        "Karyo": "technology/karyo.html",
        "Wynn": "technology/wynn.html",
    },
}

TOOLTIP_MAP = {
    "Biocontrol": {
        "Ecoza": "Azadirachtin",
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
        "Neuvita": "Ampelomyces quisqualis",
    },
    "Biostimulants": {
        "IGreen": "Microbial Consortium",
        "Zenita": "Neem Limonoids & Proteins",
        "Cropsia": "Plant Extract PGP",
        "Blooma": "Seaweed Extract",
        "Enrhize": "Arbuscular Mycorrhizae",
        "Orgocare": "Stress Management",
        "Envicta": "Humic + Fulvic",
    },
    "Substrates": {
        "Maxineem": "Neem Cake",
        "K-Mix": "Karanja Cake",
        "Mystica": "Wetting Agent",
        "Engrow": "Seed Coating",
    },
    "Technology": {
        "Karyo": "Delivery Platform",
        "Wynn": "Microbial Platform",
    }
}

HOME_GARDEN_PRODUCTS = [
    ("Ecoza Rix", "Natural pest control for vegetables and ornamentals."),
    ("K-Rix", "Fast knockdown against sucking pests."),
    ("MargoRix", "Neem-based defense for gardens."),
    ("Spindura Rix", "Caterpillar and thrip management."),
    ("Mycova", "Biological control for home growers."),
    ("Rexora", "Protects against soil-dwelling pests."),
    ("Biota", "Supports root health and vigor."),
    ("Seira", "Controls soft-bodied insects."),
    ("Encilo", "Coverage for whiteflies and aphids."),
    ("Neuvita", "Foliar defense spray."),
    ("Zenita", "Foliar nutrition booster."),
    ("Cropsia", "Plant vitality enhancer."),
    ("Envicta", "Soil conditioner for pots."),
    ("IGreen NPK", "Nutrient unlocking microbes."),
    ("IGreen Soil+", "Soil resilience support."),
    ("IGreen Tres", "Growth promotion blend."),
    ("IGreen Shield", "Disease resistance shield."),
    ("Admira Adrlc", "Garlic oil-based defense."),
    ("Admira Admon", "Cinnamon oil-powered care."),
    ("Admira Adyme", "Thyme oil protection."),
]

BIOCONTROL_PAGES = {
    "ecoza": {
        "title": "Ecoza",
        "overview": "Ecoza delivers broad-spectrum control of sucking pests using premium azadirachtin sourced from carefully curated neem groves. Its residue-conscious formulation is optimized for export-quality produce and demanding regulatory environments.",
        "cfu": None,
        "variants": [
            ("Max", "Azadirachtin (3%) EC"),
            ("Ace", "Azadirachtin (1.2%) EC"),
            ("Rix", "Azadirachtin (1.2%) EC"),
            ("Pro", "Azadirachtin (0.3%) EC"),
        ],
    },
    "k-guard": {
        "title": "K-Guard",
        "overview": "K-Guard leverages karanjin actives to interrupt pest feeding and oviposition without harming beneficial insects. Tailored for IPM programs seeking rapid results with organic certification support.",
        "cfu": None,
        "variants": [
            ("K-Guard", "Karanjin (2%) EC"),
            ("K-Rix", "Karanjin (5%) EC"),
        ],
    },
    "margoshine": {
        "title": "Margoshine",
        "overview": "Margoshine is a cold-pressed neem oil line offering exceptional sheen and spread for horticultural crops. Its stable emulsion technology ensures consistent field performance across climates.",
        "cfu": None,
        "variants": [
            ("Margoshine 70%", "Neem Oil (70%) EC"),
            ("MargoRix", "Neem Oil (35%) EC"),
        ],
    },
    "spindura": {
        "title": "Spindura",
        "overview": "Spindura brings spinosad power for rapid knockdown of caterpillars, thrips, and leafminers. Engineered for resistance management programs requiring fast action and export compliance.",
        "cfu": None,
        "variants": [
            ("Pro", "Spinosad (2.5%) EC"),
            ("Rix", "Spinosad (12%) EC"),
            ("Plus", "Spinosad (25.2%) EC"),
        ],
    },
    "margospin": {
        "title": "Margospin",
        "overview": "Margospin combines neem oil with spinosad for a dual-mode approach against stubborn pest pressure. The formulation is designed to reduce spray cycles while maintaining organic integrity.",
        "cfu": None,
        "variants": [
            (None, "Neem Oil 70% + Spinosad 1.2% EC"),
        ],
    },
    "admira": {
        "title": "Admira",
        "overview": "Admira is a versatile essential-oil platform that blends culinary-grade extracts into potent bioinsecticides. Each variant offers targeted activity and sensory-friendly field performance.",
        "cfu": None,
        "variants": [
            ("Adyme", "Thyme Oil EC / WSP"),
            ("Adrlc", "Garlic Oil EC / WSP"),
            ("Adove", "Clove Oil EC / WSP"),
            ("Admon", "Cinnamon Oil EC / WSP"),
        ],
    },
    "weedx": {
        "title": "WeedX",
        "overview": "WeedX is a botanical contact herbicide built on medium-chain triglycerides. It provides quick desiccation of young weeds and can be tank-mixed within regenerative programs.",
        "cfu": None,
        "variants": [
            (None, "Non-selective botanical herbicide"),
        ],
    },
    "mycova": {
        "title": "Mycova",
        "overview": "Mycova features Beauveria bassiana for comprehensive biological control of whiteflies, aphids, and thrips. High CFU counts and stable spores ensure dependable performance.",
        "cfu": "1x10^10",
        "variants": [
            ("Mycova EC", "Beauveria bassiana (1x10^10 cfu/mL) EC"),
            ("Mycova WP", "Beauveria bassiana (1x10^10 cfu/g) WP"),
        ],
    },
    "rexora": {
        "title": "Rexora",
        "overview": "Rexora deploys Metarhizium anisopliae spores to manage soil and foliar insects. Its high-density formulations integrate seamlessly with precision agriculture schedules.",
        "cfu": "1x10^10",
        "variants": [
            ("Rexora EC", "Metarhizium anisopliae (1x10^10 cfu/mL) EC"),
            ("Rexora WP", "Metarhizium anisopliae (1x10^10 cfu/g) WP"),
        ],
    },
    "biota": {
        "title": "Biota (V/H)",
        "overview": "Biota blends Trichoderma viride and harzianum strains to protect roots and enhance soil microbiology. It supports transplant vigor and disease suppression in high-value crops.",
        "cfu": "1x10^8",
        "variants": [
            ("Biota V-EC", "Trichoderma viride (1x10^8 cfu/mL) EC"),
            ("Biota V-WP", "Trichoderma viride (1x10^8 cfu/g) WP"),
            ("Biota H-EC", "Trichoderma harzianum (1x10^8 cfu/mL) EC"),
            ("Biota H-WP", "Trichoderma harzianum (1x10^8 cfu/g) WP"),
        ],
    },
    "seira": {
        "title": "Seira",
        "overview": "Seira utilises Verticillium lecanii to target soft-bodied insects while protecting pollinators. Stable CFU levels deliver reliable field persistence across climates.",
        "cfu": "1x10^10",
        "variants": [
            ("Seira EC", "Verticillium lecanii (1x10^10 cfu/mL) EC"),
            ("Seira WP", "Verticillium lecanii (1x10^10 cfu/g) WP"),
        ],
    },
    "encilo": {
        "title": "EnCilo",
        "overview": "EnCilo provides Paecilomyces fumosoroseus to suppress whiteflies and mealybugs. Its formulations maintain viability under tropical logistics and field conditions.",
        "cfu": "1x10^10",
        "variants": [
            ("EnCilo EC", "Paecilomyces fumosoroseus (1x10^10 cfu/mL)"),
            ("EnCilo WP", "Paecilomyces fumosoroseus (1x10^10 cfu/g)"),
        ],
    },
    "neuvita": {
        "title": "Neuvita",
        "overview": "Neuvita brings Ampelomyces quisqualis to manage powdery mildew complexes. Its balanced EC and WP formats ensure compatibility with organic spray programs.",
        "cfu": "1x10^10",
        "variants": [
            ("Neuvita EC", "Ampelomyces quisqualis (1x10^10 cfu/mL) EC"),
            ("Neuvita WP", "Ampelomyces quisqualis (1x10^10 cfu/g) WP"),
        ],
    },
}

BIOSTIMULANT_PAGES = {
    "igreen": {
        "title": "IGreen",
        "overview": "IGreen is a modular microbial consortium built to unlock soil nutrients, defend against stress, and drive resilient growth. Four targeted blends address core agronomic challenges.",
        "variants": [
            ("NPK", "Paenibacillus elgii, Bacillus mucilaginosus, Paenibacillus polymyxa", "Consortium for N-P-K", "SL / WP (3x10^10 cfu/mL)"),
            ("Soil+", "Paenibacillus chibensis, Bacillus subtilis, Bacillus pumilus", "Disease suppression", "SL / WP (3x10^10 cfu/mL)"),
            ("Tres", "Paenibacillus chibensis, Bacillus mycoides, Bacillus endophyticus", "Growth promotion", "SL / WP (3x10^10 cfu/mL)"),
            ("Shield", "Bacillus licheniformis, Bacillus amyloliquefaciens, Bacillus subtilis", "Disease resistance", "SL / WP (3x10^10 cfu/mL)"),
        ],
    },
    "zenita": {
        "title": "Zenita",
        "overview": "Zenita harnesses water-soluble neem limonoids and proteins to deliver foliar nutrition and plant growth promotion with excellent compatibility in fertigation systems.",
        "formulation": "SL / WSP",
    },
    "cropsia": {
        "title": "Cropsia",
        "overview": "Cropsia combines moringa and Adhatoda vasica extracts to revitalise crops under abiotic stress, supporting greener canopies and improved yields.",
        "formulation": "SL / WSP",
    },
    "enrhize": {
        "title": "Enrhize",
        "overview": "Enrhize supplies high-density Glomus spp. propagules that colonise roots rapidly, improving nutrient uptake and resilience in challenging soils.",
        "formulation": "Powder",
    },
    "orgocare": {
        "title": "Orgocare",
        "overview": "Orgocare is a plant-extract blend designed to mitigate stress responses and maintain metabolic balance during crop transitions.",
        "formulation": "SL",
    },
    "blooma": {
        "title": "Blooma",
        "overview": "Blooma utilises premium seaweed extracts to boost flowering, fruit set, and abiotic stress tolerance in high-value crops.",
        "formulation": "SL / WSP",
    },
    "envicta": {
        "title": "Envicta",
        "overview": "Envicta combines humic, fulvic, and amino acids to restore soil structure and enhance nutrient availability in organic systems.",
        "formulation": "SL / WSP",
    },
}

SUBSTRATE_PAGES = {
    "maxineem": {
        "title": "Maxineem",
        "overview": "Maxineem is a rich neem cake substrate that improves soil organic matter, suppresses nematodes, and supports sustainable fertility programs.",
    },
    "kmix": {
        "title": "K-Mix",
        "overview": "K-Mix delivers karanja cake nutrition with balanced NPK values, ideal for blending into potting mixes and regenerative soil systems.",
    },
    "mystica": {
        "title": "Mystica",
        "overview": "Mystica is a wetting and spreading adjuvant that enhances spray coverage while remaining gentle on crops and beneficials.",
    },
    "engrow": {
        "title": "Engrow",
        "overview": "Engrow offers a protective seed coating matrix that boosts germination, early vigor, and microbial compatibility.",
    },
}

TECH_PAGES = {
    "karyo": {
        "title": "Karyo Delivery Platform",
        "category": "Delivery Platform",
        "purpose": "To transform nature-derived molecules into scalable, effective agricultural solutions.",
        "components": [
            "Botanical Actives Formulation",
            "Microbial Actives Formulation",
            "Advanced Delivery (Encapsulation)",
            "Formulation Science",
            "Stability & Handling",
            "Sustainability",
        ],
        "audience": "50% Marketing, 50% Technical",
    },
    "wynn": {
        "title": "Wynn Microbial Platform",
        "category": "Microbial Technology Platform",
        "purpose": "End-to-end development and production of microbial-based agricultural solutions.",
        "components": [
            "Microbial Discovery",
            "Bioactive Compound ID",
            "Fermentation Technology (Solid-State)",
            "Metabolite Extraction & Purification",
            "Media Optimization",
            "Proprietary Formulation",
        ],
        "audience": "50% Marketing, 50% Technical",
    },
}


def build_head(title: str, base: str) -> str:
    fonts = (
        "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap"
    )
    icons = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,500,0,0"
    return f"""
    <head>
      <meta charset=\"utf-8\">
      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
      <title>{title} · Kriya Ltd</title>
      <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
      <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
      <link href=\"{fonts}\" rel=\"stylesheet\">
      <link href=\"{icons}\" rel=\"stylesheet\">
      <link rel=\"stylesheet\" href=\"{base}assets/css/styles.css\">
      <link rel=\"icon\" href=\"{base}assets/img/placeholder.svg\" type=\"image/svg+xml\">
    </head>
    """


def build_nav(base: str) -> str:
    def build_products_dropdown():
        cols = []
        for category, info in NAV_STRUCTURE["Products"].items():
            if info["items"]:
                items = "".join(
                    f"<li data-tooltip-category=\"{category.lower()}\" data-tooltip-key=\"{name}\"><a href=\"{base}{href}\">{name}</a></li>"
                    for name, href in info["items"]
                )
                items_html = f"<ul>{items}</ul>"
            else:
                items_html = f"<ul><li><a href=\"{base}{info['path']}\">Explore Range</a></li></ul>"
            subtitle = f"<h4>{category}</h4>" if category != "Home & Garden" else "<h4>Home & Garden</h4><p>Consumer friendly packs</p>"
            cols.append(f"<div>{subtitle}{items_html}</div>")
        return "".join(cols)

    def build_mobile_products():
        blocks = []
        for category, info in NAV_STRUCTURE["Products"].items():
            items = "".join(
                f"<li><a href=\"{base}{href}\">{name}</a></li>" for name, href in info["items"]
            )
            if items:
                items = f"<ul class=\"submenu\">{items}</ul>"
            else:
                items = ""
            blocks.append(
                f"<li><a href=\"{base}{info['path']}\">{category}</a>{items}</li>"
            )
        return "".join(blocks)

    tech_desktop = "".join(
        f"<li data-tooltip-category=\"technology\" data-tooltip-key=\"{name}\"><a href=\"{base}{href}\">{name}</a></li>"
        for name, href in NAV_STRUCTURE["Technology"].items()
    )
    tech_mobile = "".join(
        f"<li><a href=\"{base}{href}\">{name}</a></li>" for name, href in NAV_STRUCTURE["Technology"].items()
    )

    return f"""
    <header class=\"site-header\">
      <div class=\"wrapper\">
        <div class=\"navbar\">
          <a class=\"logo-placeholder\" href=\"{base}index.html\">
            <span class=\"logo-mark\">K</span>
            <span>Kriya Ltd</span>
          </a>
          <nav class=\"primary-nav\">
            <ul>
              <li><a href=\"{base}about.html\">About</a></li>
              <li data-nav-trigger>
                <button type=\"button\" data-nav-trigger>Products</button>
                <div class=\"dropdown multi-column\">
                  {build_products_dropdown()}
                </div>
              </li>
              <li data-nav-trigger>
                <button type=\"button\" data-nav-trigger>Technology</button>
                <div class=\"dropdown\">
                  <div>
                    <h4>Platforms</h4>
                    <ul>
                      {tech_desktop}
                    </ul>
                  </div>
                </div>
              </li>
              <li><a href=\"{base}contract-manufacturing.html\">Contract Manufacturing</a></li>
              <li><a href=\"{base}contact.html\">Contact</a></li>
            </ul>
          </nav>
          <div class=\"nav-cta\">
            <a class=\"secondary\" href=\"{base}products/biocontrol.html\">Browse Products</a>
            <a class=\"primary\" href=\"{base}contact.html\">Contact Sales</a>
          </div>
          <button class=\"mobile-toggle\" type=\"button\" data-mobile-toggle aria-expanded=\"false\">
            <span class=\"material-symbols-outlined\">menu</span>
          </button>
        </div>
      </div>
      <div class=\"mobile-menu\" data-mobile-menu>
        <ul>
          <li><a href=\"{base}index.html\">Home</a></li>
          <li><a href=\"{base}about.html\">About</a></li>
          <li>
            <button type=\"button\" data-accordion aria-expanded=\"false\">Products</button>
            <div class=\"submenu\">
              {build_mobile_products()}
            </div>
          </li>
          <li>
            <button type=\"button\" data-accordion aria-expanded=\"false\">Technology</button>
            <div class=\"submenu\">
              <ul>{tech_mobile}</ul>
            </div>
          </li>
          <li><a href=\"{base}contract-manufacturing.html\">Contract Manufacturing</a></li>
          <li><a href=\"{base}contact.html\">Contact</a></li>
        </ul>
        <div class=\"cta-group\">
          <a class=\"btn-primary\" href=\"{base}contact.html\">Contact Sales</a>
          <a class=\"btn-outline\" href=\"{base}products/biocontrol.html\">Browse Products</a>
        </div>
      </div>
    </header>
    """


def build_footer(base: str) -> str:
    socials = [
        ("LinkedIn", "https://www.linkedin.com/company/108402158/"),
        ("YouTube", "https://www.youtube.com/@kriyabiosys"),
        ("Twitter", "https://x.com/kriyabiosys"),
        ("Instagram", "https://www.instagram.com/kriyabiosys/"),
        ("Facebook", "https://www.facebook.com/kriyabiosys"),
        ("Email", "mailto:info@kriya.ltd"),
        ("WhatsApp", "https://wa.me/916385848466"),
    ]
    social_links = "".join(
        f"<a href=\"{url}\" target=\"_blank\" rel=\"noopener\">{name}</a>" for name, url in socials
    )
    return f"""
    <footer class=\"footer\">
      <div class=\"wrapper\">
        <div class=\"footer-top\">
          <div class=\"links\">
            <a href=\"{base}about.html\">About</a>
            <a href=\"{base}products/biocontrol.html\">Products</a>
            <a href=\"{base}technology/karyo.html\">Technology</a>
            <a href=\"{base}contact.html\">Contact</a>
            <a href=\"{base}contract-manufacturing.html\">Contract Manufacturing</a>
          </div>
          <div class=\"meta\">
            {social_links}
          </div>
          <div class=\"disclaimer\">
            For usage/dosage information consult product literature and regional agronomists.
          </div>
          <div class=\"meta\">
            <span>© Kriya Ltd 2025 · All rights reserved.</span>
            <a href=\"{base}docs/privacy.pdf\">Privacy</a>
            <a href=\"{base}docs/responsible-use.pdf\">Responsible Use</a>
          </div>
        </div>
      </div>
    </footer>
    """


def build_layout(title: str, base: str, body: str) -> str:
    head = build_head(title, base)
    nav = build_nav(base)
    footer = build_footer(base)
    return f"<!DOCTYPE html><html lang=\"en\">{head}<body>{nav}<main>{body}</main>{footer}<script src=\"{base}assets/js/main.js\" defer></script></body></html>"


def write_page(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def index_page() -> str:
    badges = "".join(
        f"<span>{badge}</span>"
        for badge in [
            "Residue-conscious crop inputs",
            "Certified & regulatory-ready formulations",
            "Reliable global B2B supply",
        ]
    )
    categories = [
        ("Biocontrol", "Natural solutions that manage insects and pathogens while reducing chemical residues."),
        ("Biostimulants", "Products that enhance plant resilience, nutrient uptake, and growth performance."),
        ("Substrates", "Organic soil amendments and seed treatments that improve soil fertility and crop establishment."),
        ("Home & Garden", "Consumer-friendly packs bringing biological crop care to everyday growers."),
    ]
    category_cards = "".join(
        f"<div class=\"card\"><h3>{title}</h3><p>{desc}</p></div>" for title, desc in categories
    )
    featured = [
        ("Ecoza", "A premium azadirachtin-based bioinsecticide offering broad-spectrum control of sucking pests."),
        ("Mycova", "Beauveria bassiana delivering effective control against whiteflies, aphids, and thrips."),
        ("IGreen NPK", "A microbial consortium that mobilizes soil nutrients and supports plant health."),
        ("Spindura", "Spinosad formulations designed for fast-acting control of caterpillars and thrips."),
    ]
    feature_links = {
        "Ecoza": "products/biocontrol/ecoza.html",
        "Mycova": "products/biocontrol/mycova.html",
        "IGreen NPK": "products/biostimulants/igreen.html",
        "Spindura": "products/biocontrol/spindura.html",
    }
    featured_cards = "".join(
        f"<div class=\"card\"><h3>{name}</h3><p>{desc}</p><a class=\"list-pill\" href=\"{feature_links[name]}\">Explore</a></div>"
        for name, desc in featured
    )
    hero = f"""
    <section class=\"hero\">
      <div class=\"wrapper hero-content\">
        <div class=\"hero-copy\">
          <h1>Organic Crop Care Solutions – Trusted Inputs for a Growing World</h1>
          <p class=\"lead\">Kriya delivers residue-conscious biocontrols, biostimulants, and substrates designed for modern agriculture. Our products are certified, regulatory-ready, and tailored for international distributors seeking reliability and performance.</p>
          <div class=\"badge-list\">{badges}</div>
          <div class=\"cta-group\">
            <a class=\"btn-primary\" href=\"products/biocontrol.html\">Browse Products</a>
            <a class=\"btn-outline\" href=\"docs/kriya-product-catalog.pdf\">Download Product Catalog</a>
          </div>
        </div>
        <div class=\"hero-media\">
          <img src=\"assets/img/placeholder.svg\" alt=\"Organic crop care solutions illustration\">
        </div>
      </div>
    </section>
    """

    why_cards = [
        ("R&D Expertise", "Our team combines microbial discovery, plant science, and advanced formulation technology to create scalable solutions."),
        ("Certified & Trusted", "Every product aligns with EU 2019/1009 and leading organic certifications for compliance-ready distribution."),
        ("Premium Quality", "Rigorous QA/QC systems guarantee stable performance, shelf-life, and farmer satisfaction."),
        ("Strong Partnerships", "We collaborate with distributors to deliver reliable supply, technical support, and business growth."),
    ]
    why_section = "".join(
        f"<div class=\"card\"><h3>{title}</h3><p>{desc}</p></div>" for title, desc in why_cards
    )

    tech_cards = "".join(
        f"<div class=\"tile\"><strong>{title}</strong><p>{copy}</p></div>" for title, copy in [
            ("Karyo", "Transforms botanical and microbial actives into stable, scalable formulations."),
            ("Wynn", "End-to-end microbial development encompassing discovery to proprietary formulation."),
            ("Contract Manufacturing", "CO₂ extraction, fermentation, formulation, and packing for partners."),
        ]
    )

    cert_strip = "".join(
        f"<span class=\"highlight-pill\">{label}</span>" for label in [
            "OMRI", "Ecocert", "ISO", "GMP", "Chemexcil", "SHEFEXIL"
        ]
    )

    return "".join([
        hero,
        "<section class='content-section'><div class='wrapper'><div class='section-heading'><h2 class='section-title'>Why Kriya?</h2><p>We blend science-led R&D with premium production infrastructure to deliver dependable organic crop care inputs for international partners.</p></div><div class='card-grid'>",
        why_section,
        "</div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='section-heading'><h2 class='section-title'>Product Categories</h2><p>Our portfolio spans four categories designed to deliver performance across crops, soils, and climates.</p></div><div class='card-grid'>",
        category_cards,
        "</div></div></section>",
        "<section class='featured-strip'><div class='wrapper'><div class='section-heading'><h2 class='section-title'>Featured Products</h2><p>Explore a selection of flagship solutions trusted by distributors worldwide.</p></div><div class='card-grid'>",
        featured_cards,
        "</div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='section-heading'><h2 class='section-title'>Technology & Contract Manufacturing</h2><p>Beyond individual products, Kriya invests in platforms and partnerships that unlock long-term value.</p></div><div class='tiles'>",
        tech_cards,
        "</div></div></section>",
        f"<section class='content-section'><div class='wrapper'><div class='lead-strip'><h2 class='section-title'>Certifications</h2><p>Our formulations are aligned with international standards assuring product safety, quality, and market readiness.</p><div>{cert_strip}</div></div></div></section>",
    ])


def about_page() -> str:
    sections = [
        ("Who We Are", "Kriya Ltd develops and supplies certified organic pesticides, biostimulants, and substrates designed for residue-conscious agriculture. Headquartered in Tamil Nadu, India, we combine science-led R&D with reliable large-scale production to deliver premium solutions for international distributors."),
        ("Our Mission", "To transform nature-derived actives into effective, compliant, and scalable inputs that enable growers to reduce chemical residues, improve soil health, and achieve sustainable yields."),
        ("Our Vision", "A future where every farmer has access to high-performance crop care solutions that are safe for people, soil, and the planet—supported by trusted partnerships worldwide."),
    ]
    values = [
        ("Integrity", "We ensure every product meets regulatory, quality, and ethical standards."),
        ("Innovation", "We invest in discovery and formulation science to continuously improve efficacy and sustainability."),
        ("Collaboration", "We work hand-in-hand with global distributors to unlock market opportunities."),
        ("Sustainability", "We prioritize eco-friendly inputs that protect natural resources for future generations."),
    ]
    values_cards = "".join(f"<div class='card'><h3>{title}</h3><p>{copy}</p></div>" for title, copy in values)

    how_cards = [
        ("Facilities", "Our facilities integrate microbial fermentation, advanced extraction, formulation, and packaging capabilities. With in-house analytical labs and QA/QC systems, we guarantee compliance with EU 2019/1009, organic certifications, and international safety standards."),
        ("Why Organic?", "Organic agriculture meets rising consumer demand, regulatory pressure, and climate resilience needs. Our portfolio equips distributors with scientifically validated solutions ready for global markets."),
        ("Distributor Partnership", "We provide technical documentation, regulatory guidance, marketing collateral, and consistent delivery to support partner growth."),
    ]

    how_cards_html = "".join(f"<div class='card'><h3>{title}</h3><p>{copy}</p></div>" for title, copy in how_cards)

    return "".join([
        "<section class='page-hero'><div class='wrapper'><h1>About Kriya Ltd</h1><p>Premium, eco-friendly crop care inputs backed by science-led R&D, strong manufacturing, and trusted global partnerships.</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='card-grid'>",
        "".join(f"<div class='card'><h3>{title}</h3><p>{copy}</p></div>" for title, copy in sections),
        "</div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='section-heading'><h2 class='section-title'>Our Values</h2><p>Guiding principles that shape every product we create and every partnership we build.</p></div><div class='card-grid'>",
        values_cards,
        "</div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='card-grid'>",
        how_cards_html,
        "</div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='lead-strip'><h2 class='section-title'>Why Kriya?</h2><div class='tiles'>",
        "".join(
            f"<div class='tile'><strong>{title}</strong><p>{copy}</p></div>"
            for title, copy in [
                ("Premium Quality", "Rigorously tested and validated products."),
                ("Eco-Friendly", "Natural actives with proven performance."),
                ("Science-Led R&D", "Strong pipeline of innovative formulations."),
                ("Trusted Partner", "Reliable supply and responsive support."),
            ]
        ),
        "</div></div></div></section>",
    ])


def contract_page() -> str:
    capabilities = [
        "Supercritical CO₂ Extraction – High-purity actives from botanical sources with no solvent residues.",
        "Solvent & Aqueous Extraction – Scalable methods for diverse bioactive fractions.",
        "Microbial Fermentation & Metabolite Extraction – Production of beneficial microbes, spores, and metabolites.",
        "Formulation & Packing – Custom dosage forms including EC, SC, WP, WSP, tablets, and RTU sprays.",
        "R&D & Analytical Services – Stability studies, assay development, and regulatory documentation support.",
    ]
    steps = ["Scope", "Feasibility", "Pilot", "Scale-Up", "Supply"]
    qa = [
        "Identity & assay verification",
        "Microbial load testing",
        "Residual solvent analysis",
        "Shelf-life & stability validation",
        "Packaging integrity checks",
        "Traceability and batch documentation",
    ]

    return "".join([
        "<section class='page-hero'><div class='wrapper'><h1>End-to-end manufacturing for sustainable agri-inputs</h1><p>Kriya offers a full suite of contract manufacturing services for companies seeking to develop and scale natural crop care solutions. From extraction and microbial fermentation to formulation and packaging, we provide the technical expertise, facilities, and QA/QC systems to bring your products to market faster.</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='lead-strip'><h2 class='section-title'>Core Capabilities</h2><ul class='check-list'>",
        "".join(f"<li>{item}</li>" for item in capabilities),
        "</ul></div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='section-heading'><h2 class='section-title'>Engagement Model</h2><p>Collaborative steps that accelerate partner products from concept to commercial supply.</p></div><div class='tiles'>",
        "".join(f"<div class='tile'><strong>{step}</strong><p>Stage {i+1} of our engagement journey.</p></div>" for i, step in enumerate(steps)),
        "</div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='lead-strip'><h2 class='section-title'>QA/QC Focus</h2><div>",
        "".join(f"<span class='highlight-pill'>{item}</span>" for item in qa),
        "</div></div></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='two-column'><div class='card'><h3>Equipment & Scale</h3><p>Our facilities are equipped to handle small pilot runs through full-scale commercial batches, ensuring flexibility for start-ups, scale-ups, and established distributors.</p></div><div class='card'><h3>Packaging Options</h3><p>Bulk – drums, IBCs, and industrial packs for B2B supply.<br>Retail – sachets, bottles, water-soluble tablets, and RTU sprays with eco-friendly packaging.</p></div></div></div></section>",
    ])


def contact_page() -> str:
    return "".join([
        "<section class='page-hero'><div class='wrapper'><h1>Contact Sales</h1><p>Share your requirements and our team will tailor product, regulatory, and supply information for your market.</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='two-column'><div class='card'><h3>Connect with Kriya</h3><p>Email: <a href='mailto:info@kriya.ltd'>info@kriya.ltd</a><br>WhatsApp: <a href='https://wa.me/916385848466'>+91 6385848466</a></p><p>LinkedIn: <a href='https://www.linkedin.com/company/108402158/'>@kriyabiosys</a><br>Twitter: <a href='https://x.com/kriyabiosys'>@kriyabiosys</a></p><p>We respond within 2 business days to discuss distribution, private label, and contract manufacturing opportunities.</p></div><form class='contact-form' data-contact-form><div><label for='name'>Name</label><input id='name' name='name' required></div><div><label for='company'>Company</label><input id='company' name='company' required></div><div><label for='country'>Country</label><input id='country' name='country' required></div><div><label for='email'>Email</label><input id='email' name='email' type='email' required></div><div><label for='whatsapp'>WhatsApp (optional)</label><input id='whatsapp' name='whatsapp' type='tel'></div><div><label for='interest'>Product Interest</label><select id='interest' name='interest' required><option value='' disabled selected>Select a category</option><option>Biocontrol</option><option>Biostimulants</option><option>Substrates</option><option>Home &amp; Garden</option><option>Technology Platform</option><option>Contract Manufacturing</option></select></div><div><label for='message'>Message</label><textarea id='message' name='message' rows='5' required></textarea></div><button type='submit'>Compose Email</button></form></div></div></section>",
    ])


def list_page(title: str, intro: str, cards: str) -> str:
    return f"<section class='page-hero'><div class='wrapper'><h1>{title}</h1><p>{intro}</p></div></section><section class='content-section'><div class='wrapper'><div class='card-grid'>{cards}</div></div></section>"


def build_product_card(name: str, description: str, link: str) -> str:
    return f"<div class='card'><h3>{name}</h3><p>{description}</p><a class='list-pill' href='{link}'>View Product</a></div>"


def biocontrol_page() -> str:
    cards = []
    for key, data in BIOCONTROL_PAGES.items():
        cards.append(
            build_product_card(
                data["title"],
                data["overview"],
                f"biocontrol/{key}.html",
            )
        )
    return list_page(
        "Biocontrol Portfolio",
        "Natural solutions that manage insects and pathogens while reducing chemical residues.",
        "".join(cards),
    )


def biostimulant_page() -> str:
    cards = []
    for key, data in BIOSTIMULANT_PAGES.items():
        cards.append(
            build_product_card(
                data["title"],
                data["overview"],
                f"biostimulants/{key}.html",
            )
        )
    return list_page(
        "Biostimulants Portfolio",
        "Products that enhance plant resilience, nutrient uptake, and growth performance.",
        "".join(cards),
    )


def substrates_page() -> str:
    cards = []
    for key, data in SUBSTRATE_PAGES.items():
        cards.append(
            build_product_card(
                data["title"],
                data["overview"],
                f"substrates/{key if key != 'kmix' else 'kmix'}.html",
            )
        )
    return list_page(
        "Substrates Portfolio",
        "Organic soil amendments and seed treatments that improve soil fertility and crop establishment.",
        "".join(cards),
    )


def home_garden_page() -> str:
    cards = "".join(
        f"<div class='consumer-card'><img src='../assets/img/placeholder.svg' alt='{name} packshot placeholder'><strong>{name}</strong><p>{benefit}</p><a class='list-pill' href='../docs/{slugify(name)}-product-sheet.pdf'>Download Product Sheet</a></div>"
        for name, benefit in HOME_GARDEN_PRODUCTS
    )
    return "".join([
        "<section class='page-hero'><div class='wrapper'><h1>Home &amp; Garden Collection</h1><p>Consumer-ready packs that bring the benefits of biocontrols and biostimulants to everyday growers.</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='consumer-grid'>",
        cards,
        "</div></div></section>",
    ])


def tech_page(slug: str) -> str:
    data = TECH_PAGES[slug]
    components = "".join(f"<li>{item}</li>" for item in data["components"])
    return "".join([
        f"<section class='page-hero'><div class='wrapper'><h1>{data['title']}</h1><p>{data['purpose']}</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='lead-strip'><h2 class='section-title'>Core Capabilities</h2><ul class='check-list'>",
        components,
        "</ul></div></div></section>",
        f"<section class='content-section'><div class='wrapper'><div class='card'><h3>Target Audience</h3><p>{data['audience']}</p></div></div></section>",
    ])


def product_detail_page(category: str, slug: str, data: dict) -> str:
    breadcrumbs = {
        "biocontrol": ("Biocontrol Portfolio", "../../products/biocontrol.html"),
        "biostimulants": ("Biostimulants Portfolio", "../../products/biostimulants.html"),
        "substrates": ("Substrates Portfolio", "../../products/substrates.html"),
    }
    crumb_title, crumb_link = breadcrumbs[category]
    lead = f"<a class='list-pill' href='{crumb_link}'>← {crumb_title}</a>"
    overview = data["overview"]
    download_base = slugify(data["title"])
    downloads = f"<div class='download-links'><a href='../../docs/{download_base}-tech-sheet.pdf'><span class='material-symbols-outlined'>description</span>Tech Sheet</a><a href='../../docs/{download_base}-regulatory-pack.pdf'><span class='material-symbols-outlined'>inventory_2</span>Regulatory Pack</a></div>"
    if category == "biostimulants" and slug == "igreen":
        table_rows = "".join(
            f"<tr><td>{variant}</td><td>{actives}</td><td>{utility}</td><td>{form}</td></tr>"
            for variant, actives, utility, form in data["variants"]
        )
    else:
        table_rows = "".join(
            f"<tr><td>{variant or data['title']}</td><td>{details}</td><td>0.5–1.0 L/ha</td><td>Spray / drip as directed</td></tr>"
            for variant, details in data.get("variants", [])
        )

    table = f"<div class='table-wrapper'><table><thead><tr><th>Variant</th><th>Details</th><th>Recommended Dosage</th><th>Application</th></tr></thead><tbody>{table_rows}</tbody></table></div>"

    compliance = []
    if data.get("cfu"):
        compliance.append(f"Guaranteed CFU: {data['cfu']}")
    compliance.extend([
        "Aligned with EU 2019/1009",
        "Supports leading organic certifications",
        "Residue-conscious formulation",
        "Traceable batch documentation",
    ])

    compliance_html = "".join(f"<li>{item}</li>" for item in compliance)

    body = "".join([
        f"<section class='page-hero'><div class='wrapper'>{lead}<h1>{data['title']}</h1><p>{overview}</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='two-column'><div><h2 class='section-title'>Variants</h2>",
        table,
        downloads,
        "</div><div class='card'><h3>Safety &amp; Compliance</h3><ul class='check-list'>",
        compliance_html,
        "</ul></div></div></div></section>",
    ])
    return body


def substrate_detail_page(slug: str, data: dict) -> str:
    compliance = [
        "Sustainably sourced inputs",
        "Supports organic certification",
        "Consistent particle sizing",
        "Traceable supply",
    ]
    return "".join([
        "<section class='page-hero'><div class='wrapper'><a class='list-pill' href='../../products/substrates.html'>← Substrates Portfolio</a>",
        f"<h1>{data['title']}</h1><p>{data['overview']}</p></div></section>",
        "<section class='content-section'><div class='wrapper'><div class='two-column'><div class='card'><h3>Applications</h3><p>Blend into potting mixes, apply in-field for soil conditioning, or integrate with microbial inoculants as part of regenerative programs.</p></div><div class='card'><h3>Safety &amp; Compliance</h3><ul class='check-list'>",
        "".join(f"<li>{item}</li>" for item in compliance),
        "</ul></div></div><div class='download-links'><a href='../../docs/" + slugify(data['title']) + "-tech-sheet.pdf'><span class='material-symbols-outlined'>description</span>Tech Sheet</a><a href='../../docs/" + slugify(data['title']) + "-regulatory-pack.pdf'><span class='material-symbols-outlined'>inventory_2</span>Regulatory Pack</a></div></div></section>",
    ])


def build_all():
    pages = {
        Path('index.html'): ("Kriya Ltd", '', index_page()),
        Path('about.html'): ("About", '', about_page()),
        Path('contract-manufacturing.html'): ("Contract Manufacturing", '', contract_page()),
        Path('contact.html'): ("Contact", '', contact_page()),
        Path('products/biocontrol.html'): ("Biocontrol", '../', biocontrol_page()),
        Path('products/biostimulants.html'): ("Biostimulants", '../', biostimulant_page()),
        Path('products/substrates.html'): ("Substrates", '../', substrates_page()),
        Path('products/home-garden.html'): ("Home & Garden", '../', home_garden_page()),
        Path('technology/karyo.html'): ("Karyo", '../', tech_page('karyo')),
        Path('technology/wynn.html'): ("Wynn", '../', tech_page('wynn')),
    }

    # Core product document placeholders
    for data in BIOCONTROL_PAGES.values():
        ensure_doc_placeholders(data['title'])
    for data in BIOSTIMULANT_PAGES.values():
        ensure_doc_placeholders(data['title'])
    for data in SUBSTRATE_PAGES.values():
        ensure_doc_placeholders(data['title'])

    # Home & Garden downloads placeholders
    for name, _ in HOME_GARDEN_PRODUCTS:
        filename = slugify(name) + '-product-sheet.pdf'
        path = Path('docs') / filename
        if not path.exists():
            path.write_text(f"Placeholder sheet for {name}\n", encoding='utf-8')

    for slug, data in BIOCONTROL_PAGES.items():
        pages[Path(f'products/biocontrol/{slug}.html')] = (
            data['title'],
            '../../',
            product_detail_page('biocontrol', slug, data),
        )

    for slug, data in BIOSTIMULANT_PAGES.items():
        if slug == 'igreen':
            body = product_detail_page('biostimulants', slug, data)
        else:
            detail = {
                **data,
                "variants": [(data['title'], data.get('formulation', ''))],
            }
            body = product_detail_page('biostimulants', slug, detail)
        pages[Path(f'products/biostimulants/{slug}.html')] = (
            data['title'],
            '../../',
            body,
        )

    for slug, data in SUBSTRATE_PAGES.items():
        pages[Path(f'products/substrates/{slug}.html')] = (
            data['title'],
            '../../',
            substrate_detail_page(slug, data),
        )

    for path, (title, base, body) in pages.items():
        html = build_layout(title, base, body)
        write_page(path, html)


if __name__ == '__main__':
    build_all()
