 
from sqlalchemy.orm import Session
from app.database.models import ScanResult
import json

def save_scan_result(db: Session, domain: str, result: dict):
    db_result = ScanResult(
        domain=domain,
        score=result["score"]["score"],
        verdict=result["verdict"],
        raw_data=json.dumps(result)
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_scan_results(db: Session, limit: int = 10):
    return db.query(ScanResult).order_by(ScanResult.id.desc()).limit(limit).all()
