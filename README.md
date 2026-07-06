# BNKM International Ltd. — Website

Static marketing site for a process engineering & project consultancy.
Plain HTML/CSS/JS — no framework, no build step required to serve.
Each page is self-contained (CSS, JS and the logo are inlined), so any page
also renders correctly on its own.

## Pages (9)
Home, About Us, Industries, Services, Energy Transition, Projects,
Technical Expertise, Careers, Contact.

---

## Hosting: GitHub Actions -> GitHub Pages

Deployment is automated by `.github/workflows/deploy.yml`. On every push to
`main`, the workflow stages the static files (excluding source/dev files) and
publishes them to GitHub Pages.

### One-time setup
1. Create a GitHub repo and push these files to the `main` branch:

       git init
       git add .
       git commit -m "BNKM International website"
       git branch -M main
       git remote add origin https://github.com/<you>/<repo>.git
       git push -u origin main

2. In the repo: Settings -> Pages -> Build and deployment -> Source = "GitHub Actions".
3. The "Deploy site to GitHub Pages" workflow runs automatically (watch it under
   the Actions tab). When it finishes, your site is live.

You can also run it manually: Actions -> Deploy site to GitHub Pages -> Run workflow.

---

## Custom domain

The domain is set in TWO places -- keep them in sync:

1. `CNAME` (repo root) -- currently `bnkminternational.com`. Put your real
   domain here (apex like `bnkminternational.com`, or a subdomain like
   `www.bnkminternational.com`). GitHub Pages reads this file on every deploy.
2. `build.py` -> `DOMAIN` -- used for canonical URLs, Open Graph tags and
   `sitemap.xml`. Set it to the same domain, then run `python3 build.py` to
   regenerate the pages (and update `sitemap.xml` / `robots.txt`).

### DNS records (at your domain registrar)
Apex domain (bnkminternational.com):

    A     @   185.199.108.153
    A     @   185.199.109.153
    A     @   185.199.110.153
    A     @   185.199.111.153
    AAAA  @   2606:50c0:8000::153
    AAAA  @   2606:50c0:8001::153
    AAAA  @   2606:50c0:8002::153
    AAAA  @   2606:50c0:8003::153

www subdomain (www.bnkminternational.com):

    CNAME  www   <you>.github.io.

Then in Settings -> Pages -> Custom domain, enter the domain and, once DNS
verifies, tick "Enforce HTTPS". (These are GitHub's published Pages IPs; if
GitHub changes them, use the values in GitHub's current Pages docs.)

---

## Logo
Displayed logo: `assets/bnkm-logo.png` (also used for the social preview image).
It is inlined into each page (a small optimised copy, `assets/_logo_inline.jpg`,
is what gets embedded). To change the logo, replace `assets/bnkm-logo.png` and
re-create `_logo_inline.jpg` (a ~120px-tall JPEG), then run `python3 build.py`.

## Contact form
The form is a front-end stub (shows a confirmation but sends nothing). GitHub
Pages has no server, so wire it to a static form service such as Formspree:

    <form data-contact-form action="https://formspree.io/f/XXXX" method="POST">

Alternatives: Getform, Basin, Google Forms embed.

## SEO
Per-page title/description/keywords, canonical + Open Graph/Twitter tags,
JSON-LD ProfessionalService schema, `sitemap.xml` and `robots.txt`.

## Editing / regenerating
`build.py` assembles all pages from shared head/nav/footer parts plus per-page
content; `scenes.py` holds the SVG industry illustrations. After edits:

    python3 build.py

You can also edit the generated `.html` files directly -- they are plain HTML.

## Imagery
Oil & gas scenes (refinery, offshore platform, onshore pump jacks) are
hand-authored SVG in `scenes.py` -- no stock-photo licensing or hotlink risk.
To use your own licensed photos, replace a `.split-figure.photo` or `.imgband`
block with an `<img>` you have rights to (drop the file in `assets/`).
