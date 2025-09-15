from fastapi import APIRouter, HTTPException
from config.db import SessionLocal       
from models.ml import MLModel           

router = APIRouter() 

@router.get("/", tags=["models"])
def list_ml_models():
    try:
        with SessionLocal() as s:  
            rows = (
                s.query(MLModel)
                 .order_by(MLModel.created_at.desc())
                 .all()
            )
            return [
                {
                    "id": str(r.id),
                    "name": r.name,
                    "description": r.description,
                    "created_at": r.created_at.isoformat() if r.created_at else None,
                    "is_active": r.is_active,
                }
                for r in rows
            ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
