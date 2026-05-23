from sqlalchemy.orm import Session
from app.infrastructure.models import BarrioDB, TipoUsuarioDB, UsuarioDB, EmpresaDB, RutaDB, HorarioDB, TiempoDB, DetalleRutaDB, RutaBarrioDB

class TipoUsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(TipoUsuarioDB).all()

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(UsuarioDB).all()

class EmpresaRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(EmpresaDB).all()

class BarrioRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(BarrioDB).all()

class RutaRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(RutaDB).all()

class HorarioRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(HorarioDB).all()

class TiempoRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(TiempoDB).all()

class DetalleRutaRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(DetalleRutaDB).all()

class RutaBarrioRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(RutaBarrioDB).all()