from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Pasajero(Base):
    __tablename__ = 'pasajeros'

    id_pasajero = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, index=True)
    sexo = Column(String)
    fecha_nacimiento = Column(Date)
    email = Column(String, unique=True, index=True)
    telefono = Column(String)

    # Relaciones
    membresias = relationship("Membresia", back_populates="pasajero")
    compras = relationship("Compra", back_populates="pasajero")
