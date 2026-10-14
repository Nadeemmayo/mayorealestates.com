# -*- coding: utf-8 -*-
"""Site content for mayorealestates.com — societies, cities, categories, blog posts, FAQs.
Edit here, then run:  python3 tools/build.py   (rebuilds all .html pages)."""

SITE = dict(
    name="Mayo Real Estates", domain="mayorealestates.com", owner="Wakeel Mayo",
    phone1="+92 347 4209912", phone2="+92 305 4512133", whatsapp="923474209912",
    email="wakeelmayo@gmail.com", office="Raiwind, Lahore",
    social=dict(facebook="#", instagram="#", tiktok="#"),
)

# photo ids refer to images/p/<id>.jpg
SOCIETIES = [
  # ---------------- Lahore ----------------
  dict(slug="dha-lahore", name="DHA Lahore", city="Lahore", photo=31737860,
       short="Lahore's most sought-after address — Phases 1 to 9, Prism and beyond.",
       about=["Defence Housing Authority Lahore is the city's benchmark for planned living: wide boulevards, strict building bylaws, underground utilities and its own security. The older phases (1 to 6) are fully settled with mature trees, parks, schools and the famous Y-Block and CCA commercial areas, while Phases 7, 8, 9 Prism and the newer sectors offer modern houses and possession plots at lower entry prices.",
               "We deal in brand-new and old houses from 5 marla to 2 kanal, possession and file plots, and commercial buildings in the CCA and Broadway areas. Every DHA deal we handle is checked against the DHA transfer record before you pay a token."],
       points=["Phases 1–9, Prism, Raya and the newer sectors","5 marla to 2 kanal houses","Possession plots and commercial in CCA & Broadway","Transfer verified at DHA office"]),
  dict(slug="bahria-town-lahore", name="Bahria Town Lahore", city="Lahore", photo=39011061,
       short="Gated living off Canal Road — the Grand Jamia Mosque, theme park and Spanish villas.",
       about=["Bahria Town Lahore sits along Canal Bank Road and the Lahore Ring Road and is one of Pakistan's largest gated communities. Residents value the 24/7 security, uninterrupted maintenance, schools, hospitals and landmarks such as the Grand Jamia Mosque and the Eiffel Tower replica.",
               "We handle 5, 8, 10 marla and 1 kanal houses, Spanish and modern villas, apartments and plots in sectors A to F and the Overseas blocks, with prices that suit both first homes and rental investment."],
       points=["Sectors A–F and Overseas blocks","5 marla homes to 1 kanal villas","Apartments with rental demand","Easy access from Canal Road & Ring Road"]),
  dict(slug="gulberg-lahore", name="Gulberg", city="Lahore", photo=8143668,
       short="Central Lahore prestige — large old houses, MM Alam Road and Main Boulevard.",
       about=["Gulberg is the commercial and social heart of Lahore. Its residential blocks (Gulberg II, III and the surrounding areas) hold some of the city's largest older homes on 1 to 4 kanal plots, while MM Alam Road, Main Boulevard and Liberty Market make it Lahore's prime retail and office address.",
               "We bring you large family houses that can be renovated or rebuilt, luxury apartments in new towers and high-street shops and offices."],
       points=["1–4 kanal family houses","Luxury apartments on Main Boulevard","MM Alam Road & Liberty commercial","Ideal for rebuild projects"]),
  dict(slug="model-town-lahore", name="Model Town", city="Lahore", photo=7587470,
       short="A leafy, established neighbourhood with large plots and old-Lahore charm.",
       about=["Model Town is one of Lahore's oldest planned neighbourhoods, laid out in a ring around the central Model Town Park. Wide, tree-lined roads, big plots and a settled community make it a favourite for families who want space close to the city centre.",
               "Most homes here are older houses on 1 to 4 kanal — excellent for buyers who want to renovate or build a new home in an established area."],
       points=["Large 1–4 kanal plots","Tree-lined roads","Near Model Town Park & Link Road","Old houses for renovation"]),
  dict(slug="johar-town", name="Johar Town", city="Lahore", photo=18611145,
       short="Busy, well-connected and great value — near Emporium Mall and the Expo Centre.",
       about=["Johar Town is a large residential and commercial area between Canal Road and the Lahore Ring Road. Home to Emporium Mall, the Expo Centre and many universities, it has strong rental demand and a wide range of house prices.",
               "We list 5 marla to 1 kanal houses — both old and newly built — plus commercial plots and offices."],
       points=["Strong rental demand","Near Emporium Mall & Expo Centre","5 marla to 1 kanal houses","Canal Road & Ring Road access"]),
  dict(slug="lake-city", name="Lake City", city="Lahore", photo=26859048,
       short="Golf-course living on Raiwind Road with wide plots and a calm, gated setting.",
       about=["Lake City on Raiwind Road is a gated community planned around an 18-hole golf course and a lake. Its large plot sizes and low density attract families building luxury homes and villas.",
               "We deal in 1 and 2 kanal houses, luxury pool villas and residential plots across Lake City's sectors."],
       points=["Golf course & lake","1–2 kanal luxury villas","Low-density, gated","Raiwind Road location"]),
  dict(slug="bahria-orchard", name="Bahria Orchard", city="Lahore", photo=102728,
       short="Affordable Bahria living on Raiwind Road — plots and homes for growing families.",
       about=["Bahria Orchard is a large gated project on Raiwind Road with residential plots and homes at a lower entry price than Bahria Town. It is popular with first-time buyers and investors looking for growth along the Raiwind corridor."],
       points=["Budget-friendly plots","Gated Bahria community","Raiwind Road corridor","Good for first-time buyers"]),
  dict(slug="valencia-town", name="Valencia Town", city="Lahore", photo=26595553,
       short="Quiet, well-kept and close to Defence Road — loved by families.",
       about=["Valencia Town on Defence Road is a well-maintained gated society with parks, a commercial area and quick links to DHA and Raiwind Road. It offers quieter streets and better value than neighbouring DHA phases."],
       points=["Gated & well maintained","Close to DHA","10 marla to 1 kanal houses","Parks in every block"]),
  dict(slug="park-view-city-lahore", name="Park View City Lahore", city="Lahore", photo=31722506,
       short="A new society on Multan Road with plots on easy installments.",
       about=["Park View City Lahore on Multan Road is a newer development offering residential plots in blocks such as Platinum, Gold, Executive and Overseas, many on installment plans."],
       points=["Plots on installments","Multan Road access","New infrastructure","Overseas block"]),
  dict(slug="bedian-road", name="Bedian Road Farmhouses", city="Lahore", photo=28054875,
       short="Lahore's farmhouse belt — pools, lawns and weekend estates near DHA.",
       about=["Bedian Road, running east from DHA towards the border, is Lahore's best-known farmhouse area. Owners build weekend homes and event venues on 4 to 20 kanal plots with pools, orchards and lawns, while staying 10–20 minutes from DHA.",
               "We deal in ready farmhouses and farmhouse land, and help with boundary, fard and registry checks before purchase."],
       points=["4 to 20 kanal farmhouses","Pools, lawns & orchards","10–20 min from DHA","Land for custom farmhouses"]),
  dict(slug="raiwind-road", name="Raiwind Road", city="Lahore", photo=10546914,
       short="Our home ground — farmhouse land, housing schemes and growing value.",
       about=["Raiwind Road connects Thokar Niaz Baig to Raiwind and is lined with major projects such as Lake City, Bahria Orchard and many farmhouse estates. Mayo Real Estates is based in Raiwind, so we know every link road and village in this corridor.",
               "We deal in agricultural and farmhouse land, houses in the surrounding schemes and commercial plots on the main road."],
       points=["Our local speciality","Farmhouse & agricultural land","Commercial plots on main road","Fast-growing corridor"]),
  # ---------------- Islamabad / Rawalpindi ----------------
  dict(slug="e-7-islamabad", name="E-7 Islamabad", city="Islamabad", photo=7045711,
       short="Islamabad's most exclusive sector, at the foot of the Margalla Hills.",
       about=["E-7 sits right below the Margalla Hills and is Islamabad's most exclusive residential sector, home to ambassadors, senior officials and business families. Houses are large — mostly 1 to 4 kanal — with hill views and quiet, green streets.",
               "Supply is very limited, so we work privately with owners. Ask us for discreet viewings."],
       points=["1–4 kanal mansions","Margalla Hill views","Very limited supply","Discreet, private deals"]),
  dict(slug="f-6-f-7-islamabad", name="F-6 & F-7 Islamabad", city="Islamabad", photo=7031607,
       short="Central, green and walkable — Super Market and Jinnah Super on your doorstep.",
       about=["F-6 and F-7 are among Islamabad's original sectors: central, green and close to the Super Market, Jinnah Super, Kohsar Market and the Margalla trails. Many older homes are being rebuilt as contemporary houses."],
       points=["Central location","Near Jinnah Super & Kohsar","Old houses and new rebuilds","1 kanal and above"]),
  dict(slug="e-11-islamabad", name="E-11 Islamabad", city="Islamabad", photo=18559073,
       short="Apartments and houses near Margalla Road with good hill views.",
       about=["E-11 is a popular private-sector area at the western end of Margalla Road, with apartment buildings and family houses, schools and quick access to the motorway."],
       points=["Apartments & houses","Near Margalla Road","Motorway access"]),
  dict(slug="dha-islamabad", name="DHA Islamabad", city="Islamabad", photo=35361412,
       short="Defence living on GT Road — Phases 1 to 5, Valley and Highway sectors.",
       about=["DHA Islamabad-Rawalpindi spreads along GT Road and the Islamabad Expressway, with Phases 1 and 2 well developed and settled. It offers secure, planned living with parks, Giga Mall and wide roads, at better value than the central sectors.",
               "We list new and old houses, villas and possession plots in all phases."],
       points=["Phases 1–5 and DHA Valley","Near Giga Mall","Houses, villas & plots","Secure gated phases"]),
  dict(slug="bahria-town-islamabad", name="Bahria Town Islamabad / Rawalpindi", city="Rawalpindi", photo=15422346,
       short="Phases 1 to 8 — the twin cities' largest gated community.",
       about=["Bahria Town Rawalpindi/Islamabad runs from Phase 1 near the Islamabad Expressway to Phase 8 along the Rawalpindi Ring Road route. Its security, maintenance and commercial areas such as Spring North and Civic Centre make it a family favourite.",
               "We handle 5 marla to 1 kanal houses, apartments, shops and plots across all phases."],
       points=["Phases 1–8","Houses, shops & apartments","Spring North & Civic Centre","Expressway & Ring Road access"]),
  dict(slug="gulberg-islamabad", name="Gulberg Islamabad", city="Islamabad", photo=31685810,
       short="Gulberg Greens and Residencia — farmhouses and homes off the Expressway.",
       about=["Gulberg Islamabad, with its Greens (farmhouse) and Residencia (residential) sections, sits just off the Islamabad Expressway. Gulberg Greens is known for 4 to 10 kanal farmhouses within a gated, developed society."],
       points=["Gated farmhouses 4–10 kanal","Residencia houses & plots","Islamabad Expressway access"]),
  dict(slug="chak-shahzad", name="Chak Shahzad & Park Road", city="Islamabad", photo=33738275,
       short="Islamabad's classic farmhouse area — orchards and green estates.",
       about=["Chak Shahzad, along Park Road and Simly Dam Road, is Islamabad's established farmhouse area. Estates of 4 to 20 kanal with orchards and lawns sit close to the city and the Expressway."],
       points=["4–20 kanal farmhouses","Orchards & lawns","Near Park Road & Expressway"]),
  dict(slug="blue-area", name="Blue Area", city="Islamabad", photo=33719831,
       short="Islamabad's business district along Jinnah Avenue.",
       about=["Blue Area along Jinnah Avenue is Islamabad's main business district, with office towers, banks and corporate headquarters. We deal in office floors, shops and commercial investments."],
       points=["Office floors & shops","Jinnah Avenue","Corporate tenants"]),
  # ---------------- Karachi ----------------
  dict(slug="dha-karachi", name="DHA Karachi", city="Karachi", photo=30211366,
       short="Phases 1 to 8 — bungalows near Seaview and Clifton.",
       about=["DHA Karachi stretches from the older central phases to Phase 8 along the sea. Bungalows of 300 to 2,000 square yards, sea-facing apartments and the Khayaban commercial streets make it Karachi's premium address."],
       points=["300–2,000 sq. yd bungalows","Near Seaview","Phases 1–8"]),
  dict(slug="clifton-karachi", name="Clifton", city="Karachi", photo=33634443,
       short="Sea-view apartments and classic bungalows in Karachi's heart.",
       about=["Clifton's blocks hold Karachi's best sea-view apartment towers and established bungalows, close to Boat Basin, Do Darya and the beach."],
       points=["Sea-view apartments","Established bungalows","Near Boat Basin"]),
  # ---------------- Murree ----------------
  dict(slug="murree-galyat", name="Murree & Galyat", city="Murree", photo=7031406,
       short="Holiday villas and hillside land in Bhurban, Nathia Gali and Ayubia.",
       about=["The hills of Murree, Bhurban and the Galyat (Nathia Gali, Dunga Gali, Ayubia) are Pakistan's favourite summer escape. Holiday homes here earn good rental income in summer and snowfall season."],
       points=["Holiday villas","Hillside plots","Rental-income homes"]),
]

