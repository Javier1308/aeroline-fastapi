from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/pasajeros/", response_model=schemas.Pasajero)
def create_pasajero(pasajero: schemas.PasajeroCreate, db: Session = Depends(database.get_db)):
    return crud.create_pasajero(db=db, pasajero=pasajero)
