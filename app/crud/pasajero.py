from sqlalchemy.orm import Session
from app import models, schemas

def get_pasajeros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pasajero).offset(skip).limit(limit).all()

def create_pasajero(db: Session, pasajero: schemas.PasajeroCreate):
    db_pasajero = models.Pasajero(**pasajero.dict())
    db.add(db_pasajero)
    db.commit()
    db.refresh(db_pasajero)
    return db_pasajero