CITIES = [
  dict(slug="lahore", short="DHA, Bahria Town, Gulberg & farmhouses", name="Lahore", photo=12912453, photo2=16364707,
       title="Property for sale in Lahore",
       intro="Houses, villas, farmhouses, plots and commercial property across DHA, Bahria Town, Gulberg, Model Town, Lake City, Bedian Road and Raiwind Road.",
       about=["Lahore is Pakistan's second-largest city and its cultural capital. Its property market runs from historic Model Town and Gulberg to the planned phases of DHA and Bahria Town, with a strong farmhouse belt on Bedian Road and Raiwind Road.",
              "Mayo Real Estates is based on Raiwind Road, Lahore. We visit every property ourselves, check documents before you pay and stay with you until the transfer is complete."]),
  dict(slug="islamabad", short="E-7, F-7, DHA & farmhouses", name="Islamabad", photo=30665958, photo2=38773558,
       title="Property for sale in Islamabad",
       intro="Mansions in E-7 and F-7, homes in DHA and Bahria Town, farmhouses in Chak Shahzad and Gulberg Greens, and offices in Blue Area.",
       about=["Islamabad's sector system, green belts and the Margalla Hills make it Pakistan's most planned city. The central sectors (E-7, F-6, F-7) are premium and scarce, while DHA, Bahria Town and Gulberg offer modern gated living.",
              "We work with trusted partners in Islamabad and arrange site visits, CDA/society verification and transfers on your behalf."]),
  dict(slug="rawalpindi", short="Bahria Town & DHA phases", name="Rawalpindi", photo=37937785, photo2=34430707,
       title="Property for sale in Rawalpindi",
       intro="Bahria Town phases 1–8, DHA Islamabad-Rawalpindi and well-priced homes across the twin city.",
       about=["Rawalpindi shares its gated communities with Islamabad — Bahria Town and DHA — and offers better value with quick links to the Islamabad Expressway and the new airport."]),
  dict(slug="karachi", short="DHA bungalows & Clifton", name="Karachi", photo=16240077, photo2=10753082,
       title="Property for sale in Karachi",
       intro="Bungalows in DHA, sea-view apartments in Clifton and investment property in Pakistan's largest city.",
       about=["Karachi is Pakistan's largest city and financial hub. DHA and Clifton are its premium areas, close to the sea, with bungalows measured in square yards and high-rise sea-view apartments."]),
  dict(slug="murree", short="Hill villas & holiday homes", name="Murree", photo=7031407, photo2=20281627,
       title="Holiday homes in Murree & Galyat",
       intro="Mountain villas in Bhurban and hillside plots in Nathia Gali — your own place in the hills.",
       about=["Murree and the Galyat are Pakistan's best-loved hill stations, a short drive from Islamabad. A villa here is a family retreat that can also earn holiday-rental income."]),
]

