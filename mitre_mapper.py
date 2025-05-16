def map_to_mitre(event_type):
    mitre_map = {
        "powershell": "Execution > PowerShell",
        "dns exfil": "Command and Control > Exfiltration over DNS",
        "lsass dump": "Credential Access > OS Credential Dumping"
    }
    return mitre_map.get(event_type.lower(), "Unknown Technique")
