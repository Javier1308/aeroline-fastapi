from sqlalchemy.orm import Session
from app import models, schemas

def create_membresia(db: Session, membresia: schemas.MembresiaCreate):
    db_membresia = models.Membresia(**membresia.dict())
    db.add(db_membresia)
    db.commit()
    db.refresh(db_membresia)
    return db_membresia
