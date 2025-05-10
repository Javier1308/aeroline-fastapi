from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

# Crear una nueva compra
@router.post("/compras/", response_model=schemas.Compra)
def create_compra(compra: schemas.CompraCreate, db: Session = Depends(database.get_db)):
    return crud.create_compra(db=db, compra=compra)
