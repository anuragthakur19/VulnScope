# app/routes/scan_request.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.scanner.nmap_scanner import run_nmap_scan
from app.scanner.security_headers import check_security_headers
from app.scanner.geoip import geoip_lookup as get_geo_info
from app.scanner.verdict import generate_verdict
from app.database.models import ScanResult
from app.database.session import get_db

router = APIRouter()

class ScanRequest(BaseModel):
    domain: str

@router.post("/scan")
def scan_domain(request: ScanRequest):
    domain = request.domain
    print(f"Scanning domain: {domain}")

    try:
        # Run Nmap scan
        nmap_result = run_nmap_scan(domain)

        # Check security headers (fix URL if needed)
        url = domain if domain.startswith("http") else f"https://{domain}"
        header_result = check_security_headers(url)

        # Get geo info
        geo_result = get_geo_info(domain)

        # Generate verdict (fix: pass both results correctly)
        score, verdict = generate_verdict(nmap_result, header_result)

        # Build response
        full_result = {
            "domain": domain,
            "nmap": nmap_result,
            "headers": header_result,
            "geo": geo_result,
            "score": score,
            "verdict": verdict,
        }

        # Save to database
        db = next(get_db())
        scan_record = ScanResult(
            domain=domain,
            score=score,
            verdict=verdict,
            raw_data=str(full_result)
        )
        db.add(scan_record)
        db.commit()
        db.close()

        return full_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
