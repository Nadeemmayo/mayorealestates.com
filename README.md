# Mayo Real Estates — mayorealestates.com

Luxury houses, villas, farmhouses, plots, apartments and commercial property in Lahore, Islamabad and across Pakistan.
Owner: Wakeel Mayo · WhatsApp +92 347 4209912 · +92 305 4512133 · wakeelmayo@gmail.com

## Where to edit

| What | File |
|---|---|
| **Add / remove / change a property** | `assets/js/listings.js` (instructions at the top) |
| Your own property photos | upload to `images/listings/`, then list them in that property's `photos:[...]` |
| Mark a property sold | set `status:"sold"` in `listings.js` |
| Phone, WhatsApp, email, Facebook / Instagram / TikTok links | `tools/content.py` → `SITE`, then run `python3 tools/build.py` |
| Society & city guides, blog posts, FAQs | `tools/content.py`, then run `python3 tools/build.py` |
| Colours, fonts, layout | `assets/css/style.css` |
| Logo | `assets/img/logo.svg` (also inside `tools/build.py` → `LOGO_SVG`) |

Listings appear automatically on the home page, category pages, society pages and city pages — no rebuild needed.

## Pages

Home · All properties (filters) · Property detail (`property.html?id=...`) · Houses · Brand-new houses · Old houses ·
Luxury villas · Farmhouses · Plots · Commercial · Apartments · 21 society guides · 5 city pages (Lahore, Islamabad,
Rawalpindi, Karachi, Murree) · Sell your property · Services · Overseas Pakistanis · Calculators (marla/kanal converter,
home-finance installment, construction cost) · About · Contact · Guides (6 articles) · FAQs · Privacy · Terms ·
Photo credits · 404 · `sitemap.xml` · `robots.txt`.

All forms open WhatsApp with the details filled in — no server needed.

## Photos

Demo photos come from Pexels (free licence) and are stored in `images/p/` (large) and `images/p/t/` (cards) by the
GitHub Action in `.github/workflows/fetch-photos.yml` (add a line `id|pexels-slug` to `images/p/photos.txt` to fetch more).
Replace them with real photos of your own properties as they come in.
