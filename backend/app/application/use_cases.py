from app.infrastructure.repositories import BarrioRepository
from sqlalchemy.orm import Session

def listar_barrios(db: Session):
    repo = BarrioRepository(db)
    return repo.get_all()