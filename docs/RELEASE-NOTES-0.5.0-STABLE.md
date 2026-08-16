# Arqivexa 0.5.0 Stable release notes

**Arqivexa 0.5.0 Stable** is the renamed public release of the build originally published as **CFS 0.5.0 Stable**. The signed 0.5.0 binaries and compatibility identifiers are unchanged by the rebrand. This release replaces the legacy application-first workflow with Explorer-first archive creation, browsing, editing, extraction, and recovery.

## Explorer-first archive creation

- Create a `.cfs` archive from one folder or regular files selected from one directory through the current build's **Compress to CFS** command. Mixed selections and special file system objects are rejected with an explanation.
- The command client owns the Save dialog, naming, compression preference, progress, cancellation, destination confirmation, and reveal-after-success workflow. Create or open archives without opening or depending on `Cfs.App`; Explorer does not load archive code. **Create empty CFS archive here** uses the production `create-empty` path.
- Double-clicking an archive opens its ProjFS workspace. Repeated opens reuse its writable session instead of creating competing writers.
- Windows 11 receives a primary compression action, a compact archive submenu, and classic **Show more options** fallbacks.
- The in-process extension is limited to receiving selections, starting the command client, and reading the bounded broker status snapshot. Dirty and recovery-required archive or mount roots can receive a nonblocking status overlay; Explorer never waits on broker IPC for that status.

## Safer persistence and recovery

- Ordinary mounted edits are automatically saved after a quiet period, while explicit commit, discard, close, and recovery actions retain distinct behavior.
- Arqivexa preserves unchanged compressed blocks during projected saves. Clean ProjFS entries reuse their committed blocks; changed entries are read through the provider with sharing checks so partially written files are not committed.
- Arqivexa keeps a validated same-volume predecessor until a candidate has been validated, atomically promoted, reopened, and validated again.
- External archive identity changes, write conflicts, disk-space failures, and interrupted commits preserve pending state rather than silently overwriting data. Recovery remains explicit: recover, discard, inspect the location, or cancel.
- CFS1 remains supported. CFS2 provides independently checksummed 64 MiB LZMA2 chunks when a streamed large entry requires it. These are archive-format identifiers and retain the CFS names.

## Safety and compatibility

- Writable sessions are limited to local NTFS. Mark-of-the-Web archives and corrupted archives do not mount writable; read-only extraction remains an explicit fallback.
- The Stable package uses the existing CFS RSA-3072 self-signed leaf certificate, RFC 3161 timestamping, signer/hash inventory, a public certificate, update manifest, SBOM, and checksums.
- Windows can still display Unknown Publisher or SmartScreen before a user explicitly trusts the exact publisher certificate. Arqivexa never installs a general root certificate authority.
- Optional failure reporting sends only sanitized structured diagnostic data when a configured reporting endpoint is available. It can be disabled or its installation identifier reset from Settings.

## Requirements and known boundaries

- Target: Windows 11 x64, local NTFS, with Projected File System enabled.
- `.cfs` archives are not encrypted. Use Windows access controls and independent backups where confidentiality or disaster recovery matters.
- Keep an independent backup of important files. Arqivexa's retained previous version protects the most recent transaction boundary but is not a substitute for a separate backup.

Copyright © 2026 Neeraj Pragnya Krishna Vasagiri. All rights reserved.
