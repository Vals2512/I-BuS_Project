# 🚌 IBuS — Sistema de Rutas de Buses · Sogamoso

Django 5.1 + PostgreSQL (Supabase) + Docker

---

## 🚀 Cómo correr el proyecto (tú)

### Primera vez:
```bash
# 1. Descomprime el zip y abre la carpeta en la terminal
# 2. El archivo .env ya viene configurado con Supabase
# 3. Ejecuta:
docker compose up --build
```
Listo. Entra a → http://localhost:8000
Usuario: admin@ibus.com | Contraseña: admin123

### Desde la segunda vez:
```bash
docker compose up
```

### Parar el servidor:
```bash
docker compose down
```

---

## 👩‍💻 Cómo lo arranca tu compañera

1. Clonar el repo de GitHub:
```bash
git clone https://github.com/TU_USUARIO/ibus_project.git
cd ibus_project
```
2. Crear su `.env` (pedirte la contraseña de Supabase por privado):
```bash
cp .env.example .env
# Editar .env y poner la contraseña donde dice PEDIR_A_COMPAÑERA
```
3. Correr:
```bash
docker compose up --build
```
Ya tiene el mismo sistema con los mismos datos.

---

## 📤 Subir a GitHub (primera vez)

```bash
git init
git add .
git commit -m "Proyecto IBuS inicial con Docker y Supabase"
git remote add origin https://github.com/TU_USUARIO/ibus_project.git
git push -u origin main
```

## 🔄 Flujo diario con tu compañera

```bash
git pull          # Antes de empezar — traer cambios de ella
# ... trabajan ...
git add .
git commit -m "descripción del cambio"
git push          # Subir los cambios
```

---

## ⚠️ Reglas importantes
- NUNCA subas el `.env` a GitHub (ya está bloqueado en .gitignore)
- Comparte la contraseña de Supabase SOLO por WhatsApp, nunca en GitHub
- Si alguien cambia `models.py`, debe correr y subir las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
# luego git add + commit + push
```
