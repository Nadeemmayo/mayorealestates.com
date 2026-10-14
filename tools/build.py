# -*- coding: utf-8 -*-
"""Builds every page of mayorealestates.com from tools/content.py.
Run from the repo root:  python3 tools/build.py
Listings are NOT built here — they live in assets/js/listings.js and appear automatically."""
import json, os, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import SITE, SOCIETIES, CITIES, CATEGORIES, FAQS, POSTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "20261014"
DOMAIN = "https://" + SITE["domain"]
e = html.escape
TEL1 = SITE["phone1"].replace(" ", "")
TEL2 = SITE["phone2"].replace(" ", "")
WA = SITE["whatsapp"]

def img(pid, small=False):
    return "images/p/%s%s.jpg" % ("t/" if small else "", pid)

LOGO_SVG = """<svg viewBox="0 0 48 56" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><path d="M4 55V23C4 12 13 6 24 1c11 5 20 11 20 22v32z" fill="#0d2620" stroke="#b8935a" stroke-width="1.6"/><path d="M8.5 55V24.5C8.5 16 15 11 24 6.6 33 11 39.5 16 39.5 24.5V55" fill="none" stroke="#b8935a" stroke-width=".8" opacity=".55"/><path d="M13 45V28.5l11 8.6 11-8.6V45" fill="none" stroke="#d6bb88" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/><circle cx="24" cy="15" r="2" fill="#d6bb88"/><path d="M20.5 55v-6.5a3.5 3.5 0 0 1 7 0V55" fill="none" stroke="#d6bb88" stroke-width="1.6"/></svg>"""

def logo(href="index.html"):
    return '<a href="%s" class="logo" aria-label="Mayo Real Estates home">%s<span class="wm"><b>Mayo</b><small>REAL ESTATES</small></span></a>' % (href, LOGO_SVG)

def social(cls="social"):
    s = SITE["social"]
    return ('<div class="%s"><a href="%s" class="fb" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>'
            '<a href="%s" class="ig" target="_blank" rel="noopener" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>'
            '<a href="%s" class="tt" target="_blank" rel="noopener" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>'
            '<a href="https://wa.me/%s" class="wa" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a></div>') % (cls, s["facebook"], s["instagram"], s["tiktok"], WA)

PROP_MENU = [("houses-for-sale.html","fa-house","Houses"),("new-houses.html","fa-star","Brand-new houses"),("old-houses.html","fa-house-chimney","Old houses"),
             ("luxury-villas.html","fa-gem","Luxury villas"),("farmhouses.html","fa-tree","Farmhouses"),("plots.html","fa-map","Plots & land"),
             ("commercial-property.html","fa-shop","Shops & offices"),("apartments.html","fa-building","Apartments"),("properties.html","fa-list","All properties")]
CITY_MENU = [("property-in-%s.html" % c["slug"], "fa-location-dot", c["name"]) for c in CITIES] + [("societies.html","fa-city","All societies")]

def drop(items):
    return '<div class="drop">' + "".join('<a href="%s"><i class="fa-solid %s"></i>%s</a>' % (h, i, t) for h, i, t in items) + '</div>'

def header():
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <div class="links"><a href="https://wa.me/{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i>{SITE['phone1']}</a><a href="tel:{TEL2}" class="hide-sm"><i class="fa-solid fa-phone"></i>{SITE['phone2']}</a><a href="mailto:{SITE['email']}" class="hide-sm"><i class="fa-solid fa-envelope"></i>{SITE['email']}</a></div>
  {social("social")}
</div></div>
<header class="site-header"><div class="container nav">
  {logo()}
  <ul class="menu">
    <li><a href="index.html">Home</a></li>
    <li><a href="properties.html">Buy <i class="fa-solid fa-angle-down" style="font-size:.7em"></i></a>{drop(PROP_MENU)}</li>
    <li><a href="societies.html">Societies <i class="fa-solid fa-angle-down" style="font-size:.7em"></i></a>{drop([(s['slug']+'.html','fa-location-dot',s['name']) for s in SOCIETIES if s['city']=='Lahore'][:7]+[(s['slug']+'.html','fa-location-dot',s['name']) for s in SOCIETIES if s['city'] in ('Islamabad','Rawalpindi')][:4]+[('societies.html','fa-city','All societies')])}</li>
    <li><a href="property-in-lahore.html">Cities <i class="fa-solid fa-angle-down" style="font-size:.7em"></i></a>{drop(CITY_MENU)}</li>
    <li><a href="sell-property.html">Sell</a></li>
    <li><a href="services.html">Services</a></li>
    <li><a href="overseas-pakistanis.html">Overseas</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
  <div class="nav-cta"><a class="saved-link" href="properties.html?saved=1" aria-label="Your shortlist"><i class="fa-regular fa-heart"></i><span class="saved-count" style="display:none">0</span></a><a class="btn btn-brass" href="sell-property.html">List your property</a></div>
  <button class="burger" data-open-drawer aria-label="Open menu" aria-expanded="false"><i class="fa-solid fa-bars"></i></button>
</div></header>
<div class="drawer" id="drawer"><div class="shade"></div><nav class="panel" aria-label="Mobile menu"><button class="close" aria-label="Close menu"><i class="fa-solid fa-xmark"></i></button>
  {logo()}
  <h4>Buy</h4>{''.join('<a href="%s"><i class="fa-solid %s"></i>%s</a>' % x for x in PROP_MENU)}
  <h4>Cities</h4>{''.join('<a href="%s"><i class="fa-solid %s"></i>%s</a>' % x for x in CITY_MENU)}
  <h4>More</h4><a href="sell-property.html"><i class="fa-solid fa-tag"></i>Sell your property</a><a href="services.html"><i class="fa-solid fa-briefcase"></i>Services</a><a href="overseas-pakistanis.html"><i class="fa-solid fa-plane"></i>Overseas Pakistanis</a><a href="calculators.html"><i class="fa-solid fa-calculator"></i>Calculators</a><a href="blog.html"><i class="fa-solid fa-newspaper"></i>Property guides</a><a href="about.html"><i class="fa-solid fa-user-tie"></i>About us</a><a href="contact.html"><i class="fa-solid fa-phone"></i>Contact</a>
  <div style="margin-top:20px">{social("social big")}</div>
</nav></div>"""

def footer():
    socs_l = "".join(['<li><a href="%s.html">%s</a></li>' % (s["slug"], e(s["name"])) for s in SOCIETIES if s["city"] == "Lahore"][:7])
    socs_i = "".join(['<li><a href="%s.html">%s</a></li>' % (s["slug"], e(s["name"])) for s in SOCIETIES if s["city"] in ("Islamabad","Rawalpindi")][:6])
    return f"""<footer class="site-footer"><div class="container">
