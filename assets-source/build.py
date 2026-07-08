#!/usr/bin/env python3
import base64, os
HERE = os.path.dirname(os.path.abspath(__file__))

def b64(path):
    with open(os.path.join(HERE, path), 'rb') as f:
        return base64.b64encode(f.read()).decode()

FONT_ALEGREYA = f"data:font/woff2;base64,{b64('Alegreya_500.woff2')}"
FONT_COMMISSIONER = f"data:font/woff2;base64,{b64('Commissioner_400.woff2')}"
IMG_LOGO = f"data:image/png;base64,{b64('logo_final.png')}"
IMG_DOCTOR = f"data:image/jpeg;base64,{b64('doctor.jpg')}"
IMG_WAITING = f"data:image/jpeg;base64,{b64('g_waiting.jpg')}"
IMG_EXAM1 = f"data:image/jpeg;base64,{b64('g_exam1.jpg')}"
IMG_EXAM2 = f"data:image/jpeg;base64,{b64('g_exam2.jpg')}"
IMG_RECEPTION = f"data:image/jpeg;base64,{b64('g_reception.jpg')}"

# ---------------------------------------------------------------- logo mark (πραγματικό logo iPC)
LOGO = '<span class="mark" role="img" aria-label="iPC Medicine — λογότυπο"></span>'

def icon(name):
    ic = {
        'gp': '<circle cx="9" cy="8" r="3.2"/><circle cx="17" cy="9.5" r="2.4"/><path d="M3 21c0-3.6 2.7-6 6-6s6 2.4 6 6"/><path d="M14.5 21c0-2.6 1.4-4.6 4-4.6 1.9 0 3.5 1.3 3.5 4.6"/>',
        'longevity': '<path d="M4 12c0-4.4 3.6-8 8-8s8 3.6 8 8-3.6 8-8 8"/><path d="M12 20a8 8 0 0 1-5.7-2.4"/><path d="M12 8v4l3 2"/>',
        'micro': '<circle cx="8" cy="9" r="1.4"/><circle cx="15" cy="7" r="1.4"/><circle cx="17" cy="14" r="1.4"/><circle cx="10" cy="16" r="1.4"/><circle cx="12.4" cy="11.5" r="2.6"/><path d="M9.4 10.2 6.9 9.4M13.9 8.4 15 7.4M14.7 12.6 16 13.6M11.3 13.6 10.4 15"/>',
        'acu': '<path d="M5 19 19 5"/><path d="M15 5h4v4"/><path d="M8.5 15.5l2 2"/><path d="M11 13l2 2"/>',
        'person': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="10" r="2.6"/><path d="M7.5 17.5c.6-2.2 2.4-3.4 4.5-3.4s3.9 1.2 4.5 3.4"/>',
        'iv': '<path d="M9 3h6"/><rect x="8.5" y="4.5" width="7" height="9" rx="2"/><path d="M12 13.5V19"/><path d="M12 22c1.1 0 1.9-.9 1.9-1.9C13.9 19 12 16.8 12 16.8S10.1 19 10.1 20.1C10.1 21.1 10.9 22 12 22Z"/>',
    }[name]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ic}</svg>'

SERVICES = [
    ('gp', 'Γενική &amp; Οικογενειακή Ιατρική',
     'Ο προσωπικός σας ιατρός για κάθε ηλικία — προληπτικοί έλεγχοι, παρακολούθηση χρόνιων παθήσεων, εμβολιασμοί, διαχείριση οξέων περιστατικών και συντονισμός με ειδικούς, για όλη την οικογένεια.'),
    ('longevity', 'Ιατρική Μακροζωίας',
     'Στοχευμένη πρόληψη και παρεμβάσεις στον τρόπο ζωής — διατροφή, άσκηση, ύπνος, διαχείριση στρες — με στόχο περισσότερα χρόνια <em>υγείας</em>, όχι απλώς ζωής.'),
    ('micro', 'Μικροβίωμα',
     'Αξιολόγηση και υποστήριξη της υγείας του εντερικού μικροβιώματος, που συνδέεται στενά με την ανοσία, τον μεταβολισμό και τη συνολική ευεξία του οργανισμού.'),
    ('acu', 'Ιατρικός Βελονισμός',
     'Τεκμηριωμένος ιατρικός βελονισμός για τη διαχείριση του πόνου, του άγχους και λειτουργικών διαταραχών, ως συμπληρωματικό εργαλείο μέσα σε ένα ολοκληρωμένο πλάνο θεραπείας.'),
    ('iv', 'Ενδοφλέβιες Θεραπείες — IV Drips',
     'Εξατομικευμένες ενδοφλέβιες χορηγήσεις βιταμινών, μετάλλων, αμινοξέων και αντιοξειδωτικών — <em>πάντα μετά από μέτρηση των επιπέδων στον ορό του αίματος</em>, ώστε να καλύπτονται οι πραγματικές σας ανάγκες.'),
    ('person', 'Εξατομικευμένη Ιατρική Προσέγγιση',
     'Κάθε πλάνο φροντίδας σχεδιάζεται γύρω από εσάς: το ιστορικό, τις συνήθειες, τους στόχους και τις ανάγκες σας. Ιατρική με το πρόσωπο στο κέντρο.'),
]

def service_card(i, s, detailed=False):
    name, title, desc = s
    num = f'{i+1:02d}'
    extra = ''
    return f'''<article class="svc">
<div class="svc-top"><span class="svc-ic">{icon(name)}</span><span class="svc-num">{num}</span></div>
<h3>{title}</h3>
<p>{desc}</p>
</article>'''

