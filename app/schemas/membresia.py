from pydantic import BaseModel
from datetime import date

class MembresiaBase(BaseModel):
    tipo: str  # 'clasica' o 'premium'
    fecha_expiracion: date
    id_pasajero: int

    class Config:
        orm_mode = True
