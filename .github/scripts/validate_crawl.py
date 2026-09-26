#!/usr/bin/env python3
"""Check the public crawl-entry, canonical, and internal-link contracts."""

import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Signals(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonicals, self.robots, self.links = [], [], []
        self.title, self.h1 = [], []
        self.in_title = self.in_h1 = False
        self.refresh = False

    def handle_starttag(self, tag, attrs):
        attrs = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "link" and "canonical" in attrs.get("rel", "").lower().split():
            self.canonicals.append(attrs.get("href", ""))
        if tag == "meta":
            if attrs.get("name", "").lower() in {"robots", "googlebot"}:
                self.robots.append(attrs.get("content", ""))
            self.refresh |= attrs.get("http-equiv", "").lower() == "refresh"
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        self.in_title |= tag == "title"
        if tag == "h1" and not self.h1:
            self.in_h1 = True

    def handle_endtag(self, tag):
        self.in_title &= tag.lower() != "title"
        self.in_h1 &= tag.lower() != "h1"

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.in_h1:
            self.h1.append(data)


def page_key(path):
    return "/" if path in {"", "/", "/index.html"} else path


def file_for(root, url_path):
    relative = unquote(url_path).lstrip("/")
    if not relative or relative.endswith("/"):
        relative += "index.html"
    target = (root / relative).resolve()
    if os.path.commonpath((str(root.resolve()), str(target))) != str(root.resolve()):
        raise ValueError("link escapes the site root")
    return target


def main():
    if len(sys.argv) != 3:
        print("usage: validate_crawl.py SITE_ROOT https://canonical-host", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    origin = sys.argv[2].rstrip("/")
    parts = urlsplit(origin)
    if parts.scheme != "https" or not parts.hostname:
        print("canonical origin must use HTTPS", file=sys.stderr)
        return 2
    host = parts.hostname.lower()
    errors = []

    robots = root / "robots.txt"
    if not robots.is_file():
        errors.append("robots.txt is missing")
    else:
        lines = robots.read_text(encoding="utf-8").splitlines()
        if not any(line.strip().lower() == "user-agent: *" for line in lines):
            errors.append("robots.txt has no default user-agent group")
        if any(re.match(r"^\s*disallow\s*:\s*/\s*$", line, re.I) for line in lines):
            errors.append("robots.txt blocks the entire site")
        sitemap_refs = [line.split(":", 1)[1].strip() for line in lines
                        if line.lower().startswith("sitemap:")]
        if f"{origin}/sitemap.xml" not in sitemap_refs:
            errors.append("robots.txt does not name the canonical sitemap")

    try:
        sitemap_root = ET.parse(root / "sitemap.xml").getroot()
        if sitemap_root.tag.rsplit("}", 1)[-1] != "urlset":
            errors.append("sitemap root is not urlset")
        urls = [node.text.strip() for node in sitemap_root.iter()
                if node.tag.rsplit("}", 1)[-1] == "loc" and node.text]
    except (ET.ParseError, OSError) as exc:
        urls = []
        errors.append(f"sitemap.xml cannot be parsed: {exc}")
    if not urls:
        errors.append("sitemap has no URLs")
    if len(urls) != len(set(urls)):
        errors.append("sitemap contains duplicate URLs")

    pages = {}
    for url in urls:
        parsed = urlsplit(url)
        if parsed.scheme != "https" or (parsed.hostname or "").lower() != host:
            errors.append(f"sitemap URL is not on the canonical HTTPS host: {url}")
            continue
        if parsed.query or parsed.fragment:
            errors.append(f"sitemap URL has a query or fragment: {url}")
        try:
            path = file_for(root, parsed.path)
        except ValueError as exc:
            errors.append(f"invalid sitemap URL {url}: {exc}")
            continue
        if not path.is_file():
            errors.append(f"sitemap URL has no matching file: {url}")
            continue
        signal = Signals()
        signal.feed(path.read_text(encoding="utf-8"))
        if signal.canonicals != [url]:
            errors.append(f"page does not have one matching self-canonical: {url}")
        directives = {part.lower() for value in signal.robots
                      for part in re.split(r"[,\s]+", value.strip()) if part}
        if "noindex" in directives or signal.refresh:
            errors.append(f"non-indexable or redirect page is in the sitemap: {url}")
        if not "".join(signal.title).strip() or not "".join(signal.h1).strip():
            errors.append(f"sitemap page needs a title and H1: {url}")
        pages[page_key(parsed.path)] = (url, path)

    inbound = {key: 0 for key in pages}
    for source in root.rglob("*.html"):
        signal = Signals()
        signal.feed(source.read_text(encoding="utf-8"))
        relative = source.relative_to(root).as_posix()
        source_url = f"{origin}/" if relative == "index.html" else f"{origin}/{relative}"
        source_key = page_key(urlsplit(source_url).path)
        for href in signal.links:
            target_url = urlsplit(urljoin(source_url, href))
            if target_url.scheme not in {"http", "https"} or not target_url.hostname:
                continue
            if target_url.hostname.lower() != host:
                continue
            if target_url.scheme != "https":
                errors.append(f"internal link is not HTTPS: {source} -> {href}")
                continue
            try:
                target = file_for(root, target_url.path)
            except ValueError as exc:
                errors.append(f"invalid internal link in {source}: {exc}")
                continue
            if not target.is_file():
                errors.append(f"broken internal link: {source} -> {href}")
                continue
            target_key = page_key(target_url.path)
            if source_key in pages and target_key in inbound and source_key != target_key:
                inbound[target_key] += 1

    for key, count in inbound.items():
        if key != "/" and not count:
            errors.append(f"sitemap page has no incoming HTML link: {pages[key][0]}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Crawlability checks passed: {len(urls)} sitemap pages, canonicals, and internal links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
