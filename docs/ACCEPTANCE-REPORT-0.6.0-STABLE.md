# Arqivexa 0.6.0 Stable verification report

## Verified checks

| Check | Result | Scope |
| --- | --- | --- |
| Save-completion regression | PASS | The original 0.5 behavior failed when a same-size, same-timestamp edit arrived during save completion. The 0.6 candidate preserves the edit for the next save. |
| Core tests | PASS, 46/46 | Fresh Release run of `tests/Cfs.Core.Tests`. |
| Portable package verification | PASS, 48/48 | Required payloads, version identity, localization smoke check, command registration dry runs, and ZIP-to-folder SHA-256 comparison. |
| Performance run | PASS | 10,000-entry workload; 1.825 second first listing, 204,156,928-byte peak working set, unchanged-block reuse and cleanup passed. |
| Installer identity | MATCH | `CFS-0.6.0-Stable-Setup.exe`, 50,736,200 bytes, SHA-256 `17c3e0e6c6ef3a259369ef3d751573b599d0d10414efaafbd8ed655da028ad57`. |

## Pending acceptance

Independent fresh-install acceptance of the 0.6.0 installer has not been completed. The package checks do not exercise installation, Explorer registration, archive creation, save/reopen behavior after installation, uninstall, or system cleanup. This report does not claim those results.

The installer and executable payloads are signed and RFC 3161 timestamped with the existing CFS publisher certificate. Windows reports an untrusted root for that self-signed certificate; no trust-store change is included. The signer thumbprint is `3128136912D1492C0727365B62D833C54C9B0CF4`.

## Scope limits

The fix preserves edits for a subsequent save. It does not prove coherent snapshots across concurrent writers or atomic terminal unmount. The 0.6.0 maintenance package introduces no transparent-folder driver feature and does not change the accepted Windows 11 x64/local-NTFS support scope.

Keep other writers closed before unmounting and maintain independent backups of important archives.
