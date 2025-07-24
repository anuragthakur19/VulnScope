# app/scanner/verdict.py

def generate_verdict(nmap_result, header_result):
    import json

    # Collect issues based on scan results
    issues = []

    # Check for open ports
    if nmap_result.get("open_ports"):
        for port in nmap_result["open_ports"]:
            issues.append({
                "description": f"Open port {port['port']} running {port['service']}",
                "severity": "Medium" if port["service"] not in ["http", "https"] else "Low"
            })

    # Check for missing security headers
    if isinstance(header_result, dict):
        missing_headers = header_result.get("missing", [])
        for header in missing_headers:
            issues.append({
                "description": f"Missing security header: {header}",
                "severity": "High" if "Strict-Transport-Security" in header else "Medium"
            })

    # Severity scoring
    score = 0
    for issue in issues:
        severity = issue.get("severity", "")
        if severity == "Critical" or severity == "High":
            score += 3
        elif severity == "Medium":
            score += 2
        elif severity == "Low" or severity == "Info":
            score += 1

    if score >= 9:
        verdict = "High Risk"
    elif score >= 5:
        verdict = "Moderate Risk"
    else:
        verdict = "Low Risk"

    return score, verdict