services_home = '\n'.join(service_card(i, s) for i, s in enumerate(SERVICES))
services_full = '\n'.join(service_card(i, s, True) for i, s in enumerate(SERVICES))

# ---------------------------------------------------------------- JSON-LD
JSONLD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Physician",
  "name": "iPC Medicine – Δρ. Γεώργιος Ι. Μπέλλος",
  "alternateName": "Ιδιωτικό Ιατρείο iPC Medicine",
  "description": "Ιατρείο Γενικής και Οικογενειακής Ιατρικής στο Κορωπί. Ολοκληρωμένη, προσωποκεντρική φροντίδα με έμφαση στην πρόληψη, τη μακροζωία, το μικροβίωμα και τον ιατρικό βελονισμό.",
  "medicalSpecialty": ["PrimaryCare", "Geriatric"],
  "founder": { "@type": "Physician", "name": "Δρ. Γεώργιος Ι. Μπέλλος", "jobTitle": "Ειδικός Γενικής & Οικογενειακής Ιατρικής" },
  "areaServed": [
    { "@type": "City", "name": "Κορωπί" },
    { "@type": "AdministrativeArea", "name": "Ανατολική Αττική" }
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[ΔΙΕΥΘΥΝΣΗ]",
    "addressLocality": "Κορωπί",
    "addressRegion": "Αττική",
    "postalCode": "19400",
    "addressCountry": "GR"
  },
  "telephone": "[ΤΗΛΕΦΩΝΟ]",
  "email": "[EMAIL]",
  "url": "https://ipcmedicine.com",
  "priceRange": "€€",
  "openingHours": ["Mo-Fr 09:00-21:00"],
  "sameAs": [
    "https://www.facebook.com/",
    "https://www.instagram.com/dr.bellos.ipc.medicine/"
  ]
}
</script>'''

# ---------------------------------------------------------------- CSS
CSS = '''
@font-face{font-family:'Alegreya';font-style:normal;font-weight:400 800;font-display:swap;src:url(__FONT_ALEGREYA__) format('woff2');}
@font-face{font-family:'Commissioner';font-style:normal;font-weight:100 900;font-display:swap;src:url(__FONT_COMMISSIONER__) format('woff2');}

/* Πάντα λευκό φόντο με μαύρα γράμματα — σταθερό theme, χωρίς dark mode. */
:root, :root[data-theme="dark"], :root[data-theme="light"]{
  color-scheme:light;
  --ground:#ffffff; --ink:#111318; --muted:#565e6b; --faint:#8b93a1;
  --line:#e7e9ee; --surface:#f6f8fb; --surface-2:#eef1f8;
  --red:#d8433a; --red-soft:#fbeceb;
  --blue:#46528c; --blue-ink:#3a4578; --blue-soft:#eef1f8;
  --serif:'Alegreya',Georgia,'Times New Roman',serif;
  --sans:'Commissioner',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  --wrap:1180px; --pad:clamp(20px,5vw,64px);
  --r:14px;
}

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;letter-spacing:.005em}
img{max-width:100%;display:block}
h1,h2,h3{font-family:var(--serif);font-weight:600;line-height:1.08;margin:0;
  text-wrap:balance;letter-spacing:-.01em}
a{color:inherit;text-decoration:none}
p{margin:0}
::selection{background:var(--blue);color:#fff}

/* signature: paired red+blue hairline */
.rule{display:inline-block;width:38px;height:4px;border-radius:2px;
  background:linear-gradient(90deg,var(--red) 0 50%,var(--blue) 50% 100%)}

.wrap{max-width:var(--wrap);margin-inline:auto;padding-inline:var(--pad)}
.eyebrow{font-size:.74rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;
  color:var(--blue-ink);display:flex;align-items:center;gap:12px}
.btn{display:inline-flex;align-items:center;gap:.5em;font-family:var(--sans);font-weight:600;
  font-size:.98rem;padding:.82em 1.5em;border-radius:999px;cursor:pointer;border:1.5px solid transparent;
  transition:transform .18s ease,background .18s ease,color .18s ease,border-color .18s}
.btn-primary{background:var(--blue);color:#fff}
.btn-primary:hover{background:var(--blue-ink);transform:translateY(-2px)}
.btn-ghost{border-color:var(--line);color:var(--ink);background:transparent}
.btn-ghost:hover{border-color:var(--blue);color:var(--blue-ink);transform:translateY(-2px)}
:focus-visible{outline:2.5px solid var(--blue);outline-offset:3px;border-radius:4px}

/* logo (πραγματικό iPC mark) */
.mark{display:inline-block;background:url(__LOGO__) center/contain no-repeat;flex:none}

/* header */
header.site{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--ground) 88%,transparent);
  backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;justify-content:space-between;gap:20px;height:72px}
.brand{display:flex;align-items:center;gap:12px}
.brand .mark{width:46px;height:39px;flex:none}
.brand .wm{display:flex;flex-direction:column;line-height:1}
.brand .wm b{font-family:var(--sans);font-weight:700;font-size:1.06rem;letter-spacing:.02em}
.brand .wm b i{font-style:normal;color:var(--red)}
.brand .wm small{font-size:.54rem;letter-spacing:.08em;line-height:1.25;text-transform:uppercase;color:var(--muted);margin-top:3px;max-width:285px}
nav.main{display:flex;align-items:center;gap:6px}
nav.main a{position:relative;padding:.5em .9em;font-weight:500;font-size:.96rem;color:var(--muted);border-radius:8px;transition:color .15s}
nav.main a:hover{color:var(--ink)}
nav.main a.active{color:var(--ink)}
nav.main a.active::after{content:"";position:absolute;left:.9em;right:.9em;bottom:2px;height:3px;border-radius:2px;
  background:linear-gradient(90deg,var(--red) 0 50%,var(--blue) 50% 100%)}
