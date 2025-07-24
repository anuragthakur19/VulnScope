# app/scanner/nmap_scanner.py

import subprocess
import re

def run_nmap_scan(domain: str):
    try:
        result = subprocess.run(
            ["nmap", "-F", "-sV", domain],
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout
        print("=== RAW NMAP OUTPUT ===")
        print(output)

        open_ports = parse_nmap_output(output)

        return {
            "open_ports": open_ports,
            "raw_output": output
        }

    except subprocess.TimeoutExpired:
        return {"error": "Nmap scan timed out"}
    except Exception as e:
        return {"error": str(e)}

def parse_nmap_output(output: str):
    open_ports = []

    for line in output.splitlines():
        if "/tcp" in line and "open" in line:
            parts = re.split(r"\s+", line.strip())
            if len(parts) >= 3:
                port_info = {
                    "port": parts[0],
                    "state": parts[1],
                    "service": parts[2],
                    "version": " ".join(parts[3:]) if len(parts) > 3 else "unknown"
                }
                open_ports.append(port_info)

    return open_ports
