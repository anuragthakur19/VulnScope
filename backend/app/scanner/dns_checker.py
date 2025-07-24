 
import dns.resolver

def check_dns(domain: str):
    results = {}

    try:
        # A record (IPv4)
        a_records = dns.resolver.resolve(domain, 'A')
        results['A'] = [r.to_text() for r in a_records]
    except Exception as e:
        results['A'] = f"Error: {str(e)}"

    try:
        # AAAA record (IPv6)
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        results['AAAA'] = [r.to_text() for r in aaaa_records]
    except Exception as e:
        results['AAAA'] = f"Error: {str(e)}"

    try:
        # MX record (mail server)
        mx_records = dns.resolver.resolve(domain, 'MX')
        results['MX'] = [r.to_text() for r in mx_records]
    except Exception as e:
        results['MX'] = f"Error: {str(e)}"

    try:
        # NS record (name servers)
        ns_records = dns.resolver.resolve(domain, 'NS')
        results['NS'] = [r.to_text() for r in ns_records]
    except Exception as e:
        results['NS'] = f"Error: {str(e)}"

    try:
        # TXT record (SPF, DMARC etc.)
        txt_records = dns.resolver.resolve(domain, 'TXT')
        results['TXT'] = [r.to_text() for r in txt_records]
    except Exception as e:
        results['TXT'] = f"Error: {str(e)}"

    return results