.head-cta{display:flex;align-items:center;gap:10px}
.menu-btn{display:none;background:none;border:1px solid var(--line);border-radius:9px;width:42px;height:42px;
  cursor:pointer;align-items:center;justify-content:center;color:var(--ink)}
.menu-btn svg{width:20px;height:20px}

/* views */
.view{display:none;animation:fade .5s ease both}
.view.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.view{animation:none}*{scroll-behavior:auto!important}}

section{padding-block:clamp(56px,8vw,104px)}
.sec-head{max-width:640px;display:flex;flex-direction:column;gap:16px;margin-bottom:48px}
.sec-head h2{font-size:clamp(1.9rem,3.6vw,2.7rem)}
.sec-head p{color:var(--muted);font-size:1.08rem}
.lead{font-size:1.16rem;color:var(--muted);max-width:60ch}

/* hero */
.hero{padding-top:clamp(40px,6vw,72px);padding-bottom:clamp(48px,7vw,96px)}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(32px,5vw,72px);align-items:center}
.hero h1{font-size:clamp(2.5rem,5.6vw,4.1rem);margin:22px 0 0}
.hero h1 em{font-style:italic;color:var(--blue-ink)}
.hero .slogan{margin-top:26px;font-size:1.2rem;color:var(--muted);max-width:52ch;line-height:1.6}
.hero-cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px}
.hero-media{position:relative}
.hero-media .frame{border-radius:var(--r);overflow:hidden;border:1px solid var(--line);
  box-shadow:0 30px 70px -40px rgba(20,24,50,.5)}
.hero-media .frame img{width:100%;height:100%;object-fit:cover;aspect-ratio:4/3.4}
.hero-media .badge{position:absolute;left:-18px;bottom:-18px;background:var(--ground);border:1px solid var(--line);
  border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;box-shadow:0 18px 40px -26px rgba(20,24,50,.55)}
.hero-media .badge .mark{width:40px;height:34px;flex:none}
.hero-media .badge b{font-family:var(--serif);font-size:1rem;line-height:1.1}
.hero-media .badge small{color:var(--muted);font-size:.76rem}

/* trust strip */
.pillars{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:var(--r);overflow:hidden;margin-top:8px}
.pillars div{background:var(--ground);padding:22px 20px}
.pillars b{font-family:var(--serif);font-size:1.05rem;display:block}
.pillars span{color:var(--muted);font-size:.9rem}

/* services grid */
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.svc{background:var(--ground);border:1px solid var(--line);border-radius:var(--r);padding:28px 26px;
  display:flex;flex-direction:column;gap:14px;transition:border-color .2s,transform .2s,box-shadow .2s}
.svc:hover{border-color:color-mix(in srgb,var(--blue) 40%,var(--line));transform:translateY(-4px);
  box-shadow:0 26px 50px -38px rgba(20,24,50,.5)}
.svc-top{display:flex;align-items:center;justify-content:space-between}
.svc-ic{width:46px;height:46px;border-radius:12px;background:var(--blue-soft);color:var(--blue-ink);
  display:grid;place-items:center}
.svc-ic svg{width:24px;height:24px}
.svc-num{font-family:var(--serif);font-size:1.5rem;color:var(--faint)}
.svc h3{font-size:1.24rem}
.svc p{color:var(--muted);font-size:.98rem}
.svc p em{font-style:italic;color:var(--ink)}

/* doctor */
.doc-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:clamp(30px,5vw,64px);align-items:start}
.doc-photo{border-radius:var(--r);overflow:hidden;border:1px solid var(--line);align-self:start;background:var(--surface)}
.doc-photo img{width:100%;height:auto;display:block}
.doc-body{display:flex;flex-direction:column;gap:22px}
.doc-body h2{font-size:clamp(2rem,4vw,2.9rem)}
.doc-body .role{color:var(--blue-ink);font-weight:600}
.doc-body p{color:var(--muted);max-width:62ch}
.doc-body p strong{color:var(--ink);font-weight:600}
.cred{border-top:1px solid var(--line);padding-top:22px;margin-top:6px}
.cred h4{margin:0 0 12px;font-family:var(--sans);font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.cred ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.cred li{display:flex;gap:12px;align-items:flex-start;color:var(--muted)}
.cred li::before{content:"";width:8px;height:8px;margin-top:9px;border-radius:2px;flex:none;
  background:linear-gradient(135deg,var(--red),var(--blue))}
.cred li em{font-style:normal;color:var(--faint)}

/* gallery band */
.gallery{background:var(--surface)}
.gal-grid{display:grid;grid-template-columns:1.6fr 1fr;gap:20px}
.gal-grid figure{margin:0;border-radius:var(--r);overflow:hidden;border:1px solid var(--line);background:var(--ground)}
.gal-grid img{width:100%;height:100%;object-fit:cover}
.gal-grid .tall{grid-row:span 1}
figcaption{padding:14px 18px;color:var(--muted);font-size:.86rem;display:flex;align-items:center;gap:10px}

/* showroom gallery */
.showroom{display:grid;grid-template-columns:1.5fr 1fr;grid-template-rows:repeat(2,232px);gap:16px}
.showroom figure{margin:0;border-radius:var(--r);overflow:hidden;border:1px solid var(--line);background:var(--surface);position:relative}
.showroom figure.feat{grid-row:1 / span 2}
.showroom img{width:100%;height:100%;object-fit:cover;transition:transform .6s ease}
.showroom figure:hover img{transform:scale(1.045)}
.showroom .cap{position:absolute;left:14px;bottom:12px;background:rgba(255,255,255,.92);color:var(--ink);
  font-size:.78rem;font-weight:600;padding:.35em .8em;border-radius:999px;backdrop-filter:blur(4px);
  display:flex;align-items:center;gap:8px}
.showroom .cap::before{content:"";width:22px;height:3px;border-radius:2px;
  background:linear-gradient(90deg,var(--red) 0 50%,var(--blue) 50% 100%)}
@media (max-width:760px){.showroom{grid-template-columns:1fr;grid-template-rows:none}
  .showroom figure.feat{grid-row:auto}.showroom figure{aspect-ratio:16/10}}

/* quote */
.quote{text-align:center;max-width:820px;margin-inline:auto;display:flex;flex-direction:column;gap:26px;align-items:center}
.quote blockquote{margin:0;font-family:var(--serif);font-size:clamp(1.5rem,3.4vw,2.25rem);line-height:1.32;font-style:italic}
.quote cite{font-style:normal;color:var(--muted);font-size:.95rem;letter-spacing:.02em}

/* contact */
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5vw,60px)}
.info-list{display:flex;flex-direction:column;gap:2px;margin-top:8px}
.info{display:flex;gap:16px;padding:20px 0;border-bottom:1px solid var(--line);align-items:flex-start}
.info:last-child{border-bottom:0}
.info .ic{width:42px;height:42px;border-radius:11px;background:var(--surface);color:var(--blue-ink);
  display:grid;place-items:center;flex:none}
