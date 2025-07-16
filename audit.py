import platform, subprocess

def quick_audit():
    os_name = platform.system()
    print(f"Performing quick system audit on {os_name}...\n")
    if os_name == 'Windows':
        try:
            result = subprocess.run(
                ["netsh", "advfirewall", "show", "allprofiles"],
                capture_output=True, text=True)
            status = result.stdout
            if "ON" in status:
                print(" - Windows Firewall is ENABLED.")
            else:
                print(" - Windows Firewall may be DISABLED. Consider enabling it.")
        except Exception:
            print(" - Unable to query firewall status. (Run as Administrator?)")
        print(" - Tip: Windows collects telemetry by default; consider adjusting privacy settings.")
    else:
        print(" - Arch Linux has no built-in telemetry; ensure installed software is trusted.")
        try:
            ufw_status = subprocess.run(
                ["ufw", "status"], capture_output=True, text=True)
            if "Status: active" in ufw_status.stdout:
                print(" - UFW firewall is active.")
            else:
                print(" - UFW firewall is INACTIVE. Consider enabling it.")
        except FileNotFoundError:
            print(" - UFW not installed; consider using a firewall (ufw/iptables).")
    print("\nAudit complete.")