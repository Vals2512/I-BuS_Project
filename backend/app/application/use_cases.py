from sqlalchemy.orm import Session
from app.infrastructure.repositories import BarrioRepository, EmpresaRepository
from app.domain.models import Barrio as DomainBarrio, Empresa as DomainEmpresa

def listar_barrios(db: Session):
    repo = BarrioRepository(db)
    barrios_db = repo.get_all()
    return [
        DomainBarrio(id=b.idBarrio, nombre=b.nombreBarrio)
        for b in barrios_db
    ]

def listar_empresas(db: Session):
    repo = EmpresaRepository(db)
    empresas_db = repo.get_all()
    return [
        DomainEmpresa(
            id=e.idEmpresa,
            nombreEmpresa=e.nombreEmpresa,
            anioFundacion=e.anioFundacion,
            direccion=e.direccion,
            telefono=e.telefono,
            cantBuses=e.cantBuses,
            cantConductores=e.cantConductores
        )
        for e in empresas_db
    ]