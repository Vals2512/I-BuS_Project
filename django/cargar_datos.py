"""
SCRIPT PARA CARGAR DATOS DE WHATSAPP → BASE DE DATOS
=====================================================
Uso: python cargar_datos.py

Este script te permite ingresar manualmente los registros
que tienes guardados en WhatsApp, uno por uno.
Al final genera un archivo datos_iniciales.json que Django
puede cargar automáticamente con: python manage.py loaddata datos_iniciales.json
"""

import json
import sys
import os

datos = {
    "TipoUsuario": [],
    "Barrio": [],
    "Empresa": [],
    "Ruta": [],
    "RutaBarrio": [],
    "Horario": [],
    "Tiempo": [],
    "DetalleRuta": [],
    "Usuario": [],
}

def separador(titulo):
    print(f"\n{'='*50}")
    print(f"  {titulo}")
    print('='*50)

def preguntar(campo, tipo=str, obligatorio=True, default=None):
    while True:
        sufijo = f" (Enter para '{default}')" if default is not None else ""
        valor = input(f"  {campo}{sufijo}: ").strip()
        if not valor and default is not None:
            return default
        if not valor and obligatorio:
            print("  ⚠ Este campo es obligatorio.")
            continue
        try:
            return tipo(valor)
        except ValueError:
            print(f"  ⚠ Ingresa un valor de tipo {'número entero' if tipo==int else 'texto'}.")

def confirmar(pregunta):
    while True:
        r = input(f"\n  {pregunta} (s/n): ").strip().lower()
        if r in ('s', 'si', 'sí', 'y', 'yes'):
            return True
        if r in ('n', 'no'):
            return False

# ─── TIPOS DE USUARIO ───────────────────────────────────────────────
separador("TIPOS DE USUARIO")
print("  (Normalmente: 1=Administrador, 2=Usuario general)")
tipos_default = confirmar("¿Usar los tipos por defecto (Administrador / Usuario general)?")
if tipos_default:
    datos["TipoUsuario"] = [
        {"model": "sistema.tipousuario", "pk": 1, "fields": {"nombreTipo": "Administrador"}},
        {"model": "sistema.tipousuario", "pk": 2, "fields": {"nombreTipo": "Usuario general"}},
    ]
    print("  ✓ Tipos de usuario agregados.")
else:
    pk = 1
    while True:
        nombre = preguntar("Nombre del tipo")
        datos["TipoUsuario"].append({"model": "sistema.tipousuario", "pk": pk, "fields": {"nombreTipo": nombre}})
        pk += 1
        if not confirmar("¿Agregar otro tipo?"):
            break

# ─── BARRIOS ────────────────────────────────────────────────────────
separador("BARRIOS")
print("  Pega los barrios uno por uno (son los que tenías en la BD).")
pk = 1
while True:
    nombre = preguntar(f"Nombre del barrio #{pk}")
    datos["Barrio"].append({"model": "sistema.barrio", "pk": pk, "fields": {"nombreBarrio": nombre}})
    pk += 1
    if not confirmar("¿Agregar otro barrio?"):
        break

# ─── EMPRESAS ───────────────────────────────────────────────────────
separador("EMPRESAS")
pk = 1
while True:
    print(f"\n  -- Empresa #{pk} --")
    nombre   = preguntar("Nombre de la empresa")
    anio     = preguntar("Año de fundación", tipo=int)
    direccion= preguntar("Dirección")
    telefono = preguntar("Teléfono")
    buses    = preguntar("Cantidad de buses", tipo=int)
    conductores = preguntar("Cantidad de conductores", tipo=int)
    datos["Empresa"].append({
        "model": "sistema.empresa", "pk": pk,
        "fields": {
            "nombreEmpresa": nombre,
            "anioFundacion": anio,
            "direccion": direccion,
            "telefono": telefono,
            "cantBuses": buses,
            "cantConductores": conductores,
        }
    })
    pk += 1
    if not confirmar("¿Agregar otra empresa?"):
        break

# Mostrar resumen para facilitar referencias
print("\n  Empresas registradas:")
for e in datos["Empresa"]:
    print(f"    ID {e['pk']}: {e['fields']['nombreEmpresa']}")
print("\n  Barrios registrados:")
for b in datos["Barrio"]:
    print(f"    ID {b['pk']}: {b['fields']['nombreBarrio']}")

# ─── RUTAS ──────────────────────────────────────────────────────────
separador("RUTAS")
pk_ruta = 1
while True:
    print(f"\n  -- Ruta #{pk_ruta} --")
    id_empresa = preguntar("ID de la empresa", tipo=int)
    id_inicio  = preguntar("ID del barrio de inicio", tipo=int)
    id_destino = preguntar("ID del barrio destino", tipo=int)
    frecuencia = preguntar("Frecuencia (ej: 15 minutos, cada hora)")
    datos["Ruta"].append({
        "model": "sistema.ruta", "pk": pk_ruta,
        "fields": {
            "idEmpresa": id_empresa,
            "inicioRuta": id_inicio,
            "destinoRuta": id_destino,
            "frecuencia": frecuencia,
        }
    })
    # Barrios intermedios de la ruta
    print(f"  ¿La ruta #{pk_ruta} pasa por barrios intermedios?")
    pk_rb = len(datos["RutaBarrio"]) + 1
    # Siempre agregar inicio y destino como RutaBarrio
    datos["RutaBarrio"].append({"model": "sistema.rutabarrio", "pk": pk_rb,
                                 "fields": {"idRuta": pk_ruta, "idBarrio": id_inicio}})
    pk_rb += 1
    datos["RutaBarrio"].append({"model": "sistema.rutabarrio", "pk": pk_rb,
                                 "fields": {"idRuta": pk_ruta, "idBarrio": id_destino}})
    pk_rb += 1
    while confirmar("¿Agregar barrio intermedio?"):
        id_b = preguntar("ID del barrio intermedio", tipo=int)
        datos["RutaBarrio"].append({"model": "sistema.rutabarrio", "pk": pk_rb,
                                     "fields": {"idRuta": pk_ruta, "idBarrio": id_b}})
        pk_rb += 1
    pk_ruta += 1
    if not confirmar("¿Agregar otra ruta?"):
        break

# ─── HORARIOS ───────────────────────────────────────────────────────
separador("HORARIOS")
print("  Formato de hora: HH:MM (ej: 06:30)")
pk = 1
while True:
    print(f"\n  -- Horario #{pk} --")
    id_empresa = preguntar("ID de la empresa", tipo=int)
    salida   = preguntar("Hora de salida (HH:MM)")
    llegada  = preguntar("Hora de llegada (HH:MM)")
    datos["Horario"].append({
        "model": "sistema.horario", "pk": pk,
        "fields": {"idEmpresa": id_empresa, "horaSalida": salida, "horaLlegada": llegada}
    })
    pk += 1
    if not confirmar("¿Agregar otro horario?"):
        break

# ─── DETALLE RUTAS ──────────────────────────────────────────────────
separador("DETALLE DE RUTAS (registros de pasajeros)")
print("  Formato de fecha: YYYY-MM-DD (ej: 2025-03-15)")
pk_tiempo = 1
pk_detalle = 1
fechas_vistas = {}

print("\n  Rutas registradas:")
for r in datos["Ruta"]:
    inicio  = next(b['fields']['nombreBarrio'] for b in datos["Barrio"] if b['pk'] == r['fields']['inicioRuta'])
    destino = next(b['fields']['nombreBarrio'] for b in datos["Barrio"] if b['pk'] == r['fields']['destinoRuta'])
    print(f"    ID {r['pk']}: {inicio} → {destino}")

while True:
    print(f"\n  -- Registro #{pk_detalle} --")
    id_ruta   = preguntar("ID de la ruta", tipo=int)
    fecha     = preguntar("Fecha (YYYY-MM-DD)")
    pasajeros = preguntar("Cantidad de pasajeros", tipo=int)

    if fecha not in fechas_vistas:
        fechas_vistas[fecha] = pk_tiempo
        datos["Tiempo"].append({
            "model": "sistema.tiempo", "pk": pk_tiempo,
            "fields": {"fecha": fecha}
        })
        pk_tiempo += 1

    datos["DetalleRuta"].append({
        "model": "sistema.detalleruta", "pk": pk_detalle,
        "fields": {
            "idRuta": id_ruta,
            "idTiempo": fechas_vistas[fecha],
            "cantidadPasajeros": pasajeros,
        }
    })
    pk_detalle += 1
    if not confirmar("¿Agregar otro registro de pasajeros?"):
        break

# ─── USUARIO ADMINISTRADOR ──────────────────────────────────────────
separador("USUARIO ADMINISTRADOR")
print("  Crea el usuario administrador para entrar al sistema.")
email = preguntar("Email del administrador")
clave = preguntar("Contraseña")
datos["Usuario"].append({
    "model": "sistema.usuario", "pk": 1,
    "fields": {"idTipoUsuario": 1, "email": email, "contrasena": clave}
})

# ─── GENERAR JSON ───────────────────────────────────────────────────
fixture = []
for tabla in ["TipoUsuario", "Barrio", "Empresa", "Ruta", "RutaBarrio", "Horario", "Tiempo", "DetalleRuta", "Usuario"]:
    fixture.extend(datos[tabla])

with open("datos_iniciales.json", "w", encoding="utf-8") as f:
    json.dump(fixture, f, ensure_ascii=False, indent=2)

separador("¡LISTO!")
print(f"  ✓ Se generó el archivo: datos_iniciales.json")
print(f"  ✓ Total registros: {len(fixture)}")
print()
print("  PRÓXIMO PASO — carga los datos en la BD:")
print("    python manage.py loaddata datos_iniciales.json")
print()
print("  O con Docker:")
print("    docker compose run web python manage.py loaddata datos_iniciales.json")
print()
