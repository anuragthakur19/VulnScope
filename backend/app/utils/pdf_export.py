 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def export_to_pdf(report_data: dict, output_path: str):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 50

    def draw_line(text, indent=0, spacing=15, bold=False):
        nonlocal y
        if y < 50:
            c.showPage()
            y = height - 50
        if bold:
            c.setFont("Helvetica-Bold", 10)
        else:
            c.setFont("Helvetica", 10)
        c.drawString(50 + indent, y, text)
        y -= spacing

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Website Vulnerability Report")
    y -= 30
    c.setFont("Helvetica", 10)
    draw_line(f"Domain: {report_data.get('domain')}")
    draw_line(f"Scanned on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    draw_line(f"Final Verdict: {report_data.get('verdict')}", bold=True)
    draw_line(f"Score: {report_data['score']['score']}/100", bold=True)
    y -= 10

    # Deductions
    draw_line("Deductions:", bold=True)
    for reason in report_data["score"].get("deductions", []):
        draw_line(f"- {reason}", indent=15)

    y -= 10
    # Nmap Results
    draw_line("Open Ports:", bold=True)
    for port in report_data["nmap"].get("open_ports", []):
        line = f"{port['port']} | {port['service']} | {port['version']}"
        draw_line(line, indent=15)

    y -= 10
    # SSL
    ssl = report_data["ssl"]
    draw_line("SSL Information:", bold=True)
    for key in ["valid", "issuer", "subject", "expires_on"]:
        value = ssl.get(key, "N/A")
        draw_line(f"{key.capitalize()}: {value}", indent=15)

    y -= 10
    # HTTP Headers
    draw_line("Missing Security Headers:", bold=True)
    for h in report_data["headers"].get("missing", []):
        draw_line(f"- {h['header']}: {h['description']}", indent=15)

    y -= 10
    # Blacklist
    draw_line("Blacklist Check:", bold=True)
    for bl, status in report_data["blacklist"].items():
        draw_line(f"{bl}: {status}", indent=15)

    y -= 10
    # DNS
    draw_line("DNS Records:", bold=True)
    for rtype, value in report_data["dns"].items():
        if isinstance(value, list):
            draw_line(f"{rtype}: {', '.join(value)}", indent=15)
        else:
            draw_line(f"{rtype}: {value}", indent=15)

    y -= 10
    # GeoIP
    draw_line("Geolocation Info:", bold=True)
    geo = report_data.get("geoip", {})
    for field in ["country", "region", "city", "isp", "org"]:
        draw_line(f"{field.capitalize()}: {geo.get(field, 'N/A')}", indent=15)

    c.save()
