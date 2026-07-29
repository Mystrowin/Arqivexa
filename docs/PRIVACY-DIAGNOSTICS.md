# CFS Privacy and Diagnostics Policy

Last updated: 2026-07-27

CFS is designed to work locally. Archive contents are not uploaded for normal compression, mounting, extraction, saving, recovery, or update checks.

## Local diagnostics

CFS stores local diagnostic logs under `%LOCALAPPDATA%\CFS\Logs`. Logs record the product version, Windows version, stable component/error information, and sanitized exception details. Archive paths and mounted-workspace paths are replaced with non-reversible identifiers. CFS does not intentionally record archive contents, filenames, account names, credentials, access tokens, PFX material, or certificate private keys in diagnostic logs.

The Settings window controls **Allow sanitized failure reports when reporting is configured**. Setup selects this option by default; the user can clear it during setup or at any time in Settings. Disabling it never blocks CFS operations.

## Failure reporting

When a reporting endpoint is configured for a released build, CFS may send only a bounded structured diagnostic record after consent. The record is limited to 64 KiB and may contain a stable error code and component, CFS version and Windows build, operation phase, and a scrubbed stack trace.

It must not contain paths, filenames, archive contents, credentials, account names, certificate material, or stored IP addresses. Reporting failures are nonfatal and never prevent local CFS work.

The diagnostics service retains accepted reports for no more than 90 days. Users can disable reporting in Settings and may request deletion of a submitted report using its report ID.

## Updates and external links

CFS update checks retrieve only the public update manifest over HTTPS. An update is never downloaded or launched without explicit user approval. Downloaded installers must pass the manifest SHA-256 check and match the pinned CFS publisher certificate before CFS offers elevation.

The public support channel is the CFS GitHub Issues page. Information submitted to a public issue is governed by GitHub and should be reviewed for private information before submission.

## Contact

For privacy questions or a future report-deletion request, open an issue at <https://github.com/Mystrowin/CFS/issues>.
