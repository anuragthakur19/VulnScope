 
import requests

API_KEY = "fd0407ad70b38f1df79a7adb15fb6d1d918a050a1fb93885ca65294404332b0c"
BASE_URL = "https://www.virustotal.com/api/v3/domains/"

def check_virustotal(domain: str):
    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(
            f"{BASE_URL}{domain}",
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return {"error": f"VirusTotal API failed: {response.status_code}"}

        data = response.json()
        stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        reputation = data.get("data", {}).get("attributes", {}).get("reputation", 0)
        categories = data.get("data", {}).get("attributes", {}).get("categories", {})

        return {
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0),
            "undetected": stats.get("undetected", 0),
            "reputation_score": reputation,
            "categories": categories
        }

    except Exception as e:
        return {"error": str(e)}
