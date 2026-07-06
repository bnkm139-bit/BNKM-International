#!/usr/bin/env python3
"""Static-site builder for BNKM International Ltd.
Assembles 9 pages from a shared head, nav, and footer + per-page content."""

import os, base64

from scenes import REFINERY, OFFSHORE, ONSHORE, FIG, BAND

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- Custom domain (GitHub Pages). Change this ONE line + the CNAME file. ----
DOMAIN = "bnkminternational.co.uk"
SITE = f"https://{DOMAIN}"

# ---- Brand logo, inlined as a data URI so pages render standalone anywhere ----
with open(os.path.join(OUT, "assets", "_logo_inline.jpg"), "rb") as _f:
    LOGO_URI = "data:image/jpeg;base64," + base64.b64encode(_f.read()).decode()
LOGO_ALT = "BNKM International Ltd., London, UK"

POSITIONING = ("A process engineering and project consultancy company specializing in "
               "hydrocarbons, chemicals, fertilizers, and low-carbon energy transition solutions.")
SUSTAIN = ("Supporting industrial decarbonization and sustainable energy transition "
           "projects globally.")

# Navigation definition: (filename, nav label, is_in_nav)
PAGES = [
    ("index.html",            "Home",              True),
    ("about.html",            "About",             True),
    ("industries.html",       "Industries",        True),
    ("services.html",         "Services",          True),
    ("energy-transition.html","Energy Transition", True),
    ("projects.html",         "Projects",          True),
    ("expertise.html",        "Expertise",         True),
    ("careers.html",          "Careers",           True),
    ("contact.html",          "Contact",           False),  # rendered as CTA button
]

def nav(active):
    items = []
    for fn, label, in_nav in PAGES:
        if not in_nav:
            continue
        cls = ' class="active"' if fn == active else ''
        aria = ' aria-current="page"' if fn == active else ''
        items.append(f'<a href="{fn}"{cls}{aria}>{label}</a>')
    links = "\n        ".join(items)
    return f'''<header class="site-head" id="siteHead">
  <div class="wrap">
    <nav class="nav" aria-label="Primary">
      <a href="index.html" class="brand" aria-label="BNKM International Ltd. — home">
        <img class="brand-logo" src="{LOGO_URI}" width="415" height="150" alt="{LOGO_ALT}">
      </a>
      <div class="nav-links" id="navLinks">
        {links}
        <div class="nav-cta"><a class="btn btn--primary" href="contact.html">Contact <span class="arr">&rarr;</span></a></div>
      </div>
      <button class="nav-toggle" id="navToggle" aria-label="Menu" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img class="foot-logo" src="{LOGO_URI}" width="415" height="150" alt="{LOGO_ALT}">
        <p>{POSITIONING}</p>
        <p style="margin-top:1rem">{SUSTAIN}</p>
      </div>
      <div>
        <h4>Navigate</h4>
        <p><a href="index.html">Home</a></p>
        <p><a href="about.html">About Us</a></p>
        <p><a href="industries.html">Industries</a></p>
        <p><a href="services.html">Services</a></p>
        <p><a href="energy-transition.html">Energy Transition</a></p>
      </div>
      <div>
        <h4>Company</h4>
        <p><a href="projects.html">Projects</a></p>
        <p><a href="expertise.html">Technical Expertise</a></p>
        <p><a href="careers.html">Careers</a></p>
        <p><a href="contact.html">Contact</a></p>
      </div>
      <div>
        <h4>Registered Office</h4>
        <p>132 Waterview House<br>12 Quay Walk<br>Wembley, HA0 1BE<br>United Kingdom</p>
        <p style="margin-top:1rem"><a href="mailto:bnkm139@gmail.com">bnkm139@gmail.com</a><br><a href="tel:+447587481434">+44 7587 481434</a></p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span data-year>2026</span> BNKM International Ltd. &middot; Company Reg. No. 15683113 (England &amp; Wales)</span>
      <span>Engineering design activities for industrial process &amp; production industry</span>
    </div>
  </div>
</footer>
<script>__JS__</script>
</body>
</html>'''

JSONLD = f'''<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"ProfessionalService",
  "name":"BNKM International Ltd.",
  "description":"{POSITIONING}",
  "url":"{SITE}",
  "email":"bnkm139@gmail.com",
  "telephone":"+44-7587481434",
  "foundingDate":"2024",
  "address":{{"@type":"PostalAddress","streetAddress":"132 Waterview House, 12 Quay Walk","addressLocality":"Wembley","postalCode":"HA0 1BE","addressCountry":"GB"}},
  "areaServed":"Worldwide",
  "knowsAbout":["Process Engineering Consultancy","FEED Engineering","Detailed Engineering Solutions","Green Ammonia Engineering","CCUS Consultancy","Refinery Engineering Services","SAF Engineering","Carbon Capture Utilisation and Storage","Dynamic Simulation","Energy Efficiency","Process Optimization","Industrial Decarbonization"]
}}
</script>'''

