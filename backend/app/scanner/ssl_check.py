 
import ssl
import socket
from datetime import datetime

def check_ssl(domain: str):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(5)
            s.connect((domain, 443))
            cert = s.getpeercert()

        issuer = dict(x[0] for x in cert.get("issuer", []))
        subject = dict(x[0] for x in cert.get("subject", []))
        not_after = cert.get("notAfter")
        expiry_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")

        return {
            "valid": True,
            "issuer": issuer.get("organizationName", "Unknown"),
            "subject": subject.get("commonName", "Unknown"),
            "expires_on": expiry_date.strftime("%Y-%m-%d"),
            "expired": expiry_date < datetime.utcnow()
        }

    except ssl.SSLError as e:
        return {"valid": False, "error": "SSL error: " + str(e)}
    except socket.timeout:
        return {"valid": False, "error": "Connection timed out"}
    except Exception as e:
        return {"valid": False, "error": str(e)}
