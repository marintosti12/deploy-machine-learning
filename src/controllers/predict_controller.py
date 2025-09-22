from fastapi import APIRouter, Depends, HTTPException

from config.db import get_db
from models.ml import MLModel 

# Schemas
from models.ml_inputs import MLInput
from models.ml_output import MLOutput

import pandas as pd
from model_loader import load_model           
from features import compute_features
from schemas.PredictItemResult import PredictItemResult
from schemas.PredictResponse import PredictResponse
from schemas.PredictRequest import PredictRequest
from sqlalchemy.orm import Session

router = APIRouter(prefix="/predict", tags=["inference"])

LABELS = {
    "0": "reste_dans_l_entreprise",
    "1": "parti_de_l_entreprise",
}

@router.post("/", response_model=PredictResponse)
@router.post("/", response_model=PredictResponse)
def batch_predict(payload: PredictRequest, db: Session = Depends(get_db)):
    row = (
        db.query(MLModel)
          .filter(MLModel.name == payload.model_name)
          .first()
    )

    # --- stocker les inputs
    objs = [MLInput(**x.model_dump()) for x in payload.inputs]
    db.add_all(objs)
    db.commit()

    if not row or getattr(row, "is_active", True) is False:
        raise HTTPException(status_code=404, detail="Modèle introuvable ou inactif")

    try:
        m = load_model(payload.model_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chargement du modèle '{payload.model_name}' impossible: {e}")

    try:
        df = pd.DataFrame([x.model_dump() for x in payload.inputs])
        X = compute_features(df)

        results: list[PredictItemResult] = []

        probas = m.predict_proba(X)
        classes = getattr(m, "classes_", None)

        for idx, p in enumerate(probas):
            i = int(p.argmax())
            key = str(classes[i]) if classes is not None else str(i)
            label = LABELS.get(key, key)

            pred = PredictItemResult(label=label, proba=float(p[i]))
            results.append(pred)

            print(objs[idx].id)
            db.add(
                MLOutput(
                    input_id=objs[idx].id,
                    prediction=label,
                    prob=float(p[i]),
                )
            )

        db.commit()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erreur pendant la prédiction: {e}")

    return PredictResponse(
        model_name=payload.model_name,
        results=results,
    )


