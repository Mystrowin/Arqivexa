from pathlib import Path

# One-time helper: append the unified site visual system.
css_path = Path("website/styles.css")
marker = "ARQIVEXA UNIFIED VISUAL SYSTEM — 2026-08-16"
css = css_path.read_text(encoding="utf-8")
if marker in css:
    print("Unified visual system already present.")
    raise SystemExit(0)

block = r'''

/* ARQIVEXA UNIFIED VISUAL SYSTEM — 2026-08-16
   Keep the homepage and all content pages visibly part of one product site. */
.home-page .hero,
.content-page .hero {
  grid-template-columns: minmax(0, 1.06fr) minmax(340px, 0.94fr);
  align-items: center;
  gap: clamp(3rem, 5.5vw, 4.5rem);
  padding: 7rem 0 5rem;
}

.content-page .hero {
  min-height: 610px;
  border-bottom: 0;
  isolation: isolate;
}

.content-page .hero-copy {
  max-width: 760px;
}

.content-page .hero h1 {
  max-width: 760px;
  font-size: clamp(3.2rem, 6.25vw, 5.9rem);
  line-height: 0.95;
  letter-spacing: -0.062em;
}

.content-page .hero-intro {
  max-width: 650px;
  font-size: 1.08rem;
  line-height: 1.72;
}

.content-page .hero::after {
  content: "";
  grid-column: 2;
  grid-row: 1;
  align-self: center;
  justify-self: stretch;
  width: 100%;
  min-height: 390px;
  border: 1px solid rgba(63, 91, 127, 0.5);
  background:
    linear-gradient(rgba(64, 111, 166, 0.10) 1px, transparent 1px),
    linear-gradient(90deg, rgba(64, 111, 166, 0.10) 1px, transparent 1px),
    linear-gradient(150deg, rgba(19, 31, 49, 0.74), rgba(6, 9, 14, 0.46));
  background-size: 36px 36px, 36px 36px, auto;
  clip-path: polygon(0 6%, 6% 0, 100% 0, 100% 94%, 94% 100%, 0 100%);
  box-shadow: inset 0 1px rgba(140, 200, 255, 0.08), 0 20px 58px rgba(0, 0, 0, 0.22);
  opacity: 1;
}

.content-page .hero::before {
  content: "ARQIVEXA / WINDOWS 11\A\A EDITABLE ARCHIVE WORKSPACE\A .CFS  •  LZMA2  •  PROJFS\A\A EXPLORER-FIRST FILE ACCESS";
  white-space: pre;
  grid-column: 2;
  grid-row: 1;
  align-self: center;
  justify-self: center;
  z-index: 2;
  width: min(72%, 340px);
  padding: 1.45rem;
  border: 1px solid var(--blue-bright);
  background: linear-gradient(145deg, #122239, #0a1019 72%);
  box-shadow: 0 0 36px rgba(47, 129, 247, 0.18);
  color: #a8c9ef;
  font: 650 0.66rem/1.75 var(--font-geist-mono), monospace;
  letter-spacing: 0.08em;
  clip-path: polygon(0 0, 88% 0, 100% 12%, 100% 100%, 0 100%);
}

.content-page .steps-grid {
  gap: 1rem;
}

.content-page .step-card {
  border-color: var(--border);
  background: rgba(12, 17, 25, 0.78);
  box-shadow: inset 0 1px rgba(121, 183, 255, 0.06);
}

.content-page .step-card:hover {
  border-color: #3f648d;
  background: rgba(14, 23, 35, 0.88);
}

.home-page .section,
.content-page .section {
  scroll-margin-top: 90px;
}

.content-page .section {
  padding-top: 2.25rem;
  padding-bottom: 6.25rem;
}

.content-page .section-heading {
  margin-bottom: 2.6rem;
}

.home-page footer,
.content-page footer,
.error-page footer {
  width: min(calc(100% - 2rem), var(--max-width));
}

@media (max-width: 940px) {
  .home-page .hero,
  .content-page .hero {
    grid-template-columns: 1fr;
    gap: 3rem;
    min-height: auto;
    padding: 5.3rem 0 4.4rem;
  }

  .content-page .hero::after,
  .content-page .hero::before {
    display: none;
  }
}

@media (max-width: 680px) {
  .home-page .hero,
  .content-page .hero {
    padding: 4.5rem 0 3.8rem;
  }

  .content-page .hero h1 {
    font-size: clamp(2.8rem, 14vw, 4.4rem);
  }
}
'''
css_path.write_text(css + block, encoding="utf-8")
print("Appended unified visual system to website/styles.css")
