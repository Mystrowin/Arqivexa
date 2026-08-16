from pathlib import Path
import re

ROOT = Path("website")
CSS = ROOT / "styles.css"
POLISH_MARKER = "ARQIVEXA SITE-WIDE POLISH"

GUIDE_CLUSTER = {
    "guides.html",
    "arqivexa-vs-7zip.html",
    "edit-compressed-files-without-extracting.html",
    "editable-compressed-archives.html",
    "how-to-open-cfs-file.html",
    "lzma2-compressed-archives.html",
    "open-archive-as-folder-windows.html",
    "projfs-archive-workflow.html",
    "windows-11-archive-manager.html",
    "cfs-file-format.html",
}

NAV_ITEMS = [
    ("how-arqivexa-works.html", "How it works", "how-arqivexa-works.html"),
    ("guides.html", "Guides", "guides"),
    ("install.html", "Install", "install.html"),
    ("security.html", "Security", "security.html"),
    ("faq.html", "FAQ", "faq.html"),
    ("download.html", "Download", "download.html"),
]

FOOTER = (
    '<div class="footer-links">'
    '<a href="./">Home</a>'
    '<a href="what-is-arqivexa.html">Overview</a>'
    '<a href="guides.html">Guides</a>'
    '<a href="how-arqivexa-works.html">How it works</a>'
    '<a href="install.html">Install</a>'
    '<a href="security.html">Security</a>'
    '<a href="faq.html">FAQ</a>'
    '<a href="cfs-file-format.html">.cfs format</a>'
    '<a href="download.html">Download</a>'
    '<a href="https://github.com/Mystrowin/Arqivexa">GitHub</a>'
    '</div>'
)

