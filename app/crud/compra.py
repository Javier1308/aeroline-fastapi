from sqlalchemy.orm import Session
from app.models import Compra

def get_compras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Compra).offset(skip).limit(limit).all()

def create_compra(db: Session, compra: Compra):
    db.add(compra)
    db.commit()
    db.refresh(compra)
    return compra
