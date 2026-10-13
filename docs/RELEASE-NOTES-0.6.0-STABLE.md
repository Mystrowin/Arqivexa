# Arqivexa 0.6.0 Stable

Arqivexa 0.6.0 is a maintenance update to the accepted 0.5.0 release. It fixes a save-completion race that could leave a recent edit out of the next saved archive.

## Fixes

- Preserves an edit that arrives while a save is completing, including an edit whose file length and timestamp are unchanged.
- Keeps pending edits until the prepared replacement archive is committed and finalized successfully.
- Preserves mutation notifications that do not include a path, so the next save rescans the workspace.

The archive format, Explorer integration, recovery workflow, and Windows 11 x64 support scope remain the same. This maintenance update does not add transparent-folder replacement or a kernel driver.

## Verification status

The fresh core suite passed 46/46 checks, the portable package verifier passed 48/48 checks, and the 10,000-entry performance run passed. Independent installed acceptance for the 0.6.0 installer is still pending. See the [verification report](ACCEPTANCE-REPORT-0.6.0-STABLE.md) for the exact scope and limitations.

## Compatibility and safety

- Requires Windows 11 x64 and Windows Projected File System for Explorer mounting.
- Writable archives require local NTFS storage.
- The installer and signed executable names retain `CFS` because this maintenance build was produced before the public rebrand.
- The existing self-signed publisher certificate remains in use. Windows may show an untrusted-publisher or SmartScreen warning.
- Save and close other writers before unmounting. This fix does not establish a coherent snapshot across concurrent writers or make terminal unmount atomic.
- Keep independent backups. Arqivexa compresses files but does not encrypt them.

Copyright © 2026 Neeraj Pragnya Krishna Vasagiri. All rights reserved.