<div class="f-grid">
  <div>{logo()}<p class="f-about">Houses, luxury villas, farmhouses, plots and commercial property across Lahore, Islamabad and Pakistan — checked, verified and shown by {SITE['owner']} personally.</p>{social("social big")}</div>
  <div><h4>Buy</h4><ul>{''.join('<li><a href="%s">%s</a></li>' % (h, t) for h, i, t in PROP_MENU)}</ul></div>
  <div><h4>Lahore</h4><ul>{socs_l}</ul></div>
  <div><h4>Islamabad</h4><ul>{socs_i}<li><a href="property-in-karachi.html">Karachi</a></li><li><a href="property-in-murree.html">Murree</a></li></ul></div>
  <div><h4>Contact</h4><ul class="f-contact">
    <li><i class="fa-brands fa-whatsapp"></i><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{SITE['phone1']}</a></li>
    <li><i class="fa-solid fa-phone"></i><a href="tel:{TEL2}">{SITE['phone2']}</a></li>
    <li><i class="fa-solid fa-envelope"></i><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
    <li><i class="fa-solid fa-location-dot"></i><span>{SITE['office']}, Pakistan</span></li>
  </ul><ul style="margin-top:14px"><li><a href="sell-property.html">Sell your property</a></li><li><a href="calculators.html">Calculators</a></li><li><a href="blog.html">Property guides</a></li><li><a href="faq.html">FAQs</a></li><li><a href="about.html">About us</a></li></ul></div>
</div>
<div class="f-bottom"><span>© <span class="year">2026</span> Mayo Real Estates. All rights reserved.</span><span><a href="privacy-policy.html">Privacy</a> &nbsp;·&nbsp; <a href="terms.html">Terms</a> &nbsp;·&nbsp; <a href="photo-credits.html">Photo credits</a></span></div>
</div></footer>
<a class="float-wa" href="https://wa.me/{WA}?text={'Assalam%20o%20Alaikum%2C%20I%20found%20you%20on%20mayorealestates.com'}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<div class="side-toggle"><button class="tab" aria-expanded="false" aria-label="Contact options">Contact us</button><div class="links"><a class="ph" href="tel:{TEL1}" aria-label="Call"><i class="fa-solid fa-phone"></i></a><a href="https://wa.me/{WA}" target="_blank" rel="noopener" style="background:#25d366" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a><a class="em" href="mailto:{SITE['email']}" aria-label="Email"><i class="fa-solid fa-envelope"></i></a><a href="{SITE['social']['facebook']}" style="background:#1877f2" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a><a href="{SITE['social']['instagram']}" style="background:#d6249f" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a><a href="{SITE['social']['tiktok']}" style="background:#000" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a></div></div>"""

ORG_LD = {"@context":"https://schema.org","@type":"RealEstateAgent","name":"Mayo Real Estates","url":DOMAIN,
          "logo":DOMAIN+"/assets/img/logo.svg","image":DOMAIN+"/images/p/31737860.jpg","telephone":SITE["phone1"],"email":SITE["email"],
          "founder":SITE["owner"],"address":{"@type":"PostalAddress","addressLocality":"Lahore","addressRegion":"Punjab","addressCountry":"PK"},
          "areaServed":["Lahore","Islamabad","Rawalpindi","Karachi","Murree"]}

