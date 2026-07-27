# CFS 0.4.0 Beta release notes

## Explorer-first archive creation

CFS archives can be created, opened, edited, closed, and maintained without opening or depending on `Cfs.App`.

- Explorer workspaces now use readable, identity-qualified folder names while preserving access to older recovery paths.
- **Optimize CFS archive** transactionally removes obsolete append history without recompressing live blocks.
- Optimize, extract, compress, and other long operations use bounded progress and cancellation handling.
- Explorer verbs enforce their supported selection model and continue to launch the small command client rather than loading archive code into `explorer.exe`.
- **New → CFS Compressed Folder** and **Create empty CFS archive here** create structurally valid archives through the production `create-empty` path; **Compress to CFS** uses the production compression path.

## Archive integrity and recovery

- Candidate archives are validated before replacement.
- The previous valid archive is retained as a same-volume backup through replacement verification.
- A failed post-replacement validation restores and validates the byte-identical backup; ambiguous failures preserve recovery evidence.
- Broker startup and exception logging are best-effort, so a temporarily locked diagnostic log cannot suppress a broker response.
- Optimization refuses active mounted sessions and external archive changes.

## Safety and compatibility

- The supported release target is Windows 11 x64 with Windows Projected File System enabled.
- Normal Explorer workflows do not require `Cfs.App`; it remains available for diagnostics and settings.
- The installer is currently unsigned and Windows may display a SmartScreen warning.
- CFS 0.4.0 Beta remains experimental Windows software. Keep an independently accessible backup of important files and use the beta with non-critical data.