CATEGORIES = [
  dict(file="houses-for-sale.html", name="Houses for sale", filt={"type":"house"}, photo=8134821,
       h1="Houses for sale in Lahore, Islamabad & across Pakistan",
       intro="Brand-new and old houses from 5 marla to 2 kanal in DHA, Bahria Town, Gulberg, Model Town and more."),
  dict(file="new-houses.html", name="Brand-new houses", filt={"type":"house","condition":"new"}, photo=31737860,
       h1="Brand-new houses for sale",
       intro="Newly built, never-lived-in houses with modern designs — ready to move in."),
  dict(file="old-houses.html", name="Old houses", filt={"type":"house","condition":"old"}, photo=7587470,
       h1="Old houses for sale — live in, renovate or rebuild",
       intro="Established homes on large plots in prime locations, often the best value per marla."),
  dict(file="luxury-villas.html", name="Luxury villas", filt={"luxury":True}, photo=26859048,
       h1="Luxury villas, mansions & pool homes",
       intro="Pool villas, designer homes and grand mansions for families who want the very best."),
  dict(file="farmhouses.html", name="Farmhouses", filt={"type":"farmhouse"}, photo=28054875,
       h1="Farmhouses for sale in Lahore & Islamabad",
       intro="Weekend estates with pools, lawns and orchards on Bedian Road, Chak Shahzad and Gulberg Greens."),
  dict(file="plots.html", name="Plots", filt={"type":"plot"}, photo=20074182,
       h1="Residential plots & land for sale",
       intro="Possession plots, installment plots and farmhouse land — build your dream home."),
  dict(file="commercial-property.html", name="Commercial", filt={"type":"commercial"}, photo=12955940,
       h1="Shops, offices & commercial buildings",
       intro="High-street shops, office floors and full commercial buildings for business or rental income."),
  dict(file="apartments.html", name="Apartments", filt={"type":"apartment"}, photo=33634443,
       h1="Apartments & flats for sale",
       intro="Luxury apartments with views, and easy-to-manage flats with strong rental demand."),
]