def page(fname, title, desc, body, page_id="", og_img=31737860, ld=None, scripts=True, noindex=False):
    canon = DOMAIN + "/" + ("" if fname == "index.html" else fname)
    lds = '<script type="application/ld+json">%s</script>' % json.dumps(ld or ORG_LD, ensure_ascii=False)
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{'noindex, follow' if noindex else 'index, follow, max-image-preview:large'}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0d2620">
<meta property="og:type" content="website"><meta property="og:site_name" content="Mayo Real Estates">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/{img(og_img)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="PK-PB"><meta name="geo.placename" content="Lahore">
<link rel="icon" type="image/svg+xml" href="assets/img/logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Manrope:wght@400;500;600;700;800&family=Noto+Nastaliq+Urdu:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="assets/css/style.css?v={V}">
{lds}
</head>
<body data-page="{page_id}">
{header()}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/content.js?v={V}"></script>
<script src="assets/js/listings.js?v={V}"></script>
<script src="assets/js/app.js?v={V}"></script>
</body>
</html>
"""
    open(os.path.join(ROOT, fname), "w", encoding="utf-8").write(out)
    return fname

def page_hero(crumbs, h1, intro, photo):
    cr = '<a href="index.html">Home</a>' + "".join('<span>/</span>' + (('<a href="%s">%s</a>' % (h, e(t))) if h else e(t)) for h, t in crumbs)
    return f'<section class="page-hero" style="background-image:url({img(photo)})"><div class="container"><div class="crumbs">{cr}</div><h1>{e(h1)}</h1><p>{intro}</p></div></section>'

def listings_block(filt, limit=None):
    return "<div class=\"grid\" data-listings='%s'%s></div>" % (json.dumps(filt), (' data-limit="%d"' % limit) if limit else "")

def cta_band(photo=8143683, title="Looking for something specific?", text="Tell us your budget, area and size. We will send matching properties on WhatsApp — including off-market homes we don't advertise."):
    return f"""<section class="section tight"><div class="container"><div class="band" style="background-image:url({img(photo)})">
<h2>{title}</h2><p>{text}</p>
<div class="hero-ctas" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:18px"><a class="btn btn-wa" href="https://wa.me/{WA}?text=Assalam%20o%20Alaikum%2C%20my%20property%20requirement%20is%3A%20" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> Send your requirement</a><a class="btn btn-line" style="color:#fff" href="tel:{TEL1}"><i class="fa-solid fa-phone"></i> Call {SITE['phone1']}</a></div></div></div></section>"""

built = []
TODAY = datetime.date.today().isoformat()

# ---------------- HOME ----------------
cat_tiles = "".join(f'<a class="cat" href="{c["file"]}"><img src="{img(c["photo"],True)}" alt="{e(c["name"])}" loading="lazy"><div><b>{e(c["name"])}</b><span data-countf="{e(json.dumps(c["filt"]))}"></span></div></a>' for c in CATEGORIES)
arch_socs = "".join(f'<a class="arch" href="{s["slug"]}.html"><div class="frame"><img src="{img(s["photo"],True)}" alt="{e(s["name"])}" loading="lazy"></div><b>{e(s["name"])}</b><span>{s["city"]}</span></a>' for s in [x for x in SOCIETIES if x["slug"] in ("dha-lahore","bahria-town-lahore","gulberg-lahore","lake-city","e-7-islamabad","dha-islamabad","bedian-road","bahria-town-islamabad")])
city_arches = "".join(f'<a class="arch" href="property-in-{c["slug"]}.html"><div class="frame"><img src="{img(c["photo"],True)}" alt="{e(c["name"])}" loading="lazy"></div><b>{c["name"]}</b><span>{e(c["short"])}</span></a>' for c in CITIES[:4])
posts_cards = "".join(f'<a class="post-card" href="blog-{p["slug"]}.html"><img src="{img(p["photo"],True)}" alt="" loading="lazy"><div class="bd"><div class="meta">{datetime.date.fromisoformat(p["date"]).strftime("%d %B %Y")}</div><h3>{e(p["title"])}</h3><p>{e(p["excerpt"])}</p></div></a>' for p in POSTS[:3])
home = f"""
<section class="hero" style="background-image:url({img(31737860)})"><div class="container">
  <span class="urdu" lang="ur">آپ کا خواب، ہماری ذمہ داری</span>
  <h1>Homes worth coming home to</h1>
  <p class="lead">Luxury houses, villas, farmhouses, plots and commercial property in DHA, Bahria Town, Gulberg, E-7 and across Pakistan — every property visited and every document checked by Wakeel Mayo before it reaches you.</p>
  <div class="hero-ctas"><a class="btn btn-brass" href="properties.html">Browse properties</a><a class="btn btn-line" href="https://wa.me/{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> WhatsApp {SITE['phone1']}</a></div>
</div></section>
<div class="search-dock"><div class="container"><form class="search-card" id="homeSearch" role="search" aria-label="Search properties">
  <div class="search-tabs" role="tablist">
    <button type="button" class="on" data-type="house" role="tab" aria-selected="true">Houses</button><button type="button" data-type="villa" role="tab" aria-selected="false">Luxury villas</button><button type="button" data-type="farmhouse" role="tab" aria-selected="false">Farmhouses</button><button type="button" data-type="plot" role="tab" aria-selected="false">Plots</button><button type="button" data-type="commercial" role="tab" aria-selected="false">Commercial</button><button type="button" data-type="apartment" role="tab" aria-selected="false">Apartments</button>
  </div>
  <div class="search-fields">
    <div class="field"><label for="hsCity">City</label><select id="hsCity" name="city"><option value="">All cities</option>{''.join('<option>%s</option>' % c['name'] for c in CITIES)}</select></div>
    <div class="field"><label for="hsSoc">Society / area</label><select id="hsSoc" name="society"></select></div>
    <div class="field"><label for="hsMax">Max budget</label><select id="hsMax" name="max"><option value="">Any budget</option><option value="20000000">2 Crore</option><option value="40000000">4 Crore</option><option value="60000000">6 Crore</option><option value="100000000">10 Crore</option><option value="200000000">20 Crore</option><option value="500000000">50 Crore</option></select></div>
    <div class="field"><label for="hsBeds">Bedrooms</label><select id="hsBeds" name="beds"><option value="">Any</option><option value="2">2+</option><option value="3">3+</option><option value="4">4+</option><option value="5">5+</option></select></div>
    <button class="btn btn-ink" type="submit"><i class="fa-solid fa-magnifying-glass"></i> Search</button>
  </div>
</form></div></div>

<section class="section"><div class="container">
  <div class="sec-head"><div><h2>What are you looking for?</h2><p>From a 5 marla first home to an 8 kanal farmhouse with a pool.</p></div><a class="more" href="properties.html">All properties</a></div>
  <div class="cats">{cat_tiles}</div>
</div></section>

<section class="section white"><div class="container">
  <div class="sec-head"><div><h2>Featured properties</h2><p>Hand-picked homes we have personally visited this month.</p></div><a class="more" href="properties.html">See all</a></div>
  {listings_block({"featured":True}, 9)}
</div></section>

<section class="section dark"><div class="container">
  <div class="sec-head"><div><h2>The societies we know street by street</h2><p>Prices, blocks, bylaws and the people who matter in each one.</p></div><a class="more" href="societies.html">All societies</a></div>
  <div class="arches">{arch_socs}</div>
</div></section>

<section class="section"><div class="container split">
  <div class="pics"><img src="{img(28054875)}" alt="Farmhouse swimming pool and lawn" loading="lazy"><img src="{img(26859048,True)}" alt="Luxury villa pool at night" loading="lazy"><img src="{img(33529500,True)}" alt="Luxury villa living room" loading="lazy"></div>
  <div><h2>Farmhouses and pool villas, shown in person</h2><p class="lede">Bedian Road, Chak Shahzad, Gulberg Greens and Lake City — weekend estates with pools, event lawns and orchards.</p>
  <ul class="ticks"><li>Boundary, fard and registry checked before any token</li><li>Water, electricity and road access confirmed on site</li><li>Day visits arranged — see three or four estates in one trip</li><li>Video tours for overseas buyers</li></ul>
  <a class="btn btn-ink" href="farmhouses.html">View farmhouses</a> <a class="btn btn-line" href="luxury-villas.html">Luxury villas</a></div>
</div></section>

<section class="section white"><div class="container">
  <div class="sec-head"><div><h2>Houses, plots and new homes</h2><p>Brand-new builds, older homes on big plots and possession plots ready for construction.</p></div><a class="more" href="houses-for-sale.html">All houses</a></div>
  {listings_block({"type":"house"}, 6)}
  <div class="sec-head mt"><div><h3>Plots and commercial</h3></div></div>
  {listings_block({"type":"plot"}, 3)}
</div></section>

<section class="section dark"><div class="container">
  <div class="sec-head"><div><h2>How buying with us works</h2><p>Four steps, one person accountable from the first call to the transfer.</p></div></div>
  <div class="steps">
    <div class="step"><h3>Tell us what you need</h3><p>Budget, city, society and size — on WhatsApp or a call. We reply the same day.</p></div>
    <div class="step"><h3>Visit with Wakeel Mayo</h3><p>We shortlist and show you each property in person, or by live video if you are abroad.</p></div>
    <div class="step"><h3>Documents checked</h3><p>Title, dues and transfer record are verified before you pay any token money.</p></div>
    <div class="step"><h3>Transfer and keys</h3><p>We stay with you at the society or registry office until the transfer is in your name.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="sec-head"><div><h2>Property in every major city</h2><p>Lahore is home; Islamabad, Rawalpindi, Karachi and Murree through trusted partners.</p></div></div>
  <div class="arches">{city_arches}</div>
</div></section>

<section class="section white"><div class="container split">
  <div><h2>Marla, kanal or square feet?</h2><p class="lede">Societies use different marla sizes. Convert any area in one step before you compare prices.</p>
  <a class="btn btn-ink" href="calculators.html">All calculators</a></div>
  <div class="tool" id="converter"><div class="tool-row"><div class="field"><label for="cvVal">Area</label><input id="cvVal" type="number" value="10" min="0" step="any"></div>
  <div class="field"><label for="cvUnit">Unit</label><select id="cvUnit"><option value="marla">Marla</option><option value="kanal">Kanal</option><option value="sqft">Square feet</option><option value="sqyd">Square yards</option><option value="acre">Acre</option><option value="sqm">Square metres</option></select></div>
  <div class="field"><label for="cvMarla">1 marla =</label><select id="cvMarla"><option value="225">225 sq ft (DHA, Bahria)</option><option value="272.25">272.25 sq ft (revenue)</option><option value="250">250 sq ft</option></select></div></div>
  <div class="out" id="cvOut"></div></div>
</div></section>

<section class="section"><div class="container">
  <div class="sec-head"><div><h2>Property guides</h2><p>Plain-language advice before you buy.</p></div><a class="more" href="blog.html">All guides</a></div>
  <div class="grid">{posts_cards}</div>
</div></section>
{cta_band(31737859, "Selling a house, plot or farmhouse?", "We photograph it properly, list it here and on our social pages, and bring you serious buyers only.")}
"""
built.append(page("index.html", "Mayo Real Estates — Luxury Houses, Villas, Farmhouses & Plots for Sale in Lahore & Islamabad",
     "Buy houses, luxury villas, farmhouses, plots and commercial property in DHA, Bahria Town, Gulberg, Lake City, E-7 and across Pakistan. Verified listings by Wakeel Mayo. WhatsApp +92 347 4209912.",
     home, "home"))

# ---------------- ALL PROPERTIES ----------------
filters_html = f"""<form class="filters" id="filters" aria-label="Filter properties">
<h3>Filters <button type="button" id="resetFilters">Clear all</button></h3>
<div class="field"><label for="fq">Keyword</label><input id="fq" name="q" type="search" placeholder="e.g. pool, corner, Phase 6"></div>
<div class="field"><label for="ft">Property type</label><select id="ft" name="type"><option value="">All types</option><option value="house">Houses & villas</option><option value="villa">Luxury villas only</option><option value="farmhouse">Farmhouses</option><option value="plot">Plots & land</option><option value="commercial">Commercial</option><option value="apartment">Apartments</option></select></div>
<div class="field"><label for="fc">City</label><select id="fc" name="city"><option value="">All cities</option>{''.join('<option>%s</option>' % c['name'] for c in CITIES)}</select></div>
<div class="field"><label for="fs">Society / area</label><select id="fs" name="society"></select></div>
<div class="field"><label for="fcond">Condition</label><select id="fcond" name="condition"><option value="">Any</option><option value="new">Brand new</option><option value="old">Old house</option></select></div>
<div class="two"><div class="field"><label for="fmin">Min price</label><select id="fmin" name="min"><option value="">No min</option><option value="5000000">50 Lakh</option><option value="10000000">1 Crore</option><option value="20000000">2 Crore</option><option value="50000000">5 Crore</option><option value="100000000">10 Crore</option><option value="200000000">20 Crore</option></select></div>
<div class="field"><label for="fmax">Max price</label><select id="fmax" name="max"><option value="">No max</option><option value="10000000">1 Crore</option><option value="20000000">2 Crore</option><option value="40000000">4 Crore</option><option value="60000000">6 Crore</option><option value="100000000">10 Crore</option><option value="200000000">20 Crore</option><option value="500000000">50 Crore</option></select></div></div>
<div class="two"><div class="field"><label for="fb">Bedrooms</label><select id="fb" name="beds"><option value="">Any</option><option value="2">2+</option><option value="3">3+</option><option value="4">4+</option><option value="5">5+</option><option value="6">6+</option></select></div>
<div class="field"><label for="fa">Min size</label><select id="fa" name="minArea"><option value="">Any</option><option value="5">5 Marla</option><option value="10">10 Marla</option><option value="20">1 Kanal</option><option value="40">2 Kanal</option><option value="80">4 Kanal</option></select></div></div>
<button class="btn btn-ink btn-block" type="submit">Show properties</button>
</form>"""
plist = f"""{page_hero([(None,"Properties")], "Properties for sale", "Houses, villas, farmhouses, plots, apartments and commercial property — filter by city, society, budget and size.", 8143668)}
<section class="section tight"><div class="container list-layout">
  <div>{filters_html}</div>
  <div><div class="toolbar"><div><h2 id="resultsTitle" style="font-size:1.6rem;margin:0">All properties</h2><span class="n"><b id="count">0</b> properties found</span></div>
  <div style="display:flex;gap:8px;align-items:end"><button class="btn btn-line btn-sm filter-toggle" id="filterToggle" type="button"><i class="fa-solid fa-sliders"></i> Filters</button><div class="field"><label for="sort">Sort by</label><select id="sort"><option value="">Featured first</option><option value="price-asc">Price: low to high</option><option value="price-desc">Price: high to low</option><option value="size-desc">Size: largest first</option></select></div></div></div>
  <div class="grid" id="results" style="grid-template-columns:repeat(auto-fill,minmax(270px,1fr))"></div></div>
</div></section>{cta_band()}"""
built.append(page("properties.html", "Properties for Sale in Lahore, Islamabad & Pakistan | Mayo Real Estates",
     "Search houses, luxury villas, farmhouses, plots, apartments and commercial property for sale. Filter by city, society, budget and size.", plist, "properties"))

# ---------------- PROPERTY DETAIL ----------------
built.append(page("property.html", "Property details | Mayo Real Estates", "Property for sale with Mayo Real Estates — photos, price, features and location.",
     '<section class="section tight"><div class="container" id="propertyDetail"><p class="muted">Loading property…</p></div></section>', "property"))

# ---------------- CATEGORY PAGES ----------------
for c in CATEGORIES:
    others = "".join('<a class="chip" href="%s">%s</a>' % (x["file"], e(x["name"])) for x in CATEGORIES if x is not c)
    body = f"""{page_hero([("properties.html","Properties"),(None,c["name"])], c["h1"], c["intro"], c["photo"])}
<section class="section tight"><div class="container"><div class="chips" style="margin-bottom:26px">{others}</div>
{listings_block(c["filt"])}
<p class="mt"><a class="btn btn-ink" href="properties.html?{'&'.join('%s=%s' % (k, v) for k, v in c['filt'].items() if k!='luxury')}"><i class="fa-solid fa-sliders"></i> Filter by city, budget & size</a></p>
</div></section>{cta_band()}"""
    built.append(page(c["file"], c["h1"] + " | Mayo Real Estates", c["intro"] + " Verified listings — WhatsApp " + SITE["phone1"] + ".", body, "category", c["photo"]))

# ---------------- SOCIETIES ----------------
groups = {}
for s in SOCIETIES: groups.setdefault(s["city"], []).append(s)
soc_sections = ""
for city, lst in groups.items():
    soc_sections += f'<div class="sec-head mt"><h2>{city}</h2></div><div class="arches">' + "".join(f'<a class="arch" href="{s["slug"]}.html"><div class="frame"><img src="{img(s["photo"],True)}" alt="{e(s["name"])}" loading="lazy"></div><b>{e(s["name"])}</b><span>{e(s["short"])}</span></a>' for s in lst) + "</div>"
built.append(page("societies.html", "Housing Societies in Lahore, Islamabad & Karachi | Mayo Real Estates",
    "Guides and property for sale in DHA, Bahria Town, Gulberg, Model Town, Lake City, E-7, F-7, Gulberg Greens, Chak Shahzad and more.",
    page_hero([(None,"Societies")], "Societies & areas we deal in", "Each guide covers what the area is like and every property we currently have there.", 7045711) +
    f'<section class="section tight"><div class="container">{soc_sections}</div></section>' + cta_band(), "societies"))

for s in SOCIETIES:
    near = "".join('<a class="chip" href="%s.html">%s</a>' % (x["slug"], e(x["name"])) for x in SOCIETIES if x["city"] == s["city"] and x is not s)
    body = f"""{page_hero([("societies.html","Societies"),("property-in-%s.html" % s['city'].lower(), s['city']),(None,s["name"])], "Property for sale in " + s["name"], e(s["short"]), s["photo"])}
<section class="section tight"><div class="container split" style="align-items:start">
  <div class="prose">{''.join('<p>%s</p>' % e(p) for p in s["about"])}</div>
  <div class="box"><h2>At a glance</h2><ul class="ticks">{''.join('<li>%s</li>' % e(p) for p in s["points"])}</ul>
  <a class="btn btn-wa btn-block" target="_blank" rel="noopener" href="https://wa.me/{WA}?text={'Assalam o Alaikum, I am looking for property in '.replace(' ','%20')}{e(s['name']).replace(' ','%20')}"><i class="fa-brands fa-whatsapp"></i> Ask about {e(s["name"])}</a></div>
</div></section>
<section class="section white"><div class="container"><div class="sec-head"><h2>Available in {e(s["name"])}</h2><a class="more" href="properties.html?society={s['slug']}">Filter these</a></div>
{listings_block({"society": s["slug"]})}
<div class="sec-head mt"><h3>Nearby areas in {s["city"]}</h3></div><div class="chips">{near}</div></div></section>{cta_band()}"""
    built.append(page(s["slug"] + ".html", "Property for Sale in %s, %s — Houses, Plots & Villas | Mayo Real Estates" % (s["name"], s["city"]),
        "%s Houses, villas, plots and commercial property for sale in %s, verified by Mayo Real Estates." % (s["short"], s["name"]), body, "society", s["photo"]))

# ---------------- CITIES ----------------
for c in CITIES:
    socs = [s for s in SOCIETIES if s["city"] == c["name"] or (c["name"] == "Islamabad" and s["city"] == "Rawalpindi") or (c["name"] == "Rawalpindi" and s["slug"] in ("dha-islamabad","bahria-town-islamabad"))]
    arch = "".join(f'<a class="arch" href="{s["slug"]}.html"><div class="frame"><img src="{img(s["photo"],True)}" alt="{e(s["name"])}" loading="lazy"></div><b>{e(s["name"])}</b><span>{e(s["short"][:70])}</span></a>' for s in socs)
    body = f"""{page_hero([("properties.html","Properties"),(None,c["name"])], c["title"], e(c["intro"]), c["photo"])}
<section class="section tight"><div class="container split" style="align-items:start"><div class="prose">{''.join('<p>%s</p>' % e(p) for p in c["about"])}</div><img src="{img(c['photo2'])}" alt="{c['name']}" style="border-radius:14px;aspect-ratio:4/3;object-fit:cover;width:100%" loading="lazy"></div></section>
<section class="section white"><div class="container"><div class="sec-head"><h2>Properties in {c["name"]}</h2><a class="more" href="properties.html?city={c['name']}">Filter</a></div>{listings_block({"city": c["name"]})}</div></section>
<section class="section"><div class="container"><div class="sec-head"><h2>Areas in {c["name"]}</h2></div><div class="arches">{arch}</div></div></section>{cta_band()}"""
    built.append(page("property-in-%s.html" % c["slug"], c["title"] + " — Houses, Villas, Plots | Mayo Real Estates", c["intro"], body, "city", c["photo"]))

# ---------------- SELL ----------------
sell = f"""{page_hero([(None,"Sell your property")], "Sell your property with Mayo Real Estates", "House, plot, farmhouse, villa, shop or apartment — fill in the details and they come straight to our WhatsApp.", 7031607)}
<section class="section tight"><div class="container split" style="align-items:start">
<form class="box" data-wa="Assalam o Alaikum, I want to SELL my property:">
  <h2>Property details</h2>
  <div class="form-grid">
    <div class="field"><label for="s1">Your name</label><input id="s1" name="name" data-label="Name" required></div>
    <div class="field"><label for="s2">Phone / WhatsApp</label><input id="s2" name="phone" data-label="Phone" type="tel" required></div>
    <div class="field"><label for="s3">Property type</label><select id="s3" name="type" data-label="Type"><option>House</option><option>Luxury villa</option><option>Farmhouse</option><option>Plot</option><option>Shop / office</option><option>Commercial building</option><option>Apartment</option></select></div>
    <div class="field"><label for="s4">Condition</label><select id="s4" name="condition" data-label="Condition"><option>Brand new</option><option>Old / used</option><option>Grey structure</option><option>Not applicable (plot)</option></select></div>
    <div class="field"><label for="s5">City</label><select id="s5" name="city" data-label="City">{''.join('<option>%s</option>' % c['name'] for c in CITIES)}<option>Other</option></select></div>
    <div class="field"><label for="s6">Society / area & block</label><input id="s6" name="area" data-label="Location" required placeholder="e.g. DHA Phase 6, Block D"></div>
    <div class="field"><label for="s7">Size</label><input id="s7" name="size" data-label="Size" placeholder="e.g. 1 kanal, 10 marla"></div>
    <div class="field"><label for="s8">Demand (PKR)</label><input id="s8" name="demand" data-label="Demand" placeholder="e.g. 9.5 crore"></div>
    <div class="field"><label for="s9">Bedrooms</label><input id="s9" name="beds" data-label="Bedrooms" type="number" min="0"></div>
    <div class="field"><label for="s10">Documents</label><select id="s10" name="docs" data-label="Documents"><option>Registry / transfer complete</option><option>File / allotment</option><option>Fard & intiqal</option><option>Not sure</option></select></div>
    <div class="field full"><label for="s11">Anything else</label><textarea id="s11" name="notes" data-label="Notes" placeholder="Corner, park facing, furnished, pool, etc."></textarea></div>
  </div>
  <p class="note">After you send, attach photos and a short video in the same WhatsApp chat.</p>
  <button class="btn btn-wa btn-block" type="submit"><i class="fa-brands fa-whatsapp"></i> Send to WhatsApp</button>
</form>
<div><h2>Why owners list with us</h2><ul class="ticks"><li>Professional photos and video of your property</li><li>Listed on this website and promoted on Facebook, Instagram and TikTok</li><li>Only serious, pre-qualified buyers visit</li><li>We negotiate for the best price</li><li>Help with NDC, transfer and registry</li><li>Your number is never published</li></ul>
<img src="{img(18285958)}" alt="Classic living room" style="border-radius:14px;margin-top:20px" loading="lazy"></div>
</div></section>"""
built.append(page("sell-property.html", "Sell Your Property in Lahore & Islamabad | Mayo Real Estates", "List your house, plot, farmhouse, villa or shop with Mayo Real Estates. Professional photos, serious buyers and full transfer support.", sell, "sell", 7031607))

# ---------------- SERVICES ----------------
svc = [("fa-house","Buying property","We shortlist, show and negotiate — houses, villas, farmhouses, plots and commercial."),
       ("fa-tag","Selling property","Photos, video, marketing and serious buyers. You stay in control of the price."),
       ("fa-file-shield","Document verification","Fard, registry, intiqal, society transfer record and dues checked before any payment."),
       ("fa-chart-line","Investment advice","Which society, which block and which size — based on current demand, not hype."),
       ("fa-plane","Overseas Pakistanis","Video tours, document copies and power-of-attorney transfers while you are abroad."),
       ("fa-key","Rental & management","Find tenants, collect rent and look after your property while you are away."),
       ("fa-trowel-bricks","Construction guidance","Introductions to trusted architects and builders, and help with map approval."),
       ("fa-building-columns","Home finance help","Introductions to banks offering home finance, and the paperwork they ask for."),
       ("fa-tree","Farmhouse land","Find, demarcate and buy land for your own custom farmhouse.")]
services = f"""{page_hero([(None,"Services")], "Everything between your first call and your keys", "One accountable person for the whole deal — buying, selling, verification and transfer.", 8135492)}
<section class="section tight"><div class="container"><div class="tiles">{''.join('<div class="tile"><i class="fa-solid %s"></i><h3>%s</h3><p>%s</p></div>' % x for x in svc)}</div></div></section>
<section class="section dark"><div class="container"><div class="sec-head"><div><h2>How a purchase works</h2></div></div><div class="steps">
<div class="step"><h3>Requirement</h3><p>Budget, area, size and timeline.</p></div><div class="step"><h3>Shortlist & visits</h3><p>In person or on live video.</p></div><div class="step"><h3>Verification & token</h3><p>Documents checked first, then token with a written agreement.</p></div><div class="step"><h3>Transfer</h3><p>Final payment and transfer at the society or registry office.</p></div></div></div></section>{cta_band()}"""
built.append(page("services.html", "Real Estate Services — Buy, Sell, Verify, Transfer | Mayo Real Estates", "Property buying, selling, document verification, investment advice and overseas Pakistani services in Lahore and Islamabad.", services, "services", 8135492))

# ---------------- OVERSEAS ----------------
overseas = f"""{page_hero([(None,"Overseas Pakistanis")], "Buying a home in Pakistan from abroad", "Live video tours, verified documents and transfers through your trusted family member — without flying home.", 31737859)}
<section class="section tight"><div class="container split" style="align-items:start"><div class="prose">
<h2>How we help you</h2><ol><li><b>Video call viewings</b> — we walk through each property live on WhatsApp video at a time that suits your time zone.</li><li><b>Document copies</b> — you receive copies of the title documents and our verification notes.</li><li><b>Power of attorney</b> — the transfer can be completed by a family member holding a registered special power of attorney, attested at the Pakistani embassy or consulate.</li><li><b>Banking channels</b> — payments go through proper banking channels so you keep a clear record.</li><li><b>After purchase</b> — we can find tenants, collect rent and look after the property.</li></ol>
<p>Read our guide: <a href="blog-overseas-pakistanis-buying-property.html">How overseas Pakistanis can buy property safely</a>.</p></div>
<div class="box"><h2>Book a video viewing</h2><form data-wa="Assalam o Alaikum, I live abroad and want a VIDEO VIEWING:"><div class="field" style="margin-bottom:10px"><label for="o1">Name</label><input id="o1" name="name" data-label="Name" required></div><div class="field" style="margin-bottom:10px"><label for="o2">Country you live in</label><input id="o2" name="country" data-label="Country" required></div><div class="field" style="margin-bottom:10px"><label for="o3">What are you looking for?</label><input id="o3" name="need" data-label="Requirement" placeholder="e.g. 1 kanal house in DHA Lahore"></div><div class="field" style="margin-bottom:14px"><label for="o4">Budget</label><input id="o4" name="budget" data-label="Budget"></div><button class="btn btn-wa btn-block"><i class="fa-brands fa-whatsapp"></i> Send on WhatsApp</button></form></div>
</div></section>
<section class="section white"><div class="container"><div class="sec-head"><h2>Popular with overseas buyers</h2></div>{listings_block({"luxury":True}, 6)}</div></section>"""
built.append(page("overseas-pakistanis.html", "Property for Overseas Pakistanis — Video Tours & Safe Transfers | Mayo Real Estates", "Buy a house, villa or plot in Lahore or Islamabad from abroad with live video tours, verified documents and power-of-attorney transfers.", overseas, "overseas", 31737859))

# ---------------- CALCULATORS ----------------
calc = f"""{page_hero([(None,"Calculators")], "Property calculators", "Convert marla and kanal, estimate home-finance installments and get a rough construction budget.", 20074182)}
<section class="section tight"><div class="container" style="display:grid;gap:26px">
<div class="tool" id="converter"><h2>Area converter</h2><div class="tool-row"><div class="field"><label for="cvVal">Area</label><input id="cvVal" type="number" value="1" min="0" step="any"></div>
<div class="field"><label for="cvUnit">Unit</label><select id="cvUnit"><option value="kanal">Kanal</option><option value="marla">Marla</option><option value="sqft">Square feet</option><option value="sqyd">Square yards</option><option value="acre">Acre</option><option value="sqm">Square metres</option></select></div>
<div class="field"><label for="cvMarla">1 marla =</label><select id="cvMarla"><option value="225">225 sq ft (DHA, Bahria)</option><option value="272.25">272.25 sq ft (revenue)</option><option value="250">250 sq ft</option></select></div></div><div class="out" id="cvOut"></div></div>
<div class="tool" id="instCalc"><h2>Home finance installment</h2><div class="tool-row"><div class="field"><label for="icPrice">Property price (PKR)</label><input id="icPrice" type="number" value="50000000" step="100000"></div><div class="field"><label for="icDp">Down payment (%)</label><input id="icDp" type="number" value="30"></div><div class="field"><label for="icYears">Years</label><input id="icYears" type="number" value="15"></div></div><div class="tool-row" style="margin-top:12px"><div class="field"><label for="icRate">Yearly profit rate (%)</label><input id="icRate" type="number" value="12" step="0.1"></div></div><div class="out" id="icOut"></div><p class="note" style="margin-top:12px">Banks set their own rates and terms. Use your bank's current rate for an accurate figure.</p></div>
<div class="tool" id="costCalc"><h2>Construction cost estimate</h2><div class="tool-row"><div class="field"><label for="ccPreset">Plot size</label><select id="ccPreset"><option value="2250">5 marla (approx. 2,250 sq ft covered)</option><option value="4500" selected>10 marla (approx. 4,500 sq ft)</option><option value="7500">1 kanal (approx. 7,500 sq ft)</option><option value="13000">2 kanal (approx. 13,000 sq ft)</option></select></div><div class="field"><label for="ccArea">Covered area (sq ft)</label><input id="ccArea" type="number" value="4500"></div><div class="field"><label for="ccGrey">Grey structure rate (PKR / sq ft)</label><input id="ccGrey" type="number" value="4000"></div></div><div class="tool-row" style="margin-top:12px"><div class="field"><label for="ccFinish">Finishing rate (PKR / sq ft)</label><input id="ccFinish" type="number" value="4500"></div></div><div class="out" id="ccOut"></div><p class="note" style="margin-top:12px">Rates change with material prices and finishing quality. Enter the rates your builder quotes for a realistic budget.</p></div>
</div></section>"""
built.append(page("calculators.html", "Marla Kanal Converter, Home Finance & Construction Cost Calculator | Mayo Real Estates", "Convert marla, kanal, square feet and square yards; estimate home finance installments and construction costs in Pakistan.", calc, "calculators", 20074182))

# ---------------- ABOUT ----------------
about = f"""{page_hero([(None,"About us")], "Wakeel Mayo and Mayo Real Estates", "A Lahore property business built on one promise: we visit it, we check it, and we stand behind it.", 18285958)}
<section class="section tight"><div class="container split" style="align-items:start"><div class="prose">
<p>Mayo Real Estates is led by <b>Wakeel Mayo</b> from Raiwind, Lahore. We help families and investors buy and sell houses, luxury villas, farmhouses, plots and commercial property in Lahore's top societies — DHA, Bahria Town, Gulberg, Model Town, Lake City and the farmhouse belts of Bedian Road and Raiwind Road — and, through trusted partners, in Islamabad, Rawalpindi, Karachi and the Murree hills.</p>
<h2>What we believe</h2><ul><li><b>See it first.</b> We list what we have visited ourselves.</li><li><b>Paper before payment.</b> No token is paid until documents are checked.</li><li><b>One person accountable.</b> You deal with Wakeel Mayo from first call to transfer.</li><li><b>Straight talk.</b> If a deal isn't right for you, we say so.</li></ul>
<p>Whether it's your first 5 marla home or a weekend farmhouse with a pool, we would be glad to help.</p>
<p><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> WhatsApp Wakeel Mayo</a></p></div>
<div><img src="{img(8143683)}" alt="Mansion with lawn" style="border-radius:14px" loading="lazy">
<div class="stat-row mt"><div><b>{len(SOCIETIES)}</b>Societies & areas</div><div><b>{len(CITIES)}</b>Cities</div><div><b>6</b>Property types</div><div><b>24/7</b>WhatsApp</div></div></div></div></section>{cta_band()}"""
built.append(page("about.html", "About Mayo Real Estates — Wakeel Mayo, Lahore", "Mayo Real Estates, led by Wakeel Mayo in Raiwind, Lahore — houses, villas, farmhouses, plots and commercial property across Pakistan.", about, "about", 18285958))

# ---------------- CONTACT ----------------
contact = f"""{page_hero([(None,"Contact")], "Talk to Wakeel Mayo", "Call, WhatsApp or email — we usually reply within the hour.", 7031604)}
<section class="section tight"><div class="container contact-grid">
<div class="box"><h2>Contact details</h2>
<div class="c-line"><i class="fa-brands fa-whatsapp"></i><div><small>WhatsApp & call</small><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{SITE['phone1']}</a></div></div>
<div class="c-line"><i class="fa-solid fa-phone"></i><div><small>Phone</small><a href="tel:{TEL2}">{SITE['phone2']}</a></div></div>
<div class="c-line"><i class="fa-solid fa-envelope"></i><div><small>Email</small><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></div>
<div class="c-line"><i class="fa-solid fa-location-dot"></i><div><small>Based in</small><b>{SITE['office']}, Pakistan</b></div></div>
<div class="c-line"><i class="fa-solid fa-clock"></i><div><small>Hours</small><b>Every day, 10am – 9pm (WhatsApp any time)</b></div></div>
<div style="margin-top:18px">{social("social big")}</div></div>
<form class="box" data-wa="Assalam o Alaikum, message from mayorealestates.com:"><h2>Send a message</h2><div class="form-grid">
<div class="field"><label for="c1">Name</label><input id="c1" name="name" data-label="Name" required></div><div class="field"><label for="c2">Phone</label><input id="c2" name="phone" data-label="Phone" type="tel" required></div>
<div class="field"><label for="c3">I want to</label><select id="c3" name="want" data-label="Purpose"><option>Buy a property</option><option>Sell a property</option><option>Invest</option><option>Rent out my property</option><option>Something else</option></select></div>
<div class="field"><label for="c4">City</label><select id="c4" name="city" data-label="City">{''.join('<option>%s</option>' % c['name'] for c in CITIES)}</select></div>
<div class="field full"><label for="c5">Message</label><textarea id="c5" name="msg" data-label="Message" required></textarea></div></div>
<button class="btn btn-wa btn-block" style="margin-top:12px"><i class="fa-brands fa-whatsapp"></i> Send on WhatsApp</button>
<a class="btn btn-line btn-block" style="margin-top:10px" href="mailto:{SITE['email']}"><i class="fa-solid fa-envelope"></i> Or email us</a></form>
</div></section>"""
built.append(page("contact.html", "Contact Mayo Real Estates — WhatsApp +92 347 4209912", "Contact Wakeel Mayo at Mayo Real Estates, Lahore. WhatsApp +92 347 4209912, call +92 305 4512133, email wakeelmayo@gmail.com.", contact, "contact", 7031604))

# ---------------- FAQ ----------------
faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in FAQS]}
built.append(page("faq.html", "Frequently Asked Questions | Mayo Real Estates", "Answers about commission, document verification, overseas buying, site visits and listing your property with Mayo Real Estates.",
    page_hero([(None,"FAQs")], "Frequently asked questions", "Quick answers about buying and selling with us.", 7045703) +
    '<section class="section tight"><div class="narrow">' + "".join('<details class="q"><summary>%s</summary><p>%s</p></details>' % (e(q), e(a)) for q, a in FAQS) + '</div></section>' + cta_band(), "faq", 7045703, faq_ld))

