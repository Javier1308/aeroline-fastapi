from pydantic import BaseModel
from datetime import date

class CompraBase(BaseModel):
    fecha: date
    asiento: str
    id_pasajero: int
    id_vuelo: int

    class Config:
        orm_mode = True
