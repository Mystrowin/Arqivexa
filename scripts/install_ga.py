from pathlib import Path

ROOT = Path("website")
MEASUREMENT_ID = "G-V7BKF7BJY9"
TAG = f'''\n  <!-- Google tag (gtag.js) -->\n  <script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>\n  <script>\n    window.dataLayer = window.dataLayer || [];\n    function gtag(){{dataLayer.push(arguments);}}\n    gtag('js', new Date());\n    gtag('config', '{MEASUREMENT_ID}');\n  </script>\n'''

changed = []
for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()
    # Skip webmaster verification files or other .html files that are not real pages.
    if "<html" not in lower and "<!doctype" not in lower:
        continue
    if MEASUREMENT_ID in text:
        continue
    head_pos = lower.find("<head>")
    if head_pos == -1:
        raise SystemExit(f"Missing <head> in {path}")
    insert_at = head_pos + len("<head>")
    text = text[:insert_at] + TAG + text[insert_at:]
    path.write_text(text, encoding="utf-8")
    changed.append(path.name)

print(f"Installed {MEASUREMENT_ID} on {len(changed)} pages: {', '.join(changed)}")
