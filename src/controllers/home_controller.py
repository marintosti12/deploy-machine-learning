from fastapi import APIRouter, Depends, HTTPException
from config.db import get_db       
from models.ml import MLModel           
from sqlalchemy.orm import Session

router = APIRouter() 

@router.get("/", tags=["models"])
def list_ml_models(db: Session = Depends(get_db)):
    try:
        rows = (
            db.query(MLModel)
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
