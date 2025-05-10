from sqlalchemy.orm import Session
from app import models
from app.schemas import compra as schemas

def create_compra(db: Session, compra: schemas.CompraCreate):
    db_compra = models.Compra(**compra.dict())
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return db_compra
