# CFS 0.5.0 Stable acceptance report

Status: **Accepted for public Stable publication.** The exact signed candidate,
automated release evidence, reproducible-source run, and user-authorized
current-account installed workflow have passed.

The user explicitly declined switching into the prepared dedicated account and
authorized isolated testing under the current Windows account. The accepted
installed run therefore used the production per-user installer scope. It moved
the existing CFS profile tree aside, verified and exercised the installed
registrations and exact registered commands, observed Explorer opening the
projected mount, uninstalled the product, restored registry state without
changing Windows `UserChoice`, and restored the original profile tree to the
same SHA-256. Because the pre-existing `UserChoice` was deliberately preserved,
the report does not claim a double-click test; it records direct invocation of
the byte-exact registered open and close commands.

## Recorded local evidence

| Area | Evidence | Result |
| --- | --- | --- |
| Core archive, ProjFS, CFS1/CFS2, hostile input, diagnostics | `tests/Cfs.Core.Tests` | 43/43 passed |
| Archive creation, selection requests, ShellNew, CFS2, extraction | `tests/Cfs.Creation.Tests` | 17/17 passed |
| Broker protocol, sessions, bounded IPC, operations, status snapshot | `tests/Cfs.Broker.Tests` | 22/22 passed |
| Automatic persistence, recovery transaction, lock and disk-space safety | `tests/Cfs.Persistence.Tests` | 16/16 passed |
| Recovery metadata, interrupted commit, explicit recovery disposition | `tests/Cfs.Recovery.Tests` | 11/11 passed |
| Close, unmount, cleanup, and dirty-flush behavior | `tests/Cfs.Close.Tests` | 9/9 passed |
| Native Windows 11 Explorer extension | Visual Studio x64 Release build | passed |
| Pre-signing installer syntax and payload staging | Inno Setup compilation of staged payload | passed |
| Compression regression comparison | `tools/Test-CfsPerformanceRegression.ps1` | passed: creation -3.059%, save -80.679% versus the accepted 0.4 workload |
| 10,000-entry Explorer listing | `dist/CFS-0.5.0-Stable-performance.json` | 0.992 seconds; under the 2-second gate |
| Large-operation memory | `dist/CFS-0.5.0-Stable-performance.json` | 235,515,904 bytes; under the 512 MiB gate |
| Release package | successful final release-build log and `tools/Test-CfsBetaPackage.ps1` | 48/48 passed; retired `Cfs.App` absent |
| Release inputs and SBOM generation | local builder-input validation and `tools/New-CfsSbom.ps1` | passed; CycloneDX 1.5 SBOM with 492 artifact records |
| CFS-owned signatures and timestamping | `CFS-0.5.0-Stable-signatures.json` | 8/8 payloads carry the pinned leaf certificate and DigiCert RFC 3161 timestamp |
| Tamper rejection | `dist/CFS-0.5.0-Stable-tamper-verification.json` | passed; modified setup rejected by SHA-256 and Authenticode |
| Existing-scope conflict safety | `dist/CFS-0.5.0-Stable-scope-conflict.json` | passed; exact setup refused side-by-side installation without changing the existing installation, processes, or session data |
| Diagnostics deployment and privacy contract | `dist/CFS-0.5.0-Stable-diagnostics-deployment.json` | live acceptance passed for validation, privacy rejection, deletion authorization, rate limiting, and 90-day retention |
| Offline signing recovery material | offline PFX backup outside the repository and release output | present; the release builder accepted the external backup prerequisite |
| Dedicated-account acceptance preparation | `tools/Prepare-CfsInstalledAcceptance.ps1` preparation record | passed; exact setup staged, owned 0.4 installation removed after backup, restore point recorded, session data unchanged, and dedicated account created |
| Publishable source reproducibility | external `CFS-0.5.0-Stable-source-reproducibility.json` | passed: 118/118 from the exact source ZIP; 889 files and 91 directories unchanged; temporary artifacts cleaned |
| Installed per-user Explorer workflow | `dist/CFS-0.5.0-Stable-current-account-acceptance-summary.json` | passed: exact signed setup, ShellNew, mount, session reuse, ordinary writes, atomic replace/move, commit, close, reopen, persistence, uninstall, registry restoration, zero residue, and original profile restoration |