FAQS = [
  ("Do you charge buyers a commission?", "Our standard commission is agreed with you in writing before any viewing — there are no hidden charges. Call or WhatsApp us and we will explain it for the property you like."),
  ("Can you verify the documents before I pay?", "Yes. Before you pay any token we check the title with the society or the land record office (fard, registry, intiqal, or society transfer record) and confirm there are no dues or disputes."),
  ("I live abroad. Can I buy without coming to Pakistan?", "Yes. We send video tours, verify documents, and the transfer can be completed through a registered power of attorney given to a family member you trust. See our Overseas Pakistanis page."),
  ("Are the prices on the website final?", "Prices are the asking price from the owner. Most prices are negotiable — we negotiate on your behalf."),
  ("Do you deal only in Lahore?", "Our office is on Raiwind Road, Lahore, but we deal across Lahore, Islamabad, Rawalpindi, Karachi and the Murree hills through trusted partners."),
  ("Can I list my property with you?", "Yes. Use the Sell your property page or WhatsApp us the details and photos. We visit, photograph and list it, and bring you serious buyers only."),
  ("Do you arrange home finance?", "We can introduce you to banks that offer home finance and help with the valuation and documents they need."),
  ("How quickly can I book a site visit?", "Usually the same or next day. WhatsApp us the property link and your preferred time."),
]