def head(title, desc, keywords, canonical):
    path = "" if canonical == "index.html" else canonical
    css = open(os.path.join(OUT, "css", "style.css")).read()
    favicon = open(os.path.join(OUT, "assets", "favicon.svg")).read()
    import base64 as _b64
    fav_uri = "data:image/svg+xml;base64," + _b64.b64encode(favicon.encode()).decode()
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="BNKM International Ltd.">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BNKM International Ltd.">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:image" content="{SITE}/assets/bnkm-logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/assets/bnkm-logo.png">
<meta name="theme-color" content="#0A1320">
<link rel="icon" href="{fav_uri}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
<noscript><style>.reveal{{opacity:1!important;transform:none!important}}</style></noscript>
{JSONLD}
</head>
<body>'''

# Shared keyword string for SEO
KW = ("Process Engineering Consultancy, FEED Engineering, Green Ammonia Engineering, "
      "CCUS Consultancy, Refinery Engineering Services, SAF Engineering, Detailed "
      "Engineering Solutions, process optimization, dynamic simulation, carbon reduction, "
      "energy efficiency, utility integration, industrial decarbonization, ASME, API, ISO, IEC, NFPA")


def write(fn, title, desc, content, head_on_ink=False):
    active = fn
    js = open(os.path.join(OUT, "js", "main.js")).read()
    footer = FOOTER.replace("__JS__", js)
    html = head(title, desc, KW, fn) + "\n" + nav(active) + "\n" + content + "\n" + footer
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(html)
    print("wrote", fn, len(html), "bytes")


# Reusable schematic SVG (P&ID-style line motif, CSS-var colored)
SCHEMATIC = '''<div class="split-figure" aria-hidden="true">
  <div class="schematic">
    <svg viewBox="0 0 400 300" fill="none" stroke="var(--accent-2)" stroke-width="1.4">
      <rect x="40" y="60" width="70" height="46" rx="2" opacity=".9"/>
      <circle cx="220" cy="83" r="26" opacity=".9"/>
      <rect x="300" y="60" width="60" height="46" rx="2" opacity=".9"/>
      <rect x="150" y="200" width="120" height="40" rx="2" opacity=".7"/>
      <path d="M110 83 H194" stroke-dasharray="0"/>
      <path d="M246 83 H300"/>
      <path d="M75 106 V200 H150"/>
      <path d="M330 106 V220 H270"/>
      <circle cx="160" cy="83" r="3" fill="var(--accent-2)" stroke="none"/>
      <circle cx="273" cy="83" r="3" fill="var(--accent-2)" stroke="none"/>
      <path d="M205 120 v18 M220 120 v18 M235 120 v18" stroke-width="1" opacity=".5"/>
      <text x="46" y="50" font-family="monospace" font-size="9" fill="var(--muted-ink)" stroke="none">V-101</text>
      <text x="206" y="44" font-family="monospace" font-size="9" fill="var(--muted-ink)" stroke="none">R-201</text>
      <text x="306" y="50" font-family="monospace" font-size="9" fill="var(--muted-ink)" stroke="none">E-301</text>
      <text x="156" y="262" font-family="monospace" font-size="9" fill="var(--muted-ink)" stroke="none">SEP / CCUS PKG</text>
    </svg>
  </div>
</div>'''

# Standards block (used on several pages)
def standards_block():
    rows = [
        ("API", "American Petroleum Institute &mdash; relief, flare &amp; pressure systems"),
        ("ASME", "Pressure vessels, piping &amp; mechanical integrity codes"),
        ("ISO", "Quality, environmental &amp; process safety management"),
        ("IEC", "Instrumentation, control &amp; functional safety (SIL)"),
        ("NFPA", "Fire protection &amp; combustion safety engineering"),
    ]
    cells = "\n      ".join(
        f'<div class="std"><b>{a}</b><span>{b}</span></div>' for a, b in rows)
    return f'''<div class="standards reveal">
      {cells}
    </div>'''


# ============================ HOME ============================
home = f'''<main>
<section class="hero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">BNKM &middot; EST. 2024 &middot; LONDON, UK</p>
    <h1 class="reveal">Process engineering for hydrocarbons, chemicals &amp; the energy transition.</h1>
    <p class="lede reveal">{POSITIONING}</p>
    <div class="hero-actions reveal">
      <a class="btn btn--primary" href="services.html">Our services <span class="arr">&rarr;</span></a>
      <a class="btn btn--ghost" href="projects.html">View projects</a>
    </div>
    <div class="spec-row reveal" style="margin-top:2.4rem">
      <span class="spec">API</span><span class="spec">ASME</span><span class="spec">ISO</span>
      <span class="spec">IEC</span><span class="spec">NFPA</span>
    </div>
    <div class="hero-meta reveal">
      <div><b>19+</b><span>Years team experience</span></div>
      <div><b>4</b><span>Project phases supported</span></div>
      <div><b>5+</b><span>Industries served</span></div>
      <div><b>Global</b><span>Delivery footprint</span></div>
    </div>
  </div>
</section>

<section class="section blueprint-paper">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">[A.01] About BNKM</p>
      <h2>A specialist team delivering high-end process engineering.</h2>
      <div class="prose mt-2">
        <p>BNKM International Limited operates within engineering design activities for the industrial process and production industry. Incorporated in 2024 and headquartered in Wembley, London, our team brings more than 19 years of combined experience across the full process value chain.</p>
        <p>We deliver <strong>process optimization</strong>, <strong>dynamic simulation</strong>, <strong>energy efficiency</strong> and <strong>utility integration</strong> studies &mdash; from feasibility through FEED to detailed engineering &mdash; ensuring assets are designed, debottlenecked and operating optimally.</p>
      </div>
      <a class="btn btn--dark mt-3" href="about.html">More about us <span class="arr">&rarr;</span></a>
    </div>
    {FIG(REFINERY, "Oil and gas refinery at dusk with distillation columns, storage tanks and a flare stack")}
  </div>
</section>

<section class="section ink blueprint">
  <div class="wrap">
    <div class="shead reveal">
      <p class="eyebrow">[C.00] Capabilities</p>
      <h2>Engineering solutions across the energy value chain.</h2>
      <p class="lede">Specialist <strong>Process Engineering Consultancy</strong> spanning SAF, CCUS, ammonia, refining and upstream oil &amp; gas &mdash; grounded in recognised engineering standards and rigorous process modelling.</p>
    </div>
    <div class="grid grid-3">
      <article class="card reveal"><span class="idx">C.01 / SAF ENGINEERING</span><h3>Sustainable Aviation Fuel</h3><ul class="tick"><li>SAF process development</li><li>Gasification + Fischer-Tropsch</li><li>Biomass-to-green-fuels conversion</li></ul></article>
      <article class="card reveal"><span class="idx">C.02 / CCUS CONSULTANCY</span><h3>Carbon Capture &amp; Storage</h3><ul class="tick"><li>CO&#8322; capture system design</li><li>Compression &amp; transport</li><li>CCUS &amp; utility integration</li></ul></article>
      <article class="card reveal"><span class="idx">C.03 / GREEN AMMONIA</span><h3>Ammonia &amp; Fertilizers</h3><ul class="tick"><li>Green and grey ammonia</li><li>Urea &amp; fertilizer design</li><li>Process optimization</li></ul></article>
      <article class="card reveal"><span class="idx">C.04 / REFINERY SERVICES</span><h3>Petrochemicals &amp; Refining</h3><ul class="tick"><li>Process design &amp; simulation</li><li>Refinery engineering services</li><li>Troubleshooting &amp; debottlenecking</li></ul></article>
      <article class="card reveal"><span class="idx">C.05 / UPSTREAM</span><h3>Upstream Oil &amp; Gas</h3><ul class="tick"><li>Gas processing</li><li>Flare &amp; safety systems</li><li>Operational support</li></ul></article>
      <article class="card reveal"><span class="idx">C.06 / SPECIALIST</span><h3>Specialist Engineering</h3><ul class="tick"><li>Steady-state &amp; dynamic simulation</li><li>Surge analysis studies</li><li>Technical safety engineering</li></ul></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shead reveal">
      <p class="eyebrow">[L.00] Project lifecycle</p>
      <h2>End-to-end support across every project phase.</h2>
    </div>
    <div class="flow ink" style="border-radius:8px;overflow:hidden">
      <div class="flow-step reveal"><span class="flow-num">PHASE 01</span><h4>Feasibility &amp; Concept</h4><ul class="tick"><li>Technology screening &amp; selection</li><li>Process simulation &amp; validation</li><li>Techno-economic evaluation</li></ul></div>
      <div class="flow-step reveal"><span class="flow-num">PHASE 02</span><h4>Pre-FEED</h4><ul class="tick"><li>Conceptual design development</li><li>Process modelling &amp; optimization</li><li>Design basis &amp; philosophy</li></ul></div>
      <div class="flow-step reveal"><span class="flow-num">PHASE 03</span><h4>FEED Engineering</h4><ul class="tick"><li>PFDs &amp; P&amp;IDs development</li><li>Equipment sizing &amp; calculations</li><li>HAZID, HAZOP, SIL, LOPA</li></ul></div>
      <div class="flow-step reveal"><span class="flow-num">PHASE 04</span><h4>Detailed Engineering</h4><ul class="tick"><li>Final design deliverables</li><li>Vendor coordination &amp; review</li><li>Commissioning &amp; start-up support</li></ul></div>
    </div>
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="shead reveal">
      <p class="eyebrow">[S.00] Standards &amp; compliance</p>
      <h2>Engineering grounded in recognised codes.</h2>
      <p class="lede">Every deliverable is developed against the international standards industrial clients rely on for safety, integrity and regulatory acceptance.</p>
    </div>
    {standards_block()}
  </div>
</section>

{BAND(OFFSHORE, "[V.00] Field to facility", "From upstream wellheads to offshore platforms and downstream refineries.")}

<section class="section">
  <div class="wrap">
    <div class="cta-band reveal" style="background:var(--ink);display:grid;grid-template-columns:1.3fr .7fr;gap:2rem;align-items:center">
      <div class="accent-bar"></div>
      <div>
        <p class="eyebrow" style="color:var(--amber)">[E.00] Sustainability</p>
        <h2 style="color:#fff">{SUSTAIN}</h2>
      </div>
      <div style="text-align:right"><a class="btn btn--primary" href="energy-transition.html">Energy transition <span class="arr">&rarr;</span></a></div>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <div class="stats reveal">
      <div class="stat"><b>19+</b><span>Years experience</span></div>
      <div class="stat"><b>4</b><span>Lifecycle phases</span></div>
      <div class="stat"><b>5+</b><span>Industries served</span></div>
      <div class="stat"><b>2024</b><span>Year established</span></div>
    </div>
  </div>