# ---------------- BLOG ----------------
built.append(page("blog.html", "Property Guides & Advice for Pakistan | Mayo Real Estates", "Plain-language property guides: marla and kanal, DHA vs Bahria Town, farmhouse checklist, documents, overseas buying and Islamabad sectors.",
    page_hero([(None,"Guides")], "Property guides", "Plain-language advice before you buy or sell.", 38773558) +
    '<section class="section tight"><div class="container"><div class="grid">' + "".join(f'<a class="post-card" href="blog-{p["slug"]}.html"><img src="{img(p["photo"],True)}" alt="" loading="lazy"><div class="bd"><div class="meta">{datetime.date.fromisoformat(p["date"]).strftime("%d %B %Y")}</div><h3>{e(p["title"])}</h3><p>{e(p["excerpt"])}</p></div></a>' for p in POSTS) + '</div></div></section>', "blog", 38773558))
for p in POSTS:
    ld = {"@context":"https://schema.org","@type":"Article","headline":p["title"],"datePublished":p["date"],"author":{"@type":"Person","name":SITE["owner"]},"publisher":{"@type":"Organization","name":"Mayo Real Estates"},"image":DOMAIN+"/"+img(p["photo"])}
    more = "".join(f'<a class="post-card" href="blog-{x["slug"]}.html"><img src="{img(x["photo"],True)}" alt="" loading="lazy"><div class="bd"><h3>{e(x["title"])}</h3></div></a>' for x in [y for y in POSTS if y is not p][:3])
    body = page_hero([("blog.html","Guides"),(None,p["title"][:40]+"…")], p["title"], e(p["excerpt"]), p["photo"]) + \
        f'<section class="section tight"><article class="narrow prose"><p class="muted">By {SITE["owner"]} · {datetime.date.fromisoformat(p["date"]).strftime("%d %B %Y")}</p>{p["body"]}</article></section>' + \
        f'<section class="section white"><div class="container"><div class="sec-head"><h2>More guides</h2></div><div class="grid">{more}</div></div></section>' + cta_band()
    built.append(page("blog-%s.html" % p["slug"], p["title"] + " | Mayo Real Estates", p["excerpt"], body, "post", p["photo"], ld))

