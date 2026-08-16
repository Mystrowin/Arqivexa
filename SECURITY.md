# Arqivexa security policy

Report ordinary reproducible bugs through the
[public issue tracker](https://github.com/Mystrowin/Arqivexa/issues).

Do not publish credentials, private archives, file contents, unredacted
personal paths, signing material, or an exploit that would put users at
immediate risk. For a sensitive report, request a private contact channel from
the project owner without including sensitive details in the public request.

Only download Arqivexa from the project website or the `Mystrowin/Arqivexa`
GitHub Releases page. Arqivexa 0.5.0 Stable publishes the installer, SHA-256
checksums, public leaf certificate, signature report, SBOM, and update manifest
together. Verify the checksum and signature report before running setup.

The 0.5.0 installer and shipped executable payloads are Authenticode-signed and
RFC 3161 timestamped with the existing CFS self-signed publisher certificate.
Windows can still show Unknown Publisher or Microsoft SmartScreen before that
exact leaf certificate is explicitly trusted. Arqivexa never installs a general
root certificate authority.

The public repository is an allowlisted documentation and release surface.
Implementation source is maintained privately.
