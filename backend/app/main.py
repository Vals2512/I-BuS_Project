from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.database import get_db
from app.application.use_cases import listar_barrios, listar_empresas
from app.domain.models import Barrio, Empresa

app = FastAPI()

# Endpoint GET /api/barrios
@app.get("/api/barrios", response_model=List[Barrio])
def get_barrios(db: Session = Depends(get_db)):
    return listar_barrios(db)

# Endpoint GET /api/empresas
@app.get("/api/empresas", response_model=List[Empresa])
def get_empresas(db: Session = Depends(get_db)):
    return listar_empresas(db)
