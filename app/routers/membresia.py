from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

# Crear una nueva membresía
@router.post("/membresias/", response_model=schemas.Membresia)
def create_membresia(membresia: schemas.MembresiaCreate, db: Session = Depends(database.get_db)):
    return crud.create_membresia(db=db, membresia=membresia)