POSTS = [
  dict(slug="marla-kanal-square-feet-guide", title="Marla, kanal and square feet: a simple guide for buyers", date="2026-10-10", photo=20074182,
       excerpt="Why a 10 marla plot is not the same size everywhere, and how to convert marla, kanal, square feet and square yards.",
       body="""<p>In Pakistan land is measured in marla and kanal, but the size of one marla is not the same everywhere. Before you compare two properties, make sure you are comparing the same unit.</p>
<h2>The basic units</h2>
<ul><li><b>1 kanal = 20 marla</b></li><li><b>1 acre = 8 kanal = 160 marla</b></li><li><b>1 square yard = 9 square feet</b></li></ul>
<h2>How big is one marla?</h2>
<p>Many housing societies, including DHA Lahore and Bahria Town, use <b>225 square feet per marla</b>, so a kanal is 4,500 square feet. Government land records traditionally use <b>272.25 square feet per marla</b> (a kanal of 5,445 square feet). Some older areas use other local sizes. Always ask which marla size the seller is using.</p>
<table><tr><th>Size</th><th>At 225 sq ft / marla</th><th>At 272.25 sq ft / marla</th></tr>
<tr><td>5 marla</td><td>1,125 sq ft</td><td>1,361 sq ft</td></tr><tr><td>10 marla</td><td>2,250 sq ft</td><td>2,723 sq ft</td></tr><tr><td>1 kanal</td><td>4,500 sq ft</td><td>5,445 sq ft</td></tr><tr><td>2 kanal</td><td>9,000 sq ft</td><td>10,890 sq ft</td></tr></table>
<h2>Karachi uses square yards</h2>
<p>In Karachi, bungalows are sold in square yards: a 500 square yard plot is 4,500 square feet — the same as a 1 kanal plot in a 225-square-foot society.</p>
<p>Use our <a href="calculators.html">area converter</a> to switch between units instantly.</p>"""),
  dict(slug="dha-vs-bahria-town-lahore", title="DHA Lahore or Bahria Town Lahore: which suits your family?", date="2026-10-06", photo=39011061,
       excerpt="Location, budget, lifestyle and resale — an honest comparison of Lahore's two biggest gated communities.",
       body="""<p>Both DHA Lahore and Bahria Town Lahore are secure, planned communities. The right choice depends on your budget, where you work and the lifestyle you want.</p>
<h2>Location</h2><p>DHA is in the east of Lahore, close to the Cantt, the airport and Gulberg. Bahria Town is in the south-west along Canal Road and the Ring Road, closer to Thokar Niaz Baig and Raiwind Road.</p>
<h2>Budget</h2><p>For the same plot size, Bahria Town usually costs noticeably less than the older DHA phases. DHA's newer phases (8, 9 Prism and beyond) narrow the gap.</p>
<h2>Lifestyle</h2><ul><li><b>DHA</b>: established neighbourhoods, strong commercial areas such as Y-Block and CCA, top schools and a long track record.</li><li><b>Bahria Town</b>: landmarks, parks, theme park, its own hospital and schools, and a lively, family-friendly feel.</li></ul>
<h2>Resale and rent</h2><p>Settled DHA phases hold value strongly; Bahria Town apartments and 5–10 marla homes attract steady tenants.</p>
<p>Not sure? <a href="contact.html">Talk to us</a> — we will shortlist homes in both and show you in one day.</p>"""),
  dict(slug="buying-a-farmhouse-checklist", title="Buying a farmhouse near Lahore or Islamabad: a checklist", date="2026-09-28", photo=28054849,
       excerpt="Road access, water, land records, boundary and approvals — what to check before you buy a farmhouse.",
       body="""<p>A farmhouse is a lifestyle purchase and an investment. Because many farmhouses sit on agricultural land outside society limits, a little extra checking protects you.</p>
<h2>Before you pay a token</h2><ol><li><b>Land record:</b> check the fard and the registry/intiqal so the seller's name and area match.</li><li><b>Demarcation:</b> get the boundary measured by the patwari so the wall matches the record.</li><li><b>Access:</b> confirm a legal, metalled road to the gate.</li><li><b>Water:</b> check the bore depth and water quality.</li><li><b>Electricity:</b> confirm the connection and its load.</li><li><b>Society rules:</b> inside a gated farmhouse scheme, check the transfer process and any bylaws.</li></ol>
<h2>Running costs</h2><p>Budget for a caretaker, lawn and pool maintenance, security and electricity.</p>
<p>We handle these checks for every farmhouse we sell. See <a href="farmhouses.html">farmhouses for sale</a>.</p>"""),
  dict(slug="property-documents-pakistan", title="Property documents in Pakistan explained", date="2026-09-20", photo=7045701,
       excerpt="Fard, registry, intiqal, allotment letter, NDC — what each document means and when you need it.",
       body="""<p>Buying property safely in Pakistan comes down to the right documents. Here are the main ones in plain words.</p>
<h2>Land outside societies</h2><ul><li><b>Fard:</b> an extract from the land record showing who owns the land and how much.</li><li><b>Registry (sale deed):</b> the registered deed of sale between buyer and seller.</li><li><b>Intiqal (mutation):</b> the record that transfers ownership in the land revenue record.</li></ul>
<h2>Inside housing societies</h2><ul><li><b>Allotment letter / file:</b> proof of the plot or house allotment in your name.</li><li><b>NDC (No Demand Certificate):</b> confirms there are no unpaid dues before transfer.</li><li><b>Transfer letter:</b> issued by the society once the transfer is done.</li><li><b>Possession letter and map approval:</b> needed before you build.</li></ul>
<h2>Our rule</h2><p>We never ask you to pay a token until the documents are checked. <a href="services.html">See our services</a>.</p>"""),
  dict(slug="overseas-pakistanis-buying-property", title="How overseas Pakistanis can buy property safely", date="2026-09-12", photo=31737859,
       excerpt="Video tours, power of attorney and paying through proper banking channels — buying from abroad, step by step.",
       body="""<p>Thousands of overseas Pakistanis buy a home back home every year. Here is how to do it safely while you are abroad.</p>
<h2>Step by step</h2><ol><li><b>Shortlist with video:</b> we send live video tours and real photos of each property.</li><li><b>Verify:</b> we check the documents and share copies with you.</li><li><b>Power of attorney:</b> appoint a trusted family member through a registered special power of attorney, attested by the Pakistani embassy or consulate where you live.</li><li><b>Pay through banks:</b> send funds through proper banking channels to keep a clear record.</li><li><b>Transfer:</b> your attorney completes the transfer; we attend every step.</li></ol>
<p>Many Pakistani banks also offer accounts and home finance designed for non-resident Pakistanis. Ask us for an introduction.</p>
<p>Read more on our <a href="overseas-pakistanis.html">Overseas Pakistanis</a> page.</p>"""),
  dict(slug="islamabad-sectors-explained", title="Islamabad's sectors explained for property buyers", date="2026-09-04", photo=38773558,
       excerpt="E, F, G, H, I — what the letters mean and which sectors suit which buyers.",
       body="""<p>Islamabad is divided into lettered zones, each split into numbered sectors (for example F-7) and sub-sectors (F-7/3).</p>
<h2>The main letters</h2><ul><li><b>E and F sectors:</b> closest to the Margalla Hills; the most prestigious and expensive (E-7, F-6, F-7, F-8).</li><li><b>G sectors:</b> central, with a mix of government and private housing and big markets.</li><li><b>H sectors:</b> universities, institutions and green areas.</li><li><b>I sectors:</b> industrial areas and newer housing.</li></ul>
<h2>Beyond the sectors</h2><p>DHA, Bahria Town, Gulberg and the farmhouse areas of Chak Shahzad and Park Road offer gated or larger-plot living outside the CDA sectors.</p>
<p>See <a href="property-in-islamabad.html">property for sale in Islamabad</a>.</p>"""),
]
