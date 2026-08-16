# Arqivexa 0.5.0 Stable known limitations

- Arqivexa is not a backup system and must not be the only copy of any important file.
- Windows 11 x64 is the supported target.
- Default Explorer mounting requires enabled `Client-ProjFS` and writable archives on local NTFS storage.
- Compatibility Mode is explicit full extraction, not on-demand mounting, and can require time and disk space comparable to the uncompressed archive.
- Compatibility with every Windows application is not guaranteed. Previews, antivirus, indexing, memory mapping, and application access patterns can trigger hydration.
- Broker commits are automatic after a quiet period; a failed commit retains recoverable session data and must be resolved before the current release's **Close CFS** command can report success.
- Updates append changed data and manifests, so archives can grow. After closing the mounted workspace, use the current release's **Optimize CFS archive** command to transactionally remove obsolete archive history; optimization is currently manual rather than automatic.
- Compression is independent per-file LZMA2, not solid compression. A requested file must be decompressed as its own block before ranges are served.
- No encryption, password protection, deduplication, version history, cloud synchronization, permissions preservation, or multi-user coordination.
- Directory deletion is limited to empty folders through supported workflows.
- A failed cleanup can leave a preserved temporary mount that the user must close and retry safely.
- The public GitHub issue tracker is the support channel; reports are public and must be scrubbed of private information.
- The 0.5.0 installer uses the existing CFS self-signed publisher certificate and Windows SmartScreen may warn before the exact leaf certificate is trusted.

See [DATA-SAFETY.md](DATA-SAFETY.md) before storing important files and the
[0.5.0 Stable release notes](RELEASE-NOTES-0.5.0-STABLE.md) for the supported scope.