# ---------------- LEGAL / CREDITS / 404 ----------------
priv = """<h2>What we collect</h2><p>When you contact us by WhatsApp, phone or email we receive the details you choose to share (such as your name, number and property requirement). Our website forms do not store your data on a server — they open WhatsApp with your message so you can send it yourself.</p>
<h2>How we use it</h2><p>Only to reply to you, arrange viewings and complete your property deal. We never sell your details.</p>
<h2>Your shortlist</h2><p>Saved properties are stored only in your own browser and can be cleared at any time.</p>
<h2>Third parties</h2><p>Pages load fonts, icons and maps from Google and Cloudflare, and WhatsApp links open WhatsApp; their own privacy policies apply.</p>
<h2>Contact</h2><p>Questions? Email wakeelmayo@gmail.com.</p>"""
built.append(page("privacy-policy.html", "Privacy Policy | Mayo Real Estates", "How Mayo Real Estates handles your information.", page_hero([(None,"Privacy policy")], "Privacy policy", "Last updated October 2026.", 7045701) + '<section class="section tight"><div class="narrow prose">' + priv + '</div></section>', "legal", noindex=False))
terms = """<h2>Listings</h2><p>Property details and prices are provided by owners and are subject to change. Photos may be representative. All details are confirmed at the site visit and through document verification before any payment.</p>
<h2>No offer</h2><p>Listings on this website are invitations to enquire, not binding offers. A deal is final only through a written agreement signed by buyer and seller.</p>
<h2>Calculators</h2><p>Calculator results are estimates for guidance only.</p>
<h2>Commission</h2><p>Our commission is agreed in writing with each client before any viewing.</p>
<h2>Contact</h2><p>wakeelmayo@gmail.com · +92 347 4209912</p>"""
built.append(page("terms.html", "Terms of Use | Mayo Real Estates", "Terms of use for mayorealestates.com.", page_hero([(None,"Terms")], "Terms of use", "Last updated October 2026.", 7045701) + '<section class="section tight"><div class="narrow prose">' + terms + '</div></section>', "legal"))

