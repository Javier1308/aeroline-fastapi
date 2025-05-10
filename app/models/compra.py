from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Compra(Base):
    __tablename__ = 'compras'

    id_historial = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    asiento = Column(String)
    id_pasajero = Column(Integer, ForeignKey('pasajeros.id_pasajero'))
    id_vuelo = Column(Integer)

    # Relación con Pasajero
    pasajero = relationship("Pasajero", back_populates="compras")