.info .ic svg{width:20px;height:20px}
.info b{display:block;font-family:var(--sans);font-weight:600;font-size:.78rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--muted);margin-bottom:3px}
.info span{color:var(--ink);font-size:1.06rem}
.info span.ph{color:var(--faint);font-style:italic}
.form{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:clamp(24px,3vw,34px);
  display:flex;flex-direction:column;gap:16px}
.form label{font-size:.82rem;font-weight:600;color:var(--muted);display:flex;flex-direction:column;gap:7px}
.form input,.form textarea{font-family:var(--sans);font-size:1rem;color:var(--ink);background:var(--ground);
  border:1px solid var(--line);border-radius:10px;padding:.75em .9em;width:100%}
.form input:focus,.form textarea:focus{outline:none;border-color:var(--blue)}
.form textarea{min-height:120px;resize:vertical}
.map-note{margin-top:22px;border:1px dashed var(--line);border-radius:var(--r);padding:18px 20px;
  display:flex;align-items:center;justify-content:space-between;gap:16px;color:var(--muted);font-size:.92rem;flex-wrap:wrap}

/* CTA band */
.cta-band{background:var(--blue);color:#fff;border-radius:var(--r);padding:clamp(36px,5vw,60px);
  display:flex;align-items:center;justify-content:space-between;gap:30px;flex-wrap:wrap}
.cta-band h2{color:#fff;font-size:clamp(1.7rem,3vw,2.3rem);max-width:18ch}
.cta-band p{color:rgba(255,255,255,.82);margin-top:10px}
.cta-band .btn-primary{background:#fff;color:var(--blue-ink)}
.cta-band .btn-primary:hover{background:#f0f2fb}

/* footer */
footer.site{background:var(--surface);border-top:1px solid var(--line);padding-block:56px 32px;margin-top:0}
.foot-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1.2fr;gap:40px}
footer .brand .mark{width:48px;height:40px}
footer .col h5{font-family:var(--sans);font-size:.76rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);margin:0 0 16px;font-weight:600}
footer .col ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:11px}
footer .col a{color:var(--muted);font-size:.95rem;transition:color .15s}
footer .col a:hover{color:var(--blue-ink)}
footer .about{max-width:34ch;color:var(--muted);font-size:.94rem;margin-top:16px}
.social{display:flex;gap:10px;margin-top:18px}
.social a{width:40px;height:40px;border:1px solid var(--line);border-radius:10px;display:grid;place-items:center;color:var(--ink)}
.social a:hover{border-color:var(--blue);color:var(--blue-ink)}
.social svg{width:18px;height:18px}
.foot-bottom{border-top:1px solid var(--line);margin-top:44px;padding-top:24px;display:flex;
  justify-content:space-between;gap:16px;flex-wrap:wrap;color:var(--faint);font-size:.85rem}

/* responsive */
@media (max-width:940px){
  .hero-grid{grid-template-columns:1fr;gap:40px}
  .hero-media{order:-1;max-width:520px}
  .doc-grid{grid-template-columns:1fr}
  .doc-photo{position:static;max-width:440px}
  .contact-grid{grid-template-columns:1fr}
  .svc-grid{grid-template-columns:repeat(2,1fr)}
  .pillars{grid-template-columns:repeat(2,1fr)}
  .foot-grid{grid-template-columns:1fr 1fr;gap:32px}
  .gal-grid{grid-template-columns:1fr}
}
@media (max-width:640px){
  body{font-size:16px}
  nav.main,.head-cta .btn{display:none}
  .menu-btn{display:flex}
  .svc-grid{grid-template-columns:1fr}
  .foot-grid{grid-template-columns:1fr}
  .cta-band{flex-direction:column;align-items:flex-start}
  header.site .brand .wm small{display:none}
}
/* mobile menu */
.mobile-menu{display:none;position:fixed;inset:72px 0 auto 0;background:var(--ground);border-bottom:1px solid var(--line);
  z-index:49;padding:16px var(--pad) 26px;flex-direction:column;gap:4px}
