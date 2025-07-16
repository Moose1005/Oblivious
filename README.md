# Oblivious

Oblivis is a **cross-platform** Python tool for secure file deletion and basic system privacy auditing on Windows and Arch Linux. It features:

- **Secure Wipe:** Permanently overwrite files/directories with random data (multiple passes) before deletion.

- **Journal Scan (Stub):** Example logic for scanning NTFS or ext4 journals for remnants of deleted files.

- **Quick Audit:** A simple privacy/security check (e.g. firewall status, telemetry) on fresh Windows or Arch installs.




## Requirements
- Python 3.11 or higher (**Will break if not installed beforehand**)
- **Windows users**: install `windows-curses`
- **Arch users**: *patience* 
- Standard library modules only otherwise (no heavy GUI libraries).

## Installation
    Download and run 
        ~should be put in the documents folder or downloads folder for ease of use~
