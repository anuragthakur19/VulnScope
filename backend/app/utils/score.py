 
def calculate_score(nmap, ssl, headers, blacklist, dns):
    score = 100
    deductions = []

    # --- Nmap Penalty ---
    open_ports = nmap.get("open_ports", [])
    risky_ports = [p for p in open_ports if p["port"].startswith(("21", "23", "445", "3389"))]
    if risky_ports:
        score -= len(risky_ports) * 5
        deductions.append(f"Open risky ports: {', '.join([p['port'] for p in risky_ports])}")

    # --- SSL Penalty ---
    if not ssl.get("valid", False):
        score -= 20
        deductions.append("Invalid or expired SSL certificate")
    elif ssl.get("expired", False):
        score -= 10
        deductions.append("SSL certificate expired")

    # --- HTTP Headers Penalty ---
    if "missing" in headers:
        score -= len(headers["missing"]) * 3
        missing = ", ".join([h["header"] for h in headers["missing"]])
        deductions.append(f"Missing security headers: {missing}")

    # --- Blacklist Penalty ---
    if any(v == "Listed" for v in blacklist.values()):
        score -= 30
        listed_sources = [k for k, v in blacklist.items() if v == "Listed"]
        deductions.append(f"Blacklisted by: {', '.join(listed_sources)}")

    # --- DNS Record Penalty ---
    essential = ["A", "NS"]
    for record in essential:
        if isinstance(dns.get(record), str) and dns[record].startswith("Error"):
            score -= 5
            deductions.append(f"{record} record missing or broken")

    # Ensure score is in 0–100
    score = max(0, min(100, score))

    return {
        "score": score,
        "deductions": deductions
    }
