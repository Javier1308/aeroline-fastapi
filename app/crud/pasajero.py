from sqlalchemy.orm import Session
from app.models import Pasajero

def get_pasajeros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pasajero).offset(skip).limit(limit).all()

def create_pasajero(db: Session, pasajero: Pasajero):
    db.add(pasajero)
    db.commit()
    db.refresh(pasajero)
    return pasajero
