from fastapi import FastAPI
from app.routers import pasajero, membresia, compra  # Importamos los routers

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Incluir las rutas (endpoints) para cada entidad
app.include_router(pasajero.router, prefix="/pasajeros", tags=["Pasajeros"])
app.include_router(membresia.router, prefix="/membresias", tags=["Membresías"])
app.include_router(compra.router, prefix="/compras", tags=["Compras"])