.mobile-menu.open{display:flex}
.mobile-menu a{padding:.85em .4em;font-size:1.1rem;font-family:var(--serif);border-bottom:1px solid var(--line)}
.mobile-menu .btn{margin-top:14px;justify-content:center}
'''

# ---------------------------------------------------------------- BODY
BODY = f'''
<a class="skip" href="#main" style="position:absolute;left:-9999px">Μετάβαση στο περιεχόμενο</a>
<header class="site">
  <div class="wrap bar">
    <a class="brand" href="#/" data-nav="home" aria-label="iPC Medicine – Αρχική">
      {LOGO}
      <span class="wm"><b>iPC <i>Medicine</i></b><small>ΟΛΟΚΛΗΡΩΜΕΝΗ ΠΡΟΣΩΠΟΚΕΝΤΡΙΚΗ ΙΑΤΡΙΚΗ ΠΡΟΣΕΓΓΙΣΗ</small></span>
    </a>
    <nav class="main" aria-label="Κύρια πλοήγηση">
      <a href="#/" data-nav="home">Αρχική</a>
      <a href="#/iatros" data-nav="iatros">Ο Ιατρός</a>
      <a href="#/ypiresies" data-nav="ypiresies">Υπηρεσίες</a>
      <a href="#/epikoinonia" data-nav="epikoinonia">Επικοινωνία</a>
    </nav>
    <div class="head-cta">
      <a class="btn btn-primary" href="#/epikoinonia" data-nav="epikoinonia">Κλείστε ραντεβού</a>
      <button class="menu-btn" aria-label="Μενού" aria-expanded="false" id="menuBtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
  <div class="mobile-menu" id="mobileMenu">
    <a href="#/" data-nav="home">Αρχική</a>
    <a href="#/iatros" data-nav="iatros">Ο Ιατρός</a>
    <a href="#/ypiresies" data-nav="ypiresies">Υπηρεσίες</a>
    <a href="#/epikoinonia" data-nav="epikoinonia">Επικοινωνία</a>
    <a class="btn btn-primary" href="#/epikoinonia" data-nav="epikoinonia">Κλείστε ραντεβού</a>
  </div>
</header>

<main id="main">

<!-- ============ HOME ============ -->
<div class="view active" id="view-home">
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <p class="eyebrow"><span class="rule"></span> Γενική &amp; Οικογενειακή Ιατρική · Κορωπί</p>
        <h1>Ολοκληρωμένη, <em>προσωποκεντρική</em> ιατρική φροντίδα.</h1>
        <p class="slogan">Ένας σύγχρονος χώρος υγείας, αφιερωμένος στην πρόληψη, την εξατομικευμένη φροντίδα και τη συνολική ευεξία του ανθρώπου.</p>
        <div class="hero-cta">
          <a class="btn btn-primary" href="#/epikoinonia" data-nav="epikoinonia">Κλείστε ραντεβού</a>
          <a class="btn btn-ghost" href="#/ypiresies" data-nav="ypiresies">Οι υπηρεσίες μας</a>
        </div>
      </div>
      <div class="hero-media">
        <div class="frame"><img src="{IMG_WAITING}" alt="Ο χώρος υποδοχής του ιατρείου iPC Medicine στο Κορωπί — καθαρός, φωτεινός και minimal" width="1700" height="1143"></div>
        <div class="badge">{LOGO}<div><b>iPC Medicine</b><br><small>Δρ. Γεώργιος Ι. Μπέλλος</small></div></div>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="pillars">
        <div><b>Πρόληψη</b><span>πρώτα απ' όλα</span></div>
        <div><b>Ολιστική ματιά</b><span>ο άνθρωπος ως σύνολο</span></div>
        <div><b>Τεκμηρίωση</b><span>σύγχρονη ιατρική</span></div>
        <div><b>Χρόνος</b><span>ουσιαστική ακρόαση</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow"><span class="rule"></span> Τι προσφέρουμε</p>
        <h2>Έξι πυλώνες φροντίδας, ένας άνθρωπος στο κέντρο.</h2>
        <p>Από τη γενική ιατρική της οικογένειας μέχρι τη μακροζωία και τον ιατρικό βελονισμό — όλα σχεδιασμένα γύρω από εσάς.</p>
      </div>
      <div class="svc-grid">
        {services_home}
        <article class="svc" style="justify-content:center;background:var(--surface)">
          <h3 style="font-size:1.18rem">Χρειάζεστε καθοδήγηση;</h3>
          <p>Κλείστε μια πρώτη επίσκεψη και ας σχεδιάσουμε μαζί το δικό σας πλάνο φροντίδας.</p>
          <a class="btn btn-ghost" href="#/epikoinonia" data-nav="epikoinonia" style="align-self:flex-start;margin-top:4px">Επικοινωνία</a>
        </article>
      </div>
    </div>
  </section>

  <section class="gallery">
    <div class="wrap">
      <div class="doc-grid">
        <div class="doc-photo"><img src="{IMG_DOCTOR}" alt="Δρ. Γεώργιος Ι. Μπέλλος, Ειδικός Γενικής και Οικογενειακής Ιατρικής" width="1000" height="1921"></div>
        <div class="doc-body">
          <p class="eyebrow"><span class="rule"></span> Ο ιατρός σας</p>
          <h2>Δρ. Γεώργιος Ι. Μπέλλος</h2>
          <p class="role">Ειδικός Γενικής &amp; Οικογενειακής Ιατρικής</p>
          <p>Ιδρυτής του <strong>iPC Medicine</strong>, ο Δρ. Μπέλλος αντιμετωπίζει κάθε ασθενή ως σύνολο — σώμα, ιστορικό, συνήθειες και περιβάλλον — και όχι μεμονωμένα συμπτώματα. Στόχος του: περισσότερα χρόνια πραγματικής υγείας, μέσα από πρόληψη, εξατομικευμένη φροντίδα και ουσιαστική σχέση εμπιστοσύνης.</p>
          <a class="btn btn-ghost" href="#/iatros" data-nav="iatros" style="align-self:flex-start">Περισσότερα για τον ιατρό</a>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow"><span class="rule"></span> Ο χώρος μας</p>
        <h2>Ένας σύγχρονος, φιλόξενος χώρος υγείας.</h2>
        <p>Καθαρές, ήρεμες αίθουσες σχεδιασμένες να σας κάνουν να νιώσετε άνετα — στο κέντρο του Κορωπίου.</p>
      </div>
      <div class="showroom">
        <figure class="feat"><img src="{IMG_EXAM1}" alt="Αίθουσα εξέτασης του ιατρείου iPC Medicine — φωτεινός χώρος με φυσικό φως, στο Κορωπί" loading="lazy"><span class="cap">Αίθουσα εξέτασης</span></figure>
        <figure><img src="{IMG_RECEPTION}" alt="Χώρος υποδοχής του ιατρείου iPC Medicine στο Κορωπί" loading="lazy"><span class="cap">Υποδοχή</span></figure>
        <figure><img src="{IMG_EXAM2}" alt="Χώρος εξέτασης iPC Medicine με έργα τέχνης και φυσικό φως" loading="lazy"><span class="cap">Ο χώρος</span></figure>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap quote">
      <span class="rule"></span>
      <blockquote>«Δεν θεραπεύουμε μια ασθένεια· φροντίζουμε έναν άνθρωπο.»</blockquote>
      <cite>— Η φιλοσοφία του iPC Medicine</cite>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="cta-band">
        <div>
          <h2>Ας ξεκινήσουμε τη δική σας φροντίδα.</h2>
          <p>Κλείστε την πρώτη σας επίσκεψη στο ιατρείο μας στο Κορωπί.</p>
        </div>
        <a class="btn btn-primary" href="#/epikoinonia" data-nav="epikoinonia">Κλείστε ραντεβού</a>
      </div>
    </div>
  </section>
</div>

<!-- ============ IATROS ============ -->
<div class="view" id="view-iatros">
  <section>
    <div class="wrap">
      <div class="doc-grid">
        <div class="doc-photo"><img src="{IMG_DOCTOR}" alt="Δρ. Γεώργιος Ι. Μπέλλος, Γενικός Ιατρός στο Κορωπί" width="1000" height="1921"></div>
        <div class="doc-body">
          <p class="eyebrow"><span class="rule"></span> Ο Ιατρός</p>
          <h2>Δρ. Γεώργιος Ι. Μπέλλος</h2>
          <p class="role">Ειδικός Γενικής &amp; Οικογενειακής Ιατρικής · Ιδρυτής iPC Medicine</p>
          <p>Ο Δρ. Γεώργιος Μπέλλος συνδυάζει τη σύγχρονη, τεκμηριωμένη ιατρική με μια βαθιά <strong>προσωποκεντρική</strong> φιλοσοφία. Κάθε επίσκεψη ξεκινά με ουσιαστική συζήτηση και ακρόαση: το ιστορικό, ο τρόπος ζωής και οι στόχοι κάθε ανθρώπου είναι εξίσου σημαντικά με τα εργαστηριακά ευρήματα.</p>
          <p>Η προσέγγισή του εστιάζει στην <strong>πρόληψη</strong> και στη <strong>μακροζωία</strong>: όχι απλώς στη διαχείριση της νόσου, αλλά στη διατήρηση της υγείας σε βάθος χρόνου. Ενσωματώνει τη μελέτη του μικροβιώματος και τον ιατρικό βελονισμό ως συμπληρωματικά εργαλεία, πάντα μέσα σε ένα ολοκληρωμένο, εξατομικευμένο πλάνο.</p>
          <div class="cred">
            <h4>Σπουδές &amp; Εξειδικεύσεις</h4>
            <ul>
              <li>Ειδικότητα Γενικής &amp; Οικογενειακής Ιατρικής <em>· [συμπληρώνεται]</em></li>
              <li>Εξειδίκευση στον Ιατρικό Βελονισμό <em>· [συμπληρώνεται]</em></li>
              <li>Μετεκπαίδευση σε Ιατρική Μακροζωίας &amp; Μικροβίωμα <em>· [συμπληρώνεται]</em></li>
              <li>Μέλος επιστημονικών εταιρειών <em>· [συμπληρώνεται]</em></li>
            </ul>
          </div>
          <a class="btn btn-primary" href="#/epikoinonia" data-nav="epikoinonia" style="align-self:flex-start;margin-top:6px">Κλείστε ραντεβού</a>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- ============ YPIRESIES ============ -->
<div class="view" id="view-ypiresies">
  <section>
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow"><span class="rule"></span> Υπηρεσίες</p>
        <h2>Ολοκληρωμένη φροντίδα, από την πρόληψη έως τη μακροζωία.</h2>
        <p>Ένας σύγχρονος χώρος υγείας αφιερωμένος στη συνολική ευεξία του ανθρώπου.</p>
      </div>
      <div class="svc-grid">
        {services_full}
      </div>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap">
      <div class="cta-band">
        <div><h2>Δεν είστε σίγουροι τι χρειάζεστε;</h2><p>Ας το δούμε μαζί σε μια πρώτη επίσκεψη.</p></div>
        <a class="btn btn-primary" href="#/epikoinonia" data-nav="epikoinonia">Κλείστε ραντεβού</a>
      </div>
    </div>
  </section>
