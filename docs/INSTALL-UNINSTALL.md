# CFS 0.5.0 Stable installation and uninstall

## Recommended machine-wide setup

Run `CFS-0.5.0-Stable-Setup.exe`, approve the Windows administrator prompt when choosing an all-user install, and follow the setup wizard. Setup can install CFS for the current user or for all users, registers the command-client and broker-based Explorer workflow, adds archive-creation commands, and checks the `Client-ProjFS` Windows feature.

The Stable installer is signed with the exact CFS self-signed publisher certificate, but Microsoft SmartScreen can still display a warning before that certificate is explicitly trusted. Verify the published SHA-256 checksum before continuing.

Use Windows **Installed apps** to remove CFS. The uninstaller removes the file association only when it still points to this CFS installation and never deletes `.cfs` archives or `%LOCALAPPDATA%\CFS` user data.

## Portable install by extraction

If a complete portable package is provided, extract it to a writable local folder. Paths containing spaces are supported when commands remain quoted:

```powershell
& "$env:ProgramFiles\CFS\Cfs.CommandClient.exe" open "C:\path\to\archive.cfs"
```

Do not run only the executable from inside the ZIP and do not separate it from packaged native and managed dependencies.

## ProjFS prerequisite

The default **Open in Explorer** action requires Windows 11 x64 with `Client-ProjFS` enabled. Setup can request approval to enable **Windows Projected File System** and reports when Windows requires a restart. CFS reports unavailability and never silently activates full extraction.

## Register `.cfs` double-click

The packaged script registers the command client for the current user and supports quoted paths containing spaces:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Register-CfsFileAssociation.ps1" -CommandClientPath ".\Cfs.CommandClient.exe"
```

Registration writes under `HKCU\Software\Classes`; it does not require a machine-wide install.

## Reverse the file association

Close CFS, then use the packaged script to remove only the current-user keys created by CFS 0.5.0 Stable:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Register-CfsFileAssociation.ps1" -Unregister
```

The equivalent manual commands are:

```powershell
reg.exe delete "HKCU\Software\Classes\.cfs" /f
reg.exe delete "HKCU\Software\Classes\CFS.Archive" /f
```

If another application owned `.cfs` before testing, restore that application through its own association settings instead of assuming CFS knows the previous value.

## Uninstall the portable application

1. Save and unmount every open archive.
2. Confirm no CFS window or preserved mount is still in use.
3. Reverse the file association as above.
4. Delete the extracted CFS folder or ZIP.
5. Optionally remove `%LOCALAPPDATA%\CFS\Logs` and CFS diagnostic settings after retaining any logs needed for reports.

Uninstalling the application does not delete `.cfs` archives or user-created backups.
