 
import socket
import requests

def geoip_lookup(domain: str):
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)

        if response.status_code != 200:
            return {"error": f"GeoIP lookup failed: {response.status_code}"}

        data = response.json()

        return {
            "ip": ip,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "timezone": data.get("timezone"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "asn": data.get("as"),
        }

    except Exception as e:
        return {"error": str(e)}
