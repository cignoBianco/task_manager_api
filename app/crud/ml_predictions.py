from sqlalchemy.orm import Session
from ..models.ml_predictions import MLPrediction
from ..schemas import MLPredictionCreate, MLPredictionRead

def get_predictions(db: Session):
    return db.query(MLPrediction).all()

def get_prediction(db: Session, pred_id):
    return db.query(MLPrediction).filter(MLPrediction.id == pred_id).first()

def create_prediction(db: Session, pred: MLPredictionCreate):
    db_pred = MLPrediction(**pred.dict())
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)
    return db_pred

def update_prediction(db: Session, pred_id, pred: MLPredictionCreate):
    db_pred = get_prediction(db, pred_id)
    if not db_pred:
        return None
    for key, value in pred.dict(exclude_unset=True).items():
        setattr(db_pred, key, value)
    db.commit()
    db.refresh(db_pred)
    return db_pred

def delete_prediction(db: Session, pred_id):
    db_pred = get_prediction(db, pred_id)
    if not db_pred:
        return None
    db.delete(db_pred)
    db.commit()
    return db_pred