ids = [l.split("|") for l in open(os.path.join(ROOT, "images/p/photos.txt"), encoding="utf-8").read().splitlines() if l.strip() and not l.startswith("#")]
ok = [x for x in ids if os.path.exists(os.path.join(ROOT, "images/p/%s.jpg" % x[0]))]
cred = '<p>Photographs on this website are from <a href="https://www.pexels.com" target="_blank" rel="noopener">Pexels</a>, used under the <a href="https://www.pexels.com/license/" target="_blank" rel="noopener">Pexels licence</a>, until our own property photography replaces them. Thank you to the photographers.</p><ul>' + \
    "".join('<li><a href="https://www.pexels.com/photo/%s-%s/" target="_blank" rel="noopener">%s</a></li>' % (s, i, e(s.replace("-", " ").capitalize())) for i, s in ok) + "</ul>"
built.append(page("photo-credits.html", "Photo Credits | Mayo Real Estates", "Credits for photographs used on mayorealestates.com.", page_hero([(None,"Photo credits")], "Photo credits", "Where our photos come from.", 7045701) + '<section class="section tight"><div class="narrow prose">' + cred + '</div></section>', "legal", noindex=True))
built.append(page("404.html", "Page not found | Mayo Real Estates", "This page could not be found.",
    '<section class="section"><div class="narrow center"><h1>This page has moved or no longer exists</h1><p class="lede" style="margin:0 auto 24px">The property may have been sold. Browse what is available now, or tell us what you are looking for.</p><a class="btn btn-brass" href="properties.html">Browse properties</a> <a class="btn btn-wa" href="https://wa.me/%s" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp"></i> WhatsApp us</a></div></section>' % WA, "404", noindex=True))

