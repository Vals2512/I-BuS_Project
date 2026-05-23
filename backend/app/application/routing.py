import heapq
from collections import defaultdict
from sqlalchemy.orm import Session
from app.infrastructure.models import BarrioDB, RutaDB, RutaBarrioDB, EmpresaDB
from app.domain.models import TramoRuta, RutaCalcularResponse

def calcular_ruta_optima(db: Session, origen_id: int, destino_id: int) -> RutaCalcularResponse:
    # Cargar de barrios
    barrios = {b.idBarrio: b.nombreBarrio for b in db.query(BarrioDB).all()}
    
    if origen_id not in barrios or destino_id not in barrios:
        return None

    # Cargar nombres de rutas
    rutas_db = db.query(RutaDB).all()
    empresas = {e.idEmpresa: e.nombreEmpresa for e in db.query(EmpresaDB).all()}
    rutas_nombres = {
        r.idRuta: f"{empresas.get(r.idEmpresa, 'Bus')} (Frecuencia: {r.frecuencia})"
        for r in rutas_db
    }

    # Modelar el Grafo
    # Conectamor barrios que comparten una misma ruta de transporte
    grafo = defaultdict(list)
    for ruta in rutas_db:
        barrios_ruta = db.query(RutaBarrioDB).filter(RutaBarrioDB.idRuta == ruta.idRuta).all()
        barrio_ids = [br.idBarrio for br in barrios_ruta]
        
        if ruta.inicioRuta_id not in barrio_ids:
            barrio_ids.append(ruta.inicioRuta_id)
        if ruta.destinoRuta_id not in barrio_ids:
            barrio_ids.append(ruta.destinoRuta_id)
            
        for i in range(len(barrio_ids)):
            for j in range(i + 1, len(barrio_ids)):
                u = barrio_ids[i]
                v = barrio_ids[j]
                grafo[u].append({"destino": v, "peso": 1, "ruta_id": ruta.idRuta})
                grafo[v].append({"destino": u, "peso": 1, "ruta_id": ruta.idRuta})

    # Algoritmo de Dijkstra
    distancias = {origen_id: (0, None, None)}
    queue = [(0, origen_id)]
    visitados = set()

    while queue:
        dist_actual, nodo_actual = heapq.heappop(queue)
        
        if nodo_actual == destino_id:
            break
            
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        
        for vecino in grafo[nodo_actual]:
            destino = vecino["destino"]
            peso = vecino["peso"]
            ruta_id = vecino["ruta_id"]
            
            nueva_dist = dist_actual + peso
            
            if destino not in distancias or nueva_dist < distancias[destino][0]:
                distancias[destino] = (nueva_dist, nodo_actual, ruta_id)
                heapq.heappush(queue, (nueva_dist, destino))

    if destino_id not in distancias:
        return None

    # Reconstruir el camino óptimo
    camino = []
    nodo = destino_id
    while nodo is not None:
        dist, anterior, ruta_id = distancias[nodo]
        camino.append(TramoRuta(
            barrio_id=nodo,
            nombre_barrio=barrios.get(nodo, f"Barrio {nodo}"),
            ruta_id=ruta_id,
            nombre_ruta=rutas_nombres.get(ruta_id) if ruta_id else None
        ))
        nodo = anterior

    camino.reverse()
    
    if camino:
        camino[0].ruta_id = None
        camino[0].nombre_ruta = None

    return RutaCalcularResponse(
        total_tramos=len(camino) - 1,
        camino=camino
    )
