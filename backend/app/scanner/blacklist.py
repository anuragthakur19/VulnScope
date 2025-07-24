 
import socket

# DNSBLs (public blacklists)
DNSBL_SERVERS = [
    "zen.spamhaus.org",         # widely used spam/malware DB
    "bl.spamcop.net",           # spam/malware sender DB
    "dnsbl.sorbs.net",          # security blacklist
    "b.barracudacentral.org",   # spam reputation DB
]

def check_blacklists(domain: str):
    results = {}

    try:
        ip = socket.gethostbyname(domain)
        reversed_ip = '.'.join(reversed(ip.split('.')))

        for bl in DNSBL_SERVERS:
            query = f"{reversed_ip}.{bl}"
            try:
                socket.gethostbyname(query)
                results[bl] = "Listed"
            except socket.gaierror:
                results[bl] = "Not Listed"
    except Exception as e:
        return {"error": f"DNS lookup failed: {str(e)}"}

    return results
