import platform, curses
from wipe_module import secure_delete, secure_delete_dir
from journal_scan import scan_ntfs_journal, scan_ext4_journal
from audit import quick_audit

def main(stdscr):
    stdscr.clear()
    os_name = platform.system()
    if os_name == 'Windows':
        stdscr.addstr(0, 0, "Oblivis - Windows Environment", curses.A_BOLD)
        stdscr.addstr(2, 0, "Note: Ensure 'windows-curses' is installed (pip install windows-curses)")
    else:
        stdscr.addstr(0, 0, "Oblivis - Linux Environment", curses.A_BOLD)
        stdscr.addstr(2, 0, "Arch Linux detected; core utilities assumed present.")
    stdscr.addstr(4, 0, "1. Secure file/directory wipe")
    stdscr.addstr(5, 0, "2. Journaling scan (stub)")
    stdscr.addstr(6, 0, "3. Privacy/audit scan")
    stdscr.addstr(7, 0, "Q. Quit")
    stdscr.refresh()
    while True:
        c = stdscr.getkey()
        if c in ['q', 'Q']:
            break
        elif c == '1':
            curses.endwin()
            path = input("Enter file or directory path to wipe: ")
            passes = int(input("Enter number of passes: "))
            if os.path.isdir(path):
                secure_delete_dir(path, passes)
            else:
                secure_delete(path, passes)
            input("Wipe complete. Press Enter to continue.")
            curses.wrapper(main)
            break
        elif c == '2':
            curses.endwin()
            if os_name == 'Windows':
                scan_ntfs_journal(input("Enter volume path (e.g., C:): "))
            else:
                scan_ext4_journal(input("Enter device path (e.g., /dev/sda1): "))
            input("Scan stub complete. Press Enter to continue.")
            curses.wrapper(main)
            break
        elif c == '3':
            curses.endwin()
            quick_audit()
            input("Audit complete. Press Enter to continue.")
            curses.wrapper(main)
            break

if __name__ == '__main__':
    curses.wrapper(main)
