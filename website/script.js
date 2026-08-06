const copyButton = document.querySelector("#copy-checksum");

if (copyButton) {
  copyButton.addEventListener("click", async () => {
    const checksum = copyButton.dataset.checksum;
    const label = copyButton.querySelector(".copy-label");
    const icon = copyButton.querySelector(".copy-icon");

    try {
      await navigator.clipboard.writeText(checksum);
      label.textContent = "Copied";
      icon.textContent = "✓";

      window.setTimeout(() => {
        label.textContent = "Copy SHA-256";
        icon.textContent = "⧉";
      }, 1800);
    } catch {
      label.textContent = "Copy failed";
    }
  });
}

const preserveCfsText = [
  "CFS-0.5.0-Stable-Setup.exe",
  "CFS 0.1–0.4",
  "CFS 0.1-0.4",
  ".cfs",
  "ARCHIVE.CFS",
  "WORKSPACE.CFS",
];

function rebrandText(text) {
  if (!text || preserveCfsText.some((value) => text.includes(value))) {
    return text;
  }

  return text
    .replaceAll("Compressed File System", "Editable Archive Workspace")
    .replaceAll("CFS 0.5.0 Stable", "Arqivexa 0.5.0 Stable")
    .replaceAll("CFS 0.5 Stable", "Arqivexa 0.5 Stable")
    .replaceAll("CFS 0.5.0", "Arqivexa 0.5.0")
    .replaceAll("CFS archives", "Arqivexa archives")
    .replaceAll("CFS archive", "Arqivexa archive")
    .replaceAll("CFS installer", "Arqivexa installer")
    .replaceAll("CFS reports", "Arqivexa reports")
    .replaceAll("CFS checks", "Arqivexa checks")
    .replaceAll("CFS compresses", "Arqivexa compresses")
    .replaceAll("CFS:", "Arqivexa:")
    .replaceAll("CFS", "Arqivexa");
}

document.title = rebrandText(document.title);

for (const meta of document.querySelectorAll("meta[content]")) {
  const property = meta.getAttribute("property") || meta.getAttribute("name") || "";
  if (/title|description|site_name|image:alt|application-name/i.test(property)) {
    meta.content = rebrandText(meta.content);
  }
}

for (const node of document.querySelectorAll("body *")) {
  if (node.children.length === 0 && node.textContent) {
    node.textContent = rebrandText(node.textContent);
  }

  for (const attribute of ["aria-label", "title", "alt"]) {
    if (node.hasAttribute(attribute)) {
      node.setAttribute(attribute, rebrandText(node.getAttribute(attribute)));
    }
  }
}

for (const link of document.querySelectorAll('a[href="https://mystrowin.github.io/CFS/"], a[href="https://mystrowin.github.io/CFS/#download"]')) {
  link.href = link.href.endsWith("#download")
    ? "https://arqivexa.mystrowin.com/#download"
    : "https://arqivexa.mystrowin.com/";
}
