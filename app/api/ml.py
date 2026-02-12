from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import ml_predictions as crud_ml
from ..schemas import MLPredictionCreate, MLPredictionRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/ml-predictions", tags=["ML Predictions"])

@router.get("/", response_model=list[MLPredictionRead])
def list_predictions(db: Session = Depends(get_db)):
    return crud_ml.get_predictions(db)

@router.post("/", response_model=MLPredictionRead)
def create_prediction(pred: MLPredictionCreate, db: Session = Depends(get_db)):
    return crud_ml.create_prediction(db, pred)

@router.delete("/{pred_id}", response_model=MLPredictionRead)
def delete_prediction(pred_id: UUID, db: Session = Depends(get_db)):
    db_pred = crud_ml.delete_prediction(db, pred_id)
    if not db_pred:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return db_pred
