from sqlalchemy.orm import Session
from app.models import Membresia

def get_membresias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Membresia).offset(skip).limit(limit).all()

def create_membresia(db: Session, membresia: Membresia):
    db.add(membresia)
    db.commit()
    db.refresh(membresia)
    return membresia