## Exact signed candidate

| Artifact | SHA-256 |
| --- | --- |
| `CFS-0.5.0-Stable-Setup.exe` | `b89a650b96e3dfe981a28b2ff13888cbfef30ec8873f2af77955a1ead98fb46a` |
| `CFS-0.5.0-Stable-win-x64.zip` | `d38eb051d036b747cf09daaf162773662afbbd77a2269652eaa58aedc5908119` |
| `CFS-0.5.0-Stable-sbom.cdx.json` | `1b1a4a820b94078dc4d4bb6fd035d9cf91a43ba55f11bd2bc36becdaf065cf74` |
| `CFS-CodeSigning.cer` | `9f8247e52567c6c9bae25666bb40a8d889c4d0b2b639a6065f0d4507d6d29bd6` |
| `CFS-0.5.0-Stable-signatures.json` | `570936737d7fa90fdf2204db4ee3fae242947b650a1823907118d0056d301f86` |
| `update.json` | `fc76af1a8e5ccbc756a1c85fc46e46643a852da0b2f2d8b46e4125a5f856a9` |

The source ZIP is created after this report is embedded. Its final SHA-256 is
therefore recorded in the external `SHA256SUMS.txt` instead of circularly
embedding the archive's own digest inside itself.

Pinned signer:

- Leaf thumbprint: `3128136912D1492C0727365B62D833C54C9B0CF4`
- Public-key SHA-256: `ff0906e14f8c546bf139217ed024eef448bd2ac35bc77c9fcb1ebeb7a5ae95ba`
- Subject: `CN=Neeraj Pragnya Krishna Vasagiri`
- Timestamp responder certificate thumbprint:
  `DD6230AC860A2D306BDA38B16879523007FB417E`

Because the publisher certificate is self-signed, Windows reports an untrusted
root until the user explicitly trusts the exact leaf certificate. The release
checks separately verify the embedded signature, pinned signer identity,
timestamp, artifact hash, and tamper rejection.

## Exact evidence references

- Consolidated automated result:
  `dist/CFS-0.5.0-Stable-automated-acceptance-summary.json`
- Publishable-source verification runner:
  `tools/Test-CfsPublishableSource.ps1`; its final result and the source ZIP
  digest are recorded externally to avoid changing the source archive they
  attest to.
- Sanitized installed acceptance:
  `dist/CFS-0.5.0-Stable-current-account-acceptance-summary.json`
- Full installed and profile-restoration evidence remains local because it
  contains machine and account details. The sanitized summary pins both local
  evidence files by SHA-256.
- Performance result: `dist/CFS-0.5.0-Stable-performance.json`
- Direct 0.4 comparison: `dist/CFS-0.5.0-Stable-performance-1000.json`
- Compression regression result: `dist/CFS-0.5.0-Stable-performance-regression.json`
- Release source: `tools/Build-CfsPublishableRelease.ps1`
- Installed artifact acceptance harness: `tools/Test-CfsInstalledShellAcceptance.ps1`
- Exact setup tamper result: `dist/CFS-0.5.0-Stable-tamper-verification.json`
- Existing-scope safety result: `dist/CFS-0.5.0-Stable-scope-conflict.json`
- Live diagnostics result: `dist/CFS-0.5.0-Stable-diagnostics-deployment.json`
- Privacy policy: `docs/PRIVACY-DIAGNOSTICS.md`
- Release notes: `docs/RELEASE-NOTES-0.5.0-STABLE.md`

## Release approval

The accepted installed run used the exact setup SHA-256 recorded above. The
self-signed leaf remained untrusted by Windows, as disclosed, while the embedded
signature, pinned signer thumbprint, pinned public-key hash, and RFC 3161
timestamp were independently verified. No `Cfs.App` process was launched.

The source ZIP and checksums were regenerated with this final report and
tooling, source reproducibility passed again, and the curated GitHub export
passed. Older installers must be withdrawn rather than replaced in place.

Copyright © 2026 Neeraj Pragnya Krishna Vasagiri. All rights reserved.