</div>

<!-- ============ EPIKOINONIA ============ -->
<div class="view" id="view-epikoinonia">
  <section>
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow"><span class="rule"></span> Επικοινωνία</p>
        <h2>Κλείστε το ραντεβού σας.</h2>
        <p>Είμαστε στο Κορωπί, στην καρδιά της Ανατολικής Αττικής. Επικοινωνήστε μαζί μας — θα χαρούμε να σας φροντίσουμε.</p>
      </div>
      <div class="contact-grid">
        <div>
          <div class="info-list">
            <div class="info"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-5.5-7-11a7 7 0 0 1 14 0c0 5.5-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg></span><div><b>Διεύθυνση</b><span class="ph">[Οδός &amp; αριθμός], Κορωπί 194 00, Αττική</span></div></div>
            <div class="info"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5c0 8 7 15 15 15l-.5-3.5-4-1-2 2c-2.5-1.3-4.7-3.5-6-6l2-2-1-4Z"/></svg></span><div><b>Τηλέφωνο</b><span class="ph">[+30 21X XXX XXXX]</span></div></div>
            <div class="info"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16v12H4z"/><path d="m4 7 8 6 8-6"/></svg></span><div><b>Email</b><span class="ph">[info@ipcmedicine.com]</span></div></div>
            <div class="info"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><div><b>Ώρες λειτουργίας</b><span class="ph">Δευτ.–Παρ. [09:00–21:00] · Σάββ. [κατόπιν ραντεβού]</span></div></div>
          </div>
          <div class="map-note">
            <span>Θα βρείτε το ιατρείο μας στο κέντρο του Κορωπίου.</span>
            <a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&query=iPC+Medicine+%CE%9A%CE%BF%CF%81%CF%89%CF%80%CE%AF" target="_blank" rel="noopener">Άνοιγμα στους χάρτες</a>
          </div>
        </div>
        <form class="form" onsubmit="return false" aria-label="Φόρμα επικοινωνίας">
          <label>Ονοματεπώνυμο<input type="text" name="name" placeholder="Το όνομά σας" autocomplete="name"></label>
          <label>Τηλέφωνο ή email<input type="text" name="contact" placeholder="Πώς να επικοινωνήσουμε" autocomplete="tel"></label>
          <label>Μήνυμα<textarea name="msg" placeholder="Πείτε μας πώς μπορούμε να βοηθήσουμε"></textarea></label>
          <button class="btn btn-primary" type="submit">Αποστολή αιτήματος</button>
          <p style="color:var(--faint);font-size:.82rem;margin-top:2px">Η φόρμα θα συνδεθεί με email/τηλέφωνο κατά τη δημοσίευση.</p>
        </form>
      </div>
    </div>
  </section>
</div>

</main>

<footer class="site">
  <div class="wrap">
    <div class="foot-grid">
      <div class="col">
        <a class="brand" href="#/" data-nav="home">{LOGO}<span class="wm"><b>iPC <i>Medicine</i></b><small>ΟΛΟΚΛΗΡΩΜΕΝΗ ΠΡΟΣΩΠΟΚΕΝΤΡΙΚΗ ΙΑΤΡΙΚΗ ΠΡΟΣΕΓΓΙΣΗ</small></span></a>
        <p class="about">Ολοκληρωμένη Προσωποκεντρική Ιατρική Φροντίδα. Γενικός &amp; Οικογενειακός Ιατρός στο Κορωπί.</p>
        <div class="social">
          <a href="https://www.facebook.com/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M13 22v-8h2.7l.4-3H13V9c0-.9.3-1.5 1.6-1.5H16V4.8C15.7 4.8 14.7 4.7 13.6 4.7 11.2 4.7 9.7 6.1 9.7 8.7V11H7v3h2.7v8H13Z"/></svg></a>
          <a href="https://www.instagram.com/dr.bellos.ipc.medicine/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17" cy="7" r="1" fill="currentColor" stroke="none"/></svg></a>
        </div>
      </div>
      <div class="col">
        <h5>Σελίδες</h5>
        <ul>
          <li><a href="#/" data-nav="home">Αρχική</a></li>
          <li><a href="#/iatros" data-nav="iatros">Ο Ιατρός</a></li>
          <li><a href="#/ypiresies" data-nav="ypiresies">Υπηρεσίες</a></li>
          <li><a href="#/epikoinonia" data-nav="epikoinonia">Επικοινωνία</a></li>
        </ul>
      </div>
      <div class="col">
        <h5>Υπηρεσίες &amp; Περιοχές</h5>
        <ul>
          <li><a href="#/ypiresies" data-nav="ypiresies">Γενικός Ιατρός Κορωπί</a></li>
          <li><a href="#/ypiresies" data-nav="ypiresies">Οικογενειακή Ιατρική</a></li>
          <li><a href="#/ypiresies" data-nav="ypiresies">Ιατρικός Βελονισμός Αττική</a></li>
          <li><a href="#/ypiresies" data-nav="ypiresies">Ιατρική Μακροζωίας</a></li>
          <li><a href="#/ypiresies" data-nav="ypiresies">Μικροβίωμα</a></li>
          <li><a href="#/ypiresies" data-nav="ypiresies">Ενδοφλέβιες Θεραπείες (IV Drips)</a></li>
        </ul>
      </div>
      <div class="col">
        <h5>Επικοινωνία</h5>
        <ul>
          <li><span style="color:var(--faint)">[Οδός], Κορωπί 194 00</span></li>
          <li><a href="tel:+30">[+30 21X XXX XXXX]</a></li>
          <li><a href="mailto:info@ipcmedicine.com">[info@ipcmedicine.com]</a></li>
          <li><span style="color:var(--faint)">Δευτ.–Παρ. [09:00–21:00]</span></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 iPC Medicine — Δρ. Γεώργιος Ι. Μπέλλος. Με επιφύλαξη παντός δικαιώματος.</span>
      <span>Ολοκληρωμένη Προσωποκεντρική Ιατρική Φροντίδα · Κορωπί, Αττική</span>
    </div>
  </div>
