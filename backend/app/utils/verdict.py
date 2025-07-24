 
def generate_verdict(score_result: dict) -> str:
    score = score_result.get("score", 0)

    if score >= 90:
        return "Very Safe — no major vulnerabilities detected."
    elif score >= 75:
        return "Safe — minor improvements recommended."
    elif score >= 50:
        return "Moderate Risk — potential vulnerabilities found."
    elif score >= 30:
        return "Unsafe — several vulnerabilities detected."
    else:
        return "Dangerous — this website is highly vulnerable or malicious."