# ---------------- content.js, logo, sitemap, robots ----------------
cjs = "/* GENERATED by tools/build.py from tools/content.py — edit there, not here. */\nvar SITE=%s;\nvar SOCIETIES=%s;\n" % (
    json.dumps(SITE, ensure_ascii=False), json.dumps([{"slug": s["slug"], "name": s["name"], "city": s["city"]} for s in SOCIETIES], ensure_ascii=False))
open(os.path.join(ROOT, "assets/js/content.js"), "w", encoding="utf-8").write(cjs)
os.makedirs(os.path.join(ROOT, "assets/img"), exist_ok=True)
open(os.path.join(ROOT, "assets/img/logo.svg"), "w").write(LOGO_SVG.replace(' aria-hidden="true"', ''))
skip = {"404.html", "photo-credits.html", "property.html"}
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for f in built:
    if f in skip: continue
    pr = "1.0" if f == "index.html" else ("0.9" if f in ("properties.html",) or f.startswith("property-in-") else "0.8")
    sm.append("<url><loc>%s/%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (DOMAIN, "" if f == "index.html" else f, TODAY, pr))
try:
    lj = open(os.path.join(ROOT, "assets/js/listings.js"), encoding="utf-8").read()
    import re
    for pid in re.findall(r'\{ id:"([a-z0-9-]+)"', lj):
        sm.append("<url><loc>%s/property.html?id=%s</loc><lastmod>%s</lastmod><priority>0.7</priority></url>" % (DOMAIN, pid, TODAY))
except Exception:
    pass
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMAIN)
print("built", len(built), "pages")