</section>
</main>'''

write("index.html",
      "BNKM International Ltd. — Process Engineering Consultancy | FEED, CCUS, SAF & Green Ammonia",
      "BNKM International is a process engineering consultancy specializing in hydrocarbons, chemicals, fertilizers and low-carbon energy transition. FEED engineering, CCUS consultancy, green ammonia, SAF and refinery engineering services to API, ASME, ISO, IEC and NFPA standards.",
      home)


# ============================ ABOUT ============================
about = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[A.00] About us</p>
    <h1 class="reveal">A specialist process &amp; project engineering consultancy.</h1>
    <p class="lede reveal">{POSITIONING}</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal prose">
      <p class="eyebrow">[A.01] Who we are</p>
      <h2>High-end process engineering, end to end.</h2>
      <p class="mt-2">BNKM International Limited operates within engineering design activities for the industrial process and production industry. Incorporated in 2024, the company is headquartered at 132 Waterview House, 12 Quay Walk, Wembley, London.</p>
      <p>BNKM specialises in process engineering solutions across a range of industries, drawing on a team with more than 19 years of combined experience. We focus on high-end process engineering services delivered by engineers with proven track records across every facet of the discipline &mdash; with a firm commitment to a sustainable future.</p>
      <p>Our specialists bring experience across green and grey ammonia, low-carbon energy, Sustainable Aviation Fuel, petrochemicals, oil &amp; gas, refining, and water and wastewater treatment &mdash; ensuring clients&rsquo; assets are designed, optimised and performing reliably.</p>
    </div>
    {FIG(OFFSHORE, "Offshore oil and gas platform with derrick, modules and a flare boom")}
  </div>
</section>

<section class="section ink blueprint">
  <div class="wrap">
    <div class="shead reveal">
      <p class="eyebrow">[A.02] How we work</p>
      <h2>Engineering rigour, applied across the value chain.</h2>
    </div>
    <div class="grid grid-3">
      <article class="card reveal"><span class="idx">A.02.1</span><h4>Process optimization</h4><p style="color:#C3D2DE">Heat &amp; material balance, debottlenecking and energy efficiency studies that improve throughput and reduce operating cost.</p></article>
      <article class="card reveal"><span class="idx">A.02.2</span><h4>Dynamic simulation</h4><p style="color:#C3D2DE">Steady-state and dynamic process models to validate design intent, control philosophy and transient behaviour.</p></article>
      <article class="card reveal"><span class="idx">A.02.3</span><h4>Utility integration</h4><p style="color:#C3D2DE">Steam, condensate, cooling water and fuel-gas systems integrated for reliability and minimum energy demand.</p></article>
      <article class="card reveal"><span class="idx">A.02.4</span><h4>Carbon reduction</h4><p style="color:#C3D2DE">Decarbonisation pathways, CCUS integration and low-carbon fuel routes that lower lifecycle emissions.</p></article>
      <article class="card reveal"><span class="idx">A.02.5</span><h4>Technical safety</h4><p style="color:#C3D2DE">HAZID, HAZOP, SIL and LOPA, flare and relief adequacy to API and NFPA fire-protection principles.</p></article>
      <article class="card reveal"><span class="idx">A.02.6</span><h4>Standards compliance</h4><p style="color:#C3D2DE">Deliverables developed against API, ASME, ISO and IEC codes for integrity and regulatory acceptance.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shead reveal">
      <p class="eyebrow">[A.03] Company record</p>
      <h2>Registered in England &amp; Wales.</h2>
    </div>
    <div class="grid grid-3 reveal">
      <div class="card"><span class="idx">REGISTRATION</span><h4>Company No. 15683113</h4><p>England &amp; Wales</p></div>
      <div class="card"><span class="idx">REGISTERED OFFICE</span><h4>Wembley, London</h4><p>132 Waterview House, 12 Quay Walk, HA0 1BE, United Kingdom</p></div>
      <div class="card"><span class="idx">SECTOR</span><h4>Process &amp; production</h4><p>Engineering design activities for the industrial process and production industry.</p></div>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar"></div>
    <h2>Discuss your next project with our engineers.</h2>
    <a class="btn btn--primary mt-3" href="contact.html">Get in touch <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("about.html",
      "About Us — BNKM International | Process Engineering Consultancy",
      "About BNKM International: a process engineering and project consultancy specializing in hydrocarbons, chemicals, fertilizers and low-carbon energy transition solutions, with 19+ years of combined team experience.",
      about)


# ============================ INDUSTRIES ============================
industries = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[I.00] Industries</p>
    <h1 class="reveal">Sectors we serve across the process value chain.</h1>
    <p class="lede reveal">From hydrocarbons and chemicals to fertilizers and low-carbon energy, we apply consistent engineering rigour, process optimization and recognised standards to every sector.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid-2">
      <article class="sector reveal"><span class="tag">CCUS Consultancy</span><h3>Carbon Capture, Utilisation &amp; Storage</h3><p>End-to-end engineering and advisory for CCUS projects &mdash; from capture-technology screening to compression, transport and permanent storage.</p><ul class="tick"><li>CO&#8322; capture system design &amp; optimization</li><li>Compression, transport &amp; storage solutions</li><li>Utility integration with existing facilities</li><li>Feasibility &amp; technical evaluation of decarbonisation pathways</li></ul></article>
      <article class="sector reveal"><span class="tag">Green Ammonia Engineering</span><h3>Ammonia, Fertilizers &amp; Chemicals</h3><p>Strong expertise across conventional and emerging process technologies for ammonia, urea and fertilizer complexes.</p><ul class="tick"><li>Green and grey ammonia production</li><li>Urea &amp; fertilizer process design</li><li>Process optimization &amp; debottlenecking</li><li>Technology evaluation &amp; selection</li></ul></article>
      <article class="sector reveal"><span class="tag">Refinery Engineering Services</span><h3>Oil &amp; Gas and Petrochemicals</h3><p>Engineering support across upstream oil &amp; gas and downstream petrochemical and refining facilities.</p><ul class="tick"><li>Process design &amp; dynamic simulation</li><li>Gas processing &amp; refining systems</li><li>Flare systems &amp; safety studies (API / NFPA)</li><li>Operational troubleshooting &amp; energy efficiency</li></ul></article>
      <article class="sector reveal"><span class="tag">SAF Engineering</span><h3>Sustainable Aviation Fuel</h3><p>Process development for biomass- and waste-derived sustainable aviation fuel via gasification and Fischer-Tropsch routes.</p><ul class="tick"><li>SAF process development &amp; integration</li><li>Gasification + Fischer-Tropsch design</li><li>Syngas treatment &amp; conditioning</li><li>Carbon reduction across the fuel pathway</li></ul></article>
      <article class="sector reveal"><span class="tag">Water Engineering</span><h3>Water &amp; Wastewater Treatment</h3><p>Treatment and utility systems engineered for reliability, reuse and reduced environmental impact.</p><ul class="tick"><li>Process &amp; utility water systems</li><li>Wastewater treatment design</li><li>Utility integration &amp; optimisation</li></ul></article>
      <article class="sector reveal"><span class="tag">Energy Transition</span><h3>Low-Carbon Energy</h3><p>Hydrogen, clean-fuel and decarbonisation projects supporting the global shift to sustainable energy.</p><ul class="tick"><li>Hydrogen &amp; clean-fuel technologies</li><li>Decarbonisation strategy &amp; roadmaps</li><li>Energy efficiency &amp; carbon reduction</li></ul></article>
    </div>
  </div>
</section>

{BAND(REFINERY, "[I.00b] Process facilities", "Engineering the assets at the heart of the hydrocarbon and chemical value chain.")}

<section class="section ink">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[I.01] Standards</p><h2>Common engineering codes across all sectors.</h2></div>
    {standards_block()}
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar"></div>
    <h2>Looking for sector-specific engineering support?</h2>
    <a class="btn btn--primary mt-3" href="services.html">Explore services <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("industries.html",
      "Industries — CCUS, Green Ammonia, Refining & SAF | BNKM International",
      "Industries served by BNKM International: CCUS consultancy, green ammonia engineering, refinery engineering services, SAF engineering, petrochemicals, oil & gas and water treatment.",
      industries)


# ============================ SERVICES ============================
services = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[SV.00] Services</p>
    <h1 class="reveal">Process Engineering Consultancy &amp; project delivery.</h1>
    <p class="lede reveal">Innovative, sustainable solutions in SAF, CCUS, green and grey ammonia, fertilizers, petrochemicals and upstream oil &amp; gas &mdash; with end-to-end support from feasibility studies through Pre-FEED and FEED engineering to detailed engineering solutions.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[SV.01] Lifecycle</p><h2>End-to-end support across every project phase.</h2><p class="lede">From initial concept screening through to construction and commissioning &mdash; with process optimization and energy efficiency embedded at each stage.</p></div>
    <div class="flow ink" style="border-radius:8px;overflow:hidden">
      <div class="flow-step reveal"><span class="flow-num">PHASE 01</span><h4>Feasibility &amp; Concept</h4><ul class="tick"><li>Technology screening &amp; selection</li><li>Process simulation &amp; validation</li><li>Techno-economic evaluation</li></ul></div>
      <div class="flow-step reveal"><span class="flow-num">PHASE 02</span><h4>Pre-FEED</h4><ul class="tick"><li>Conceptual design development</li><li>Process modelling &amp; optimization</li><li>Design basis &amp; philosophy</li></ul></div>
      <div class="flow-step reveal"><span class="flow-num">PHASE 03</span><h4>FEED Engineering</h4><ul class="tick"><li>PFDs &amp; P&amp;IDs development</li><li>Equipment sizing &amp; calculations</li><li>HAZID, HAZOP, SIL, LOPA</li></ul></div>
      <div class="flow-step reveal"><span class="flow-num">PHASE 04</span><h4>Detailed Engineering</h4><ul class="tick"><li>Final design deliverables</li><li>Vendor coordination &amp; review</li><li>Commissioning &amp; start-up support</li></ul></div>
    </div>
  </div>
</section>

<section class="section ink blueprint">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[SV.02] Specialist services</p><h2>Specialist engineering services.</h2></div>
    <div class="grid grid-2">
      <article class="card reveal"><span class="idx">SV.02.1</span><h3>Process Modelling &amp; Simulation</h3><ul class="tick"><li>Aspen HYSYS / Aspen Plus modelling</li><li>Heat &amp; material balance</li><li>Dynamic simulation &amp; optimization</li></ul></article>
      <article class="card reveal"><span class="idx">SV.02.2</span><h3>Flare &amp; Relief System Engineering</h3><ul class="tick"><li>Flare system design &amp; validation (API 520/521/537)</li><li>Flarenet modelling (LP, HP, acid gas)</li><li>PSV sizing &amp; relief-load analysis</li></ul></article>
      <article class="card reveal"><span class="idx">SV.02.3</span><h3>Utilities &amp; Offsites Engineering</h3><ul class="tick"><li>Steam &amp; condensate systems</li><li>Cooling water &amp; fuel-gas networks</li><li>Utility integration &amp; energy efficiency</li><li>Water &amp; wastewater treatment</li></ul></article>
      <article class="card reveal"><span class="idx">SV.02.4</span><h3>Pipeline &amp; Surge Analysis</h3><ul class="tick"><li>Steady-state &amp; transient modelling</li><li>Surge &amp; vibration analysis</li><li>Hydraulic optimisation</li></ul></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal prose">
      <p class="eyebrow">[SV.03] Sustainability</p>
      <h2>Sustainability &amp; energy transition.</h2>
      <p class="mt-2">We support clients transitioning to low-carbon operations through innovative, future-ready engineering. {SUSTAIN}</p>
      <ul class="tick mt-2" style="max-width:46ch">
        <li>SAF production (gasification + Fischer-Tropsch)</li>
        <li>CCUS systems design &amp; integration</li>
        <li>Hydrogen &amp; clean-fuel technologies</li>
        <li>Decarbonisation strategies &amp; carbon reduction</li>
        <li>Energy optimisation &amp; efficiency</li>
      </ul>
      <a class="btn btn--dark mt-3" href="energy-transition.html">Energy transition <span class="arr">&rarr;</span></a>
    </div>
    {FIG(ONSHORE, "Onshore oil field with pump jacks, a wellhead and a storage tank")}
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[SV.04] Why BNKM</p><h2>Five reasons clients choose BNKM.</h2></div>
    <div class="reasons reveal" style="background:var(--line-ink);border-color:var(--line-ink)">
      <div class="reason" style="background:var(--ink-2)"><b>01</b><p style="color:#fff">Highly experienced process engineering specialists</p></div>
      <div class="reason" style="background:var(--ink-2)"><b>02</b><p style="color:#fff">Strong focus on sustainability and innovation</p></div>
      <div class="reason" style="background:var(--ink-2)"><b>03</b><p style="color:#fff">Proven track record across diverse industries</p></div>
      <div class="reason" style="background:var(--ink-2)"><b>04</b><p style="color:#fff">Flexible and client-focused approach</p></div>
      <div class="reason" style="background:var(--ink-2)"><b>05</b><p style="color:#fff">End-to-end project support, concept to commissioning</p></div>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar"></div>
    <h2>Tell us about your process challenge.</h2>
    <a class="btn btn--primary mt-3" href="contact.html">Start a conversation <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("services.html",
      "Services — FEED Engineering, Process Modelling & Detailed Engineering | BNKM International",
      "Process engineering consultancy services from BNKM International: feasibility, Pre-FEED, FEED engineering and detailed engineering solutions, plus process modelling, flare & relief, utilities and surge analysis.",
      services)


# ============================ ENERGY TRANSITION ============================
energy = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal" style="color:var(--amber)">[ET.00] Energy transition</p>
    <h1 class="reveal">Engineering the shift to low-carbon energy.</h1>
    <p class="lede reveal">{SUSTAIN}</p>
    <div class="hero-actions reveal"><a class="btn btn--primary" href="contact.html">Discuss a project <span class="arr">&rarr;</span></a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[ET.01] Focus areas</p><h2>Decarbonisation across the value chain.</h2><p class="lede">We combine process optimization, dynamic simulation and carbon reduction to make low-carbon projects technically and economically viable.</p></div>
    <div class="grid grid-3">
      <article class="pillar reveal"><div class="ico">SAF</div><h4>Sustainable Aviation Fuel</h4><p>Biomass- and waste-derived SAF via gasification and Fischer-Tropsch, with syngas conditioning and full process integration.</p></article>
      <article class="pillar reveal"><div class="ico">CO&#8322;</div><h4>CCUS Consultancy</h4><p>CO&#8322; capture, compression, transport and storage &mdash; integrated with existing utilities to cut facility emissions.</p></article>
      <article class="pillar reveal"><div class="ico">NH&#8323;</div><h4>Green Ammonia</h4><p>Green and grey ammonia routes, electrolysis integration and energy-efficient synthesis for fertilizers and fuel.</p></article>
      <article class="pillar reveal"><div class="ico">H&#8322;</div><h4>Hydrogen &amp; Clean Fuels</h4><p>Hydrogen production, handling and clean-fuel technologies engineered to recognised safety standards.</p></article>
      <article class="pillar reveal"><div class="ico">&#8645;</div><h4>Utility Integration</h4><p>Steam, power and cooling systems integrated for maximum energy efficiency and minimum carbon intensity.</p></article>
      <article class="pillar reveal"><div class="ico">&#8595;</div><h4>Carbon Reduction</h4><p>Decarbonisation roadmaps, energy-efficiency audits and emissions-reduction strategies for industrial assets.</p></article>
    </div>
  </div>
</section>

<section class="section ink blueprint">
  <div class="wrap split">
    <div class="reveal prose">
      <p class="eyebrow" style="color:var(--amber)">[ET.02] Our approach</p>
      <h2 style="color:#fff">From roadmap to commissioned asset.</h2>
      <p class="mt-2" style="color:#C3D2DE">Energy-transition projects demand the same engineering discipline as conventional process facilities &mdash; and more integration. We model emerging technologies with steady-state and dynamic simulation, validate them against API, ASME, ISO, IEC and NFPA requirements, and carry them from feasibility through FEED to detailed engineering.</p>
      <p style="color:#C3D2DE">The result is decarbonisation that stands up to technical, safety and economic scrutiny &mdash; supporting industrial decarbonization and sustainable energy transition projects globally.</p>
    </div>
    {SCHEMATIC}
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar" style="background:var(--amber)"></div>
    <h2>Planning a decarbonisation project?</h2>
    <a class="btn btn--primary mt-3" href="contact.html">Talk to our team <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("energy-transition.html",
      "Energy Transition — CCUS, SAF, Green Ammonia & Hydrogen | BNKM International",
      "BNKM International engineers the low-carbon energy transition: CCUS consultancy, SAF engineering, green ammonia, hydrogen and carbon reduction. Supporting industrial decarbonization and sustainable energy transition projects globally.",
      energy)


# ============================ PROJECTS ============================
projects = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[P.00] Projects</p>
    <h1 class="reveal">Complex projects across industries and phases.</h1>
    <p class="lede reveal">BNKM leadership brings extensive global experience delivering complex greenfield and brownfield projects &mdash; from concept and FEED engineering through to EPC and detailed engineering solutions.</p>
  </div>
</section>

{BAND(ONSHORE, "[P.00b] Upstream to downstream", "Delivery across greenfield and brownfield assets, concept to commissioning.")}

<section class="section">
  <div class="wrap">
    <div class="grid grid-2">
      <article class="proj reveal"><span class="proj-phase">FEED Phase</span><h3>SAF &mdash; Biomass Green Fuels</h3><span class="loc">United Kingdom &amp; Netherlands</span><ul class="tick"><li>Biomass to Sustainable Aviation Fuel</li><li>Process design including syngas treatment and Fischer-Tropsch conversion</li></ul></article>
      <article class="proj reveal"><span class="proj-phase">FEED Phase</span><h3>Ammonia &amp; Urea Complex</h3><span class="loc">Iraq</span><ul class="tick"><li>2,300 MTPD ammonia + 4,000 MTPD urea plant</li><li>Process design, safety studies and technology integration</li></ul></article>
      <article class="proj reveal"><span class="proj-phase">FEED &amp; Detailed</span><h3>Upstream Oil &amp; Gas Projects</h3><span class="loc">Iraq</span><ul class="tick"><li>Oil, gas and produced-water systems design</li><li>Storage and utility systems engineering</li></ul></article>
      <article class="proj reveal"><span class="proj-phase">EPC &amp; FEED</span><h3>Flare System &amp; LNG Project</h3><span class="loc">Woodside, Australia &amp; ABADI, Indonesia</span><ul class="tick"><li>Full flare-network modelling and adequacy studies</li><li>Integration of new and existing LNG systems</li></ul></article>
      <article class="proj reveal"><span class="proj-phase">Feasibility</span><h3>Refinery Debottlenecking Study</h3><span class="loc">Glencore, South Africa</span><ul class="tick"><li>Steam, condensate and flare-system optimisation</li><li>Capacity-enhancement solutions</li></ul></article>
      <article class="proj reveal"><span class="proj-phase">EPC Phase</span><h3>Flare System &amp; LNG Project</h3><span class="loc">Woodside, Australia</span><ul class="tick"><li>Full flare-network modelling and adequacy studies</li><li>Integration of new and existing LNG systems</li></ul></article>
    </div>
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[P.01] Core strength</p><h2>Proven delivery, end to end.</h2></div>
    <div class="grid grid-3 reveal">
      <div class="card"><span class="idx">01</span><h4>Greenfield &amp; brownfield</h4><p style="color:#C3D2DE">New facilities and modifications to operating assets alike.</p></div>
      <div class="card"><span class="idx">02</span><h4>Concept to EPC</h4><p style="color:#C3D2DE">Full lifecycle coverage from feasibility through commissioning.</p></div>
      <div class="card"><span class="idx">03</span><h4>Complex systems &amp; safety</h4><p style="color:#C3D2DE">Process, flare and safety engineering on demanding scopes.</p></div>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar"></div>
    <h2>Have a project in the pipeline?</h2>
    <a class="btn btn--primary mt-3" href="contact.html">Discuss it with us <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("projects.html",
      "Projects — FEED, EPC & Detailed Engineering | BNKM International",
      "Selected projects from BNKM International across SAF, ammonia & urea, upstream oil & gas, LNG flare systems and refinery debottlenecking — spanning feasibility, FEED engineering, EPC and detailed engineering solutions.",
      projects)


# ============================ TECHNICAL EXPERTISE ============================
expertise = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[TX.00] Technical expertise</p>
    <h1 class="reveal">Deep process engineering capability.</h1>
    <p class="lede reveal">Specialist tools, methods and standards applied to process optimization, dynamic simulation, energy efficiency, utility integration and carbon reduction.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[TX.01] Disciplines</p><h2>Core engineering disciplines.</h2></div>
    <div class="grid grid-3">
      <article class="card reveal"><span class="idx">TX.01.1</span><h3>Process Simulation</h3><ul class="tick"><li>Aspen HYSYS &amp; Aspen Plus</li><li>Steady-state &amp; dynamic simulation</li><li>Heat &amp; material balance</li></ul></article>
      <article class="card reveal"><span class="idx">TX.01.2</span><h3>Flare &amp; Relief</h3><ul class="tick"><li>PSV sizing (API 520 / 521)</li><li>Flarenet network modelling</li><li>Relief-load &amp; adequacy studies</li></ul></article>
      <article class="card reveal"><span class="idx">TX.01.3</span><h3>Process Safety</h3><ul class="tick"><li>HAZID &amp; HAZOP facilitation</li><li>SIL classification &amp; LOPA</li><li>Functional safety to IEC 61511</li></ul></article>
      <article class="card reveal"><span class="idx">TX.01.4</span><h3>Hydraulics &amp; Surge</h3><ul class="tick"><li>Steady-state &amp; transient flow</li><li>Surge &amp; vibration analysis</li><li>Hydraulic optimisation</li></ul></article>
      <article class="card reveal"><span class="idx">TX.01.5</span><h3>Utilities &amp; Energy</h3><ul class="tick"><li>Steam, condensate &amp; cooling water</li><li>Utility integration &amp; pinch analysis</li><li>Energy efficiency improvement</li></ul></article>
      <article class="card reveal"><span class="idx">TX.01.6</span><h3>Decarbonisation</h3><ul class="tick"><li>CCUS integration</li><li>Carbon reduction roadmaps</li><li>Low-carbon fuel pathways</li></ul></article>
    </div>
  </div>
</section>

<section class="section ink">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[TX.02] Standards &amp; codes</p><h2>Engineering to recognised standards.</h2><p class="lede">We design and verify against the codes that underpin safety, mechanical integrity and regulatory acceptance.</p></div>
    {standards_block()}
    <div class="spec-row reveal" style="margin-top:2rem">
      <span class="spec">API 520 / 521</span><span class="spec">API 537</span><span class="spec">ASME VIII</span>
      <span class="spec">ASME B31.3</span><span class="spec">ISO 9001</span><span class="spec">ISO 14001</span>
      <span class="spec">IEC 61511</span><span class="spec">IEC 61508</span><span class="spec">NFPA 30</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal prose">
      <p class="eyebrow">[TX.03] Toolset</p>
      <h2>Methods &amp; software.</h2>
      <p class="mt-2">Our engineers apply industry-standard simulation and analysis tools &mdash; including Aspen HYSYS, Aspen Plus and Flarenet &mdash; alongside rigorous hand calculations and recognised design codes.</p>
      <p>Every study links analysis to deliverables: PFDs, P&amp;IDs, datasheets, equipment sizing, cause-and-effect matrices and safety reports that downstream EPC and detailed engineering teams can build on directly.</p>
    </div>
    {SCHEMATIC}
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar"></div>
    <h2>Need specialist analysis on your asset?</h2>
    <a class="btn btn--primary mt-3" href="contact.html">Request expertise <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("expertise.html",
      "Technical Expertise — Simulation, Flare, Safety & Standards | BNKM International",
      "BNKM International technical expertise: process simulation, flare & relief, process safety (HAZOP, SIL, LOPA), surge analysis, utilities and decarbonisation — engineered to API, ASME, ISO, IEC and NFPA standards.",
      expertise)


# ============================ CAREERS ============================
careers = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[CR.00] Careers</p>
    <h1 class="reveal">Engineer the energy transition with us.</h1>
    <p class="lede reveal">We are building a specialist team of process engineers who want to work on hydrocarbons, chemicals, fertilizers and low-carbon energy projects that matter.</p>
    <div class="hero-actions reveal"><a class="btn btn--primary" href="mailto:bnkm139@gmail.com?subject=Career%20enquiry%20%E2%80%94%20BNKM%20International">Send your CV <span class="arr">&rarr;</span></a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[CR.01] Why BNKM</p><h2>Where your engineering goes further.</h2></div>
    <div class="grid grid-3 reveal">
      <div class="card"><span class="idx">CR.01.1</span><h4>Meaningful projects</h4><p>From CCUS and SAF to ammonia and refining &mdash; work that supports industrial decarbonization worldwide.</p></div>
      <div class="card"><span class="idx">CR.01.2</span><h4>Full lifecycle exposure</h4><p>Feasibility, Pre-FEED, FEED and detailed engineering &mdash; develop breadth across every project phase.</p></div>
      <div class="card"><span class="idx">CR.01.3</span><h4>Standards-led practice</h4><p>Work to API, ASME, ISO, IEC and NFPA, mentored by engineers with proven global track records.</p></div>
    </div>
  </div>
</section>

<section class="section ink blueprint">
  <div class="wrap">
    <div class="shead reveal"><p class="eyebrow">[CR.02] Open roles</p><h2>Current &amp; ongoing opportunities.</h2><p class="lede">We welcome applications from experienced process engineers and graduates. Don&rsquo;t see an exact match? We review speculative applications continuously.</p></div>
    <div class="grid grid-2">
      <article class="role reveal"><div class="meta"><span class="pill">Process</span><span class="pill">FEED / Detailed</span><span class="pill">Hybrid &middot; UK</span></div><h3>Senior Process Engineer</h3><p style="color:#C3D2DE">Lead process design and dynamic simulation across SAF, CCUS and ammonia projects, from concept through FEED engineering to detailed engineering deliverables.</p><a class="btn btn--ghost mt-2" href="mailto:bnkm139@gmail.com?subject=Senior%20Process%20Engineer%20%E2%80%94%20Application">Apply <span class="arr">&rarr;</span></a></article>
      <article class="role reveal"><div class="meta"><span class="pill">Safety</span><span class="pill">Flare &amp; Relief</span><span class="pill">Hybrid &middot; UK</span></div><h3>Process Safety Engineer</h3><p style="color:#C3D2DE">Deliver HAZOP, SIL and LOPA studies and flare/relief adequacy to API and IEC standards across oil &amp; gas and petrochemical assets.</p><a class="btn btn--ghost mt-2" href="mailto:bnkm139@gmail.com?subject=Process%20Safety%20Engineer%20%E2%80%94%20Application">Apply <span class="arr">&rarr;</span></a></article>
      <article class="role reveal"><div class="meta"><span class="pill">Simulation</span><span class="pill">Aspen / Flarenet</span><span class="pill">Remote-friendly</span></div><h3>Simulation Engineer</h3><p style="color:#C3D2DE">Build steady-state and dynamic models in Aspen HYSYS / Plus to drive process optimization, utility integration and energy efficiency studies.</p><a class="btn btn--ghost mt-2" href="mailto:bnkm139@gmail.com?subject=Simulation%20Engineer%20%E2%80%94%20Application">Apply <span class="arr">&rarr;</span></a></article>
      <article class="role reveal"><div class="meta"><span class="pill">Graduate</span><span class="pill">Process</span><span class="pill">UK</span></div><h3>Graduate Process Engineer</h3><p style="color:#C3D2DE">Join a structured pathway across simulation, utilities and safety, supporting carbon-reduction and energy-transition projects from day one.</p><a class="btn btn--ghost mt-2" href="mailto:bnkm139@gmail.com?subject=Graduate%20Process%20Engineer%20%E2%80%94%20Application">Apply <span class="arr">&rarr;</span></a></article>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap"><div class="cta-band reveal"><div class="accent-bar"></div>
    <h2>Speculative applications always welcome.</h2>
    <p class="lede mt-1" style="color:#C3D2DE">Send your CV and a short note to our team and we&rsquo;ll be in touch.</p>
    <a class="btn btn--primary mt-3" href="mailto:bnkm139@gmail.com?subject=Speculative%20application%20%E2%80%94%20BNKM%20International">Email your CV <span class="arr">&rarr;</span></a>
  </div></div>
</section>
</main>'''