POLISH_CSS = r'''

/* ================================================================
   ARQIVEXA SITE-WIDE POLISH — 2026-08-16
   Keeps the homepage hero distinctive while giving documentation,
   guides, comparison, setup, security, download, and error pages a
   consistent editorial layout.
   ================================================================ */

html {
  color-scheme: dark;
}

body {
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.site-shell {
  overflow: clip;
}

.site-header {
  gap: 1.5rem;
  padding-inline: 0.15rem;
}

nav {
  gap: 1.12rem;
}

nav a:not(.nav-download) {
  position: relative;
  padding: 0.55rem 0.08rem;
}

nav a:not(.nav-download)::after {
  content: "";
  position: absolute;
  left: 0;
  right: 100%;
  bottom: 0.18rem;
  height: 1px;
  background: var(--blue-bright);
  transition: right 160ms ease;
}

nav a:not(.nav-download):hover::after,
nav a:not(.nav-download)[aria-current="page"]::after {
  right: 0;
}

nav a[aria-current="page"] {
  color: #f5f9ff;
}

.nav-download {
  transition: border-color 160ms ease, background 160ms ease, transform 160ms ease;
}

.nav-download:hover,
.nav-download[aria-current="page"] {
  border-color: #6fb1ff;
  background: #102743;
}

.nav-download:hover {
  transform: translateY(-1px);
}

/* The homepage has exactly two release choices. Do not leave half a
   four-column grid empty. */
.home-page .release-access-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

/* Secondary pages use a deliberate editorial hero instead of reusing
   the homepage's two-column product-demo hero with an empty right side. */
.content-page .hero {
  min-height: 0;
  grid-template-columns: minmax(0, 790px) minmax(240px, 1fr);
  gap: clamp(2.5rem, 6vw, 5.5rem);
  padding: 6rem 0 4.75rem;
  position: relative;
  isolation: isolate;
  border-bottom: 1px solid rgba(72, 99, 134, 0.38);
}

.content-page .hero::after {
  content: "";
  grid-column: 2;
  grid-row: 1;
  align-self: center;
  justify-self: stretch;
  min-height: 285px;
  border: 1px solid rgba(69, 118, 174, 0.44);
  background:
    linear-gradient(140deg, rgba(47, 129, 247, 0.15), transparent 57%),
    linear-gradient(rgba(80, 137, 201, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(80, 137, 201, 0.08) 1px, transparent 1px),
    rgba(8, 15, 25, 0.5);
  background-size: auto, 32px 32px, 32px 32px, auto;
  box-shadow: inset 0 1px rgba(140, 200, 255, 0.08), 0 24px 70px rgba(0, 0, 0, 0.2);
  clip-path: polygon(9% 0, 100% 0, 100% 84%, 91% 100%, 0 100%, 0 16%);
  opacity: 0.9;
}

.content-page .hero-copy {
  grid-column: 1;
  grid-row: 1;
  position: relative;
  z-index: 1;
  max-width: 790px;
}

.content-page .hero h1 {
  max-width: 790px;
  margin-bottom: 1.45rem;
  font-size: clamp(3rem, 5.8vw, 5.35rem);
  line-height: 0.98;
  letter-spacing: -0.058em;
}

.content-page .hero-intro {
  max-width: 730px;
  font-size: 1.04rem;
  line-height: 1.7;
}

.content-page .hero .kicker a {
  color: #8dc4ff;
}

/* Bring useful content into view sooner and make guide/document cards
   feel like one design system rather than homepage step tiles. */
.content-page .section {
  padding: 2rem 0 5.75rem;
}

.content-page .section-heading {
  margin-bottom: 2.15rem;
}

.content-page h2 {
  font-size: clamp(2rem, 4vw, 3.35rem);
}

.content-page .steps-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  border: 0;
}

.content-page .step-card {
  min-height: 220px;
  padding: 1.65rem;
  border: 1px solid var(--border);
  background: linear-gradient(145deg, rgba(17, 26, 39, 0.82), rgba(9, 13, 20, 0.84));
  transition: transform 170ms ease, border-color 170ms ease, background 170ms ease;
}

.content-page .step-card:last-child {
  border-right: 1px solid var(--border);
}

.content-page .step-card:hover {
  transform: translateY(-2px);
  border-color: #3d6694;
  background: linear-gradient(145deg, rgba(20, 36, 56, 0.86), rgba(9, 14, 22, 0.88));
}

.content-page .steps-grid > .step-card:last-child:nth-child(odd) {
  grid-column: 1 / -1;
  min-height: 190px;
}

.content-page .step-card h3 {
  margin-bottom: 0.8rem;
  font-size: 1.22rem;
}

.content-page .step-card h3 a {
  color: #eaf4ff;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.22em;
}

.content-page .step-card h3 a:hover {
  color: #9dccff;
  text-decoration: underline;
}

.content-page .step-card p {
  margin-bottom: 0;
}

.content-page .split-section,
.content-page .limitations-section {
  padding-bottom: 5.75rem;
}

.content-page .comparison-wrap,
.content-page .primary-download-card,
.content-page .alternative-downloads,
.content-page .requirements-panel,
.content-page .projfs-panel,
.content-page .hash-panel,
.content-page .update-panel,
.content-page .limitations-copy,
.content-page .support-card {
  box-shadow: inset 0 1px rgba(138, 194, 255, 0.05);
}

.content-page .comparison-wrap {
  margin-top: 0;
}

.content-page footer,
.home-page footer {
  margin-top: 1rem;
}

.footer-links {
  justify-content: flex-end;
  flex-wrap: wrap;
  row-gap: 0.7rem;
}

.footer-links a {
  white-space: nowrap;
}

/* 404 remains lightweight, but now uses the same spacing and type scale. */
.error-page main {
  min-height: calc(100vh - 78px);
  display: flex;
  align-items: center;
}

.error-page .section {
  width: min(100%, 860px);
  padding: 6rem 0;
}

.error-page h1 {
  font-size: clamp(3rem, 7vw, 5.6rem);
  line-height: 0.98;
}

@media (max-width: 1080px) {
  nav {
    gap: 0.78rem;
    font-size: 0.78rem;
  }

  .content-page .hero {
    grid-template-columns: minmax(0, 1fr) minmax(190px, 0.42fr);
    gap: 2.5rem;
  }

  .content-page .hero::after {
    min-height: 240px;
  }
}

@media (max-width: 940px) {
  /* Override the old blanket tablet hide rule: a 900px-wide layout can
     still carry the full navigation when spacing is tightened. */
  nav a:not(.nav-download) {
    display: inline-flex;
  }

  .site-header {
    gap: 0.9rem;
  }

  nav {
    gap: 0.62rem;
    font-size: 0.72rem;
  }

  .content-page .hero {
    grid-template-columns: 1fr;
    gap: 0;
    padding: 4.8rem 0 4rem;
  }

  .content-page .hero-copy {
    grid-column: 1;
  }

  .content-page .hero::after {
    display: none;
  }

  .home-page .release-access-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 780px) {
  nav a:not(.nav-download) {
    display: none;
  }

  .content-page .steps-grid {
    grid-template-columns: 1fr;
  }

  .content-page .steps-grid > .step-card:last-child:nth-child(odd) {
    grid-column: auto;
  }

  .content-page .step-card,
  .content-page .steps-grid > .step-card:last-child:nth-child(odd) {
    min-height: 0;
  }
}

@media (max-width: 680px) {
  .content-page .hero {
    padding: 4rem 0 3.4rem;
  }

  .content-page .hero h1 {
    font-size: clamp(2.65rem, 12.5vw, 4.1rem);
    letter-spacing: -0.052em;
  }

  .content-page .section {
    padding-bottom: 4.5rem;
  }

  .content-page .step-card {
    padding: 1.3rem;
  }

  .footer-links {
    justify-content: flex-start;
  }
}
'''


