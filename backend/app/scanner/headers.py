 
import requests

def check_headers(domain: str):
    url = f"https://{domain}"
    required_headers = {
        "Content-Security-Policy": "Protects against XSS attacks",
        "Strict-Transport-Security": "Enforces HTTPS",
        "X-Frame-Options": "Prevents clickjacking",
        "X-Content-Type-Options": "Prevents MIME-sniffing",
        "Referrer-Policy": "Controls how referrer info is sent",
        "Permissions-Policy": "Restricts browser features"
    }

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        missing = []

        for header, purpose in required_headers.items():
            if header not in headers:
                missing.append({
                    "header": header,
                    "description": purpose
                })

        return {
            "present": dict(headers),
            "missing": missing
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