write("careers.html",
      "Careers — Process Engineering Jobs | BNKM International",
      "Careers at BNKM International: process engineering roles across FEED engineering, process safety, simulation and graduate pathways — working on CCUS, SAF, green ammonia and energy-transition projects.",
      careers)


# ============================ CONTACT ============================
contact = f'''<main>
<section class="phero ink blueprint">
  <div class="wrap">
    <p class="eyebrow reveal">[CT.00] Contact</p>
    <h1 class="reveal">Discuss your project with our team.</h1>
    <p class="lede reveal">For enquiries regarding our process engineering and project consultancy services, reach out using the details below or send a message.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="cinfo reveal">
      <div class="row"><span>Email</span><a href="mailto:bnkm139@gmail.com">bnkm139@gmail.com</a></div>
      <div class="row"><span>Phone</span><a href="tel:+447587481434">+44 7587 481434</a></div>
      <div class="row"><span>Registered office</span><p>132 Waterview House, 12 Quay Walk<br>Wembley, HA0 1BE, United Kingdom</p></div>
      <div class="row"><span>Company registration</span><p>No. 15683113 &mdash; England &amp; Wales</p></div>
      <hr class="divider" style="background:var(--line)">
      <div class="row"><span>Positioning</span><p style="font-size:.98rem;color:var(--body)">{POSITIONING}</p></div>
    </div>
    <div class="form reveal">
      <h3 style="margin-bottom:1.6rem">Send us a message</h3>
      <form data-contact-form novalidate>
        <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name"></div>
        <div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="company">Company</label><input id="company" name="company" type="text" autocomplete="organization"></div>
        <div class="field"><label for="message">Message *</label><textarea id="message" name="message" required></textarea></div>
        <button class="btn btn--primary" type="submit">Send message <span class="arr">&rarr;</span></button>
        <p data-form-note role="status" style="display:none;margin-top:1.2rem;font-size:.9rem;color:var(--accent-deep)"></p>
      </form>
    </div>
  </div>
</section>
</main>'''

write("contact.html",
      "Contact — BNKM International | Process Engineering Consultancy",
      "Contact BNKM International to discuss process engineering consultancy, FEED engineering, CCUS, green ammonia, SAF and refinery engineering services. Based in Wembley, London, delivering globally.",
      contact)

print("\\nAll pages built.")
