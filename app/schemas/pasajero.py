from pydantic import BaseModel, ForwardRef
from datetime import date
from typing import List

# Define ForwardRef for circular relationships
Membresia = ForwardRef('Membresia')
Compra = ForwardRef('Compra')

class PasajeroBase(BaseModel):
    nombre_completo: str
    sexo: str
    fecha_nacimiento: date
    email: str
    telefono: str

    # Relationships
    membresias: List[Membresia] = []  # Relación con Membresía
    compras: List[Compra] = []  # Relación con Compra

    class Config:
        orm_mode = True

# Actualizar las referencias después de definir todas las clases
PasajeroBase.update_forward_refs()
