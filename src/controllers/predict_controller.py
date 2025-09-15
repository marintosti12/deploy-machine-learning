# src/controllers/predict_controller.py
from fastapi import APIRouter, HTTPException

from config.db import SessionLocal
from models.ml import MLModel 

# Schemas
from models.ml_inputs import MLInput

import pandas as pd
from model_loader import load_model           
from features import compute_features
from schemas.PredictItemResult import PredictItemResult
from schemas.PredictResponse import PredictResponse
from schemas.PredictRequest import PredictRequest

router = APIRouter(prefix="/predict", tags=["inference"])

# (optionnel) mapping lisible des classes
LABELS = {
    "0": "reste_dans_l_entreprise",
    "1": "parti_de_l_entreprise",
}

# --------- Route ----------
@router.post("/", response_model=PredictResponse)
def batch_predict(payload: PredictRequest):
    with SessionLocal() as s:
        row = (
            s.query(MLModel)
             .filter(MLModel.name == payload.model_name)
             .first()
        )

        objs = [MLInput(**x.model_dump()) for x in payload.inputs]
        s.add_all(objs)
        s.commit()


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
        for p in probas:
            i = int(p.argmax())
            key = str(classes[i]) if classes is not None else str(i)
            label = LABELS.get(key, key)
            results.append(PredictItemResult(label=label, proba=float(p[i])))

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur pendant la prédiction: {e}")

    return PredictResponse(
        model_name=payload.model_name,
        results=results,
    )
