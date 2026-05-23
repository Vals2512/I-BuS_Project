from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.application.use_cases import listar_barrios

app = FastAPI()

@app.get("/barrios")
def get_barrios(db: Session = Depends(get_db)):
    return listar_barrios(db)