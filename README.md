# Oblivious

Oblivious is a cross-platform Python tool for secure file deletion and basic system privacy auditing on Windows and Arch Linux.

## Features
- Securely overwrite files and directories (multiple passes) before deletion.
- Journaling scan stubs for NTFS and ext4.
- Quick system audit (firewall status, privacy tips).

## Requirements
- Python 3.11+
- **Windows users:** `pip install windows-curses`

## Installation
```bash
git clone https://github.com/Moose1005/Oblivious.git
cd Oblivious
pip install -r requirements.txt  # or pip install windows-curses on Windows
```

## Usage
```bash
python oblivious.py
```
Follow the on-screen menu to wipe files, scan journals, or audit your system.

## Versioning
Initial alpha release v0.1.0-alpha. Future releases will use semantic versioning and GitHub tags (v0.2.0-beta1, v1.0.0, etc.).

## License
MIT License