def current_key(filename: str) -> str | None:
    if filename in GUIDE_CLUSTER:
        return "guides"
    direct = {
        "how-arqivexa-works.html": "how-arqivexa-works.html",
        "install.html": "install.html",
        "security.html": "security.html",
        "faq.html": "faq.html",
        "download.html": "download.html",
    }
    return direct.get(filename)


def nav_for(filename: str) -> str:
    active = current_key(filename)
    links = []
    for href, label, key in NAV_ITEMS:
        classes = ' class="nav-download"' if href == "download.html" else ""
        aria = ' aria-current="page"' if active == key else ""
        links.append(f'<a{classes}{aria} href="{href}">{label}</a>')
    return '<nav aria-label="Primary navigation">' + ''.join(links) + '</nav>'


def set_body_class(text: str, cls: str) -> str:
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1) or ""
        class_match = re.search(r'\bclass=("|\')(.*?)\1', attrs, flags=re.S)
        if class_match:
            classes = class_match.group(2).split()
            if cls not in classes:
                classes.append(cls)
            replacement = f'class={class_match.group(1)}{" ".join(classes)}{class_match.group(1)}'
            attrs = attrs[:class_match.start()] + replacement + attrs[class_match.end():]
        else:
            attrs = attrs.rstrip() + f' class="{cls}"'
        return '<body' + attrs + '>'
    return re.sub(r'<body([^>]*)>', repl, text, count=1, flags=re.I)


def add_theme_color(text: str) -> str:
    if 'name="theme-color"' in text or "name='theme-color'" in text:
        return text
    viewport = re.compile(r'(<meta\s+name=["\']viewport["\'][^>]*>)', re.I)
    return viewport.sub(r'\1\n    <meta name="theme-color" content="#07090d">', text, count=1)


def polish_html(path: Path) -> None:
    name = path.name
    text = path.read_text(encoding="utf-8")
    original = text

    text = add_theme_color(text)

    if name == "index.html":
        text = set_body_class(text, "home-page")
    elif name == "404.html":
        text = set_body_class(text, "error-page")
    elif name == "what-is-cfs.html":
        # Compatibility redirect: keep it minimal and noindex.
        pass
    else:
        text = set_body_class(text, "content-page")

    if name not in {"404.html", "what-is-cfs.html"}:
        nav_pattern = re.compile(r'<nav\s+aria-label=["\']Primary navigation["\'][^>]*>.*?</nav>', re.I | re.S)
        if not nav_pattern.search(text):
            raise RuntimeError(f"Primary nav not found in {path}")
        text = nav_pattern.sub(nav_for(name), text, count=1)

        footer_pattern = re.compile(r'<div\s+class=["\']footer-links["\'][^>]*>.*?</div>', re.I | re.S)
        if footer_pattern.search(text):
            text = footer_pattern.sub(FOOTER, text, count=1)

    if text != original:
        path.write_text(text, encoding="utf-8")


def polish_css() -> None:
    text = CSS.read_text(encoding="utf-8")
    text = text.replace("/* CFS GitHub Pages styles */", "/* Arqivexa GitHub Pages styles */", 1)
    if POLISH_MARKER not in text:
        text = text.rstrip() + POLISH_CSS + "\n"
    CSS.write_text(text, encoding="utf-8")


def main() -> None:
    polish_css()
    for page in sorted(ROOT.glob("*.html")):
        polish_html(page)
    print("Applied Arqivexa site-wide polish to stylesheet, navigation, footers, and page classes.")


if __name__ == "__main__":
    main()
