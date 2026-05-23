from sqlalchemy.orm import Session
from app.infrastructure.repositories import BarrioRepository, EmpresaRepository, RutaRepository, HorarioRepository, TiempoRepository
from app.domain.models import Barrio as DomainBarrio, Empresa as DomainEmpresa, Ruta as DomainRuta, Horario as DomainHorario, Tiempo as DomainTiempo
from app.infrastructure.models import RutaDB, HorarioDB, TiempoDB

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

# --- CASOS DE USO DE RUTAS ---
def crear_ruta(db: Session, ruta_in: DomainRuta):
    repo = RutaRepository(db)
    nueva_ruta = RutaDB(
        idEmpresa=ruta_in.idEmpresa,
        inicioRuta_id=ruta_in.inicioRuta_id,
        destinoRuta_id=ruta_in.destinoRuta_id,
        frecuencia=ruta_in.frecuencia
    )
    creada = repo.create(nueva_ruta)
    return DomainRuta(id=creada.idRuta, idEmpresa=creada.idEmpresa, inicioRuta_id=creada.inicioRuta_id, destinoRuta_id=creada.destinoRuta_id, frecuencia=creada.frecuencia)

def actualizar_ruta(db: Session, id_ruta: int, ruta_update: DomainRuta):
    repo = RutaRepository(db)
    ruta_db = repo.get_by_id(id_ruta)
    if not ruta_db:
        return None
    ruta_db.idEmpresa = ruta_update.idEmpresa
    ruta_db.inicioRuta_id = ruta_update.inicioRuta_id
    ruta_db.destinoRuta_id = ruta_update.destinoRuta_id
    ruta_db.frecuencia = ruta_update.frecuencia
    
    actualizada = repo.update(ruta_db)
    return DomainRuta(id=actualizada.idRuta, idEmpresa=actualizada.idEmpresa, inicioRuta_id=actualizada.inicioRuta_id, destinoRuta_id=actualizada.destinoRuta_id, frecuencia=actualizada.frecuencia)

# --- CASOS DE USO DE HORARIOS ---
def crear_horario(db: Session, horario_in: DomainHorario):
    repo = HorarioRepository(db)
    nuevo_horario = HorarioDB(
        idEmpresa=horario_in.idEmpresa,
        horaSalida=horario_in.horaSalida,
        horaLlegada=horario_in.horaLlegada
    )
    creado = repo.create(nuevo_horario)
    return DomainHorario(id=creado.idHorario, idEmpresa=creado.idEmpresa, horaSalida=str(creado.horaSalida), horaLlegada=str(creado.horaLlegada))

def actualizar_horario(db: Session, id_horario: int, horario_update: DomainHorario):
    repo = HorarioRepository(db)
    horario_db = repo.get_by_id(id_horario)
    if not horario_db:
        return None
    horario_db.idEmpresa = horario_update.idEmpresa
    horario_db.horaSalida = horario_update.horaSalida
    horario_db.horaLlegada = horario_update.horaLlegada
    
    actualizado = repo.update(horario_db)
    return DomainHorario(id=actualizado.idHorario, idEmpresa=actualizado.idEmpresa, horaSalida=str(actualizado.horaSalida), horaLlegada=str(actualizado.horaLlegada))

# --- CASOS DE USO DE TIEMPOS ---
def crear_tiempo(db: Session, tiempo_in: DomainTiempo):
    repo = TiempoRepository(db)
    nuevo_tiempo = TiempoDB(fecha=tiempo_in.fecha)
    creado = repo.create(nuevo_tiempo)
    return DomainTiempo(id=creado.idTiempo, fecha=str(creado.fecha))

def actualizar_tiempo(db: Session, id_tiempo: int, tiempo_update: DomainTiempo):
    repo = TiempoRepository(db)
    tiempo_db = repo.get_by_id(id_tiempo)
    if not tiempo_db:
        return None
    tiempo_db.fecha = tiempo_update.fecha
    
    actualizado = repo.update(tiempo_db)
    return DomainTiempo(id=actualizado.idTiempo, fecha=str(actualizado.fecha))