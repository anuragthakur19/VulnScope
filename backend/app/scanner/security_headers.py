# app/scanner/security_headers.py

import requests

def check_security_headers(domain: str) -> dict:
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "https://" + domain  # Default to HTTPS

    try:
        response = requests.get(domain, timeout=5)
        headers = response.headers

        important_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        missing = [header for header in important_headers if header not in headers]

        return {
            "present": [h for h in important_headers if h in headers],
            "missing": missing
        }

    except Exception as e:
        return {"error": str(e)}