</footer>
{JSONLD}
'''

# ---------------------------------------------------------------- JS
JS = '''
<script>
(function(){
  var views={home:'view-home',iatros:'view-iatros',ypiresies:'view-ypiresies',epikoinonia:'view-epikoinonia'};
  var titles={
    home:'iPC Medicine | Γενικός & Οικογενειακός Ιατρός στο Κορωπί – Δρ. Γεώργιος Μπέλλος',
    iatros:'Ο Ιατρός – Δρ. Γεώργιος Ι. Μπέλλος | iPC Medicine Κορωπί',
    ypiresies:'Υπηρεσίες – Γενική Ιατρική, Μακροζωία, Βελονισμός | iPC Medicine Κορωπί',
    epikoinonia:'Επικοινωνία & Ραντεβού | iPC Medicine – Γενικός Ιατρός Κορωπί'
  };
  function routeKey(){
    var h=(location.hash||'#/').replace('#/','').replace('/','');
    if(h==='iatros'||h==='ypiresies'||h==='epikoinonia') return h;
    return 'home';
  }
  function render(){
    var k=routeKey();
    Object.keys(views).forEach(function(v){
      document.getElementById(views[v]).classList.toggle('active', v===k);
    });
    document.querySelectorAll('nav.main a[data-nav]').forEach(function(a){
      a.classList.toggle('active', a.getAttribute('data-nav')===k);
    });
    document.title=titles[k];
    closeMenu();
    window.scrollTo({top:0,behavior:'instant' in document.documentElement.style?'instant':'auto'});
  }
  function closeMenu(){var m=document.getElementById('mobileMenu');if(m)m.classList.remove('open');
    var b=document.getElementById('menuBtn');if(b)b.setAttribute('aria-expanded','false');}
  document.getElementById('menuBtn').addEventListener('click',function(){
    var m=document.getElementById('mobileMenu');var o=m.classList.toggle('open');
    this.setAttribute('aria-expanded',o?'true':'false');
  });
  window.addEventListener('hashchange',render);
  render();
})();
</script>
'''

CSS_FINAL = CSS.replace('__FONT_ALEGREYA__', FONT_ALEGREYA).replace('__FONT_COMMISSIONER__', FONT_COMMISSIONER).replace('__LOGO__', IMG_LOGO)

# ---- artifact.html (body-only, for preview) ----
artifact = f'<style>{CSS_FINAL}</style>\n{BODY}\n{JS}'
with open(os.path.join(HERE,'artifact.html'),'w',encoding='utf-8') as f:
    f.write(artifact)

# ---- index.html (full document, for hosting/SEO) ----
HEAD = f'''<!doctype html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>iPC Medicine | Γενικός &amp; Οικογενειακός Ιατρός στο Κορωπί – Δρ. Γεώργιος Μπέλλος</title>
<meta name="description" content="iPC Medicine – Ιατρείο Γενικής &amp; Οικογενειακής Ιατρικής στο Κορωπί. Ο Δρ. Γεώργιος Μπέλλος προσφέρει ολοκληρωμένη, προσωποκεντρική φροντίδα: πρόληψη, ιατρική μακροζωίας, μικροβίωμα και ιατρικό βελονισμό. Κλείστε ραντεβού.">
<meta name="keywords" content="γενικός ιατρός Κορωπί, οικογενειακός ιατρός Κορωπί, παθολόγος Κορωπί, ιατρικός βελονισμός Αττική, ιατρική μακροζωίας, μικροβίωμα, Δρ Γεώργιος Μπέλλος, iPC Medicine">
<meta name="author" content="Δρ. Γεώργιος Ι. Μπέλλος">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#46528c">
<link rel="canonical" href="https://ipcmedicine.com/">
<meta property="og:type" content="website">
<meta property="og:locale" content="el_GR">
<meta property="og:site_name" content="iPC Medicine">
<meta property="og:title" content="iPC Medicine | Γενικός & Οικογενειακός Ιατρός στο Κορωπί">
<meta property="og:description" content="Ολοκληρωμένη, προσωποκεντρική ιατρική φροντίδα στο Κορωπί — Δρ. Γεώργιος Μπέλλος.">
<meta property="og:url" content="https://ipcmedicine.com/">
<meta name="twitter:card" content="summary_large_image">
<style>{CSS_FINAL}</style>
</head>
<body>
'''
index = HEAD + BODY + JS + '\n</body>\n</html>\n'
with open(os.path.join(HERE,'index.html'),'w',encoding='utf-8') as f:
    f.write(index)

print('artifact.html', os.path.getsize(os.path.join(HERE,'artifact.html'))//1024,'KB')
print('index.html', os.path.getsize(os.path.join(HERE,'index.html'))//1024,'KB')
