# Flask Sqlalchemy

## Crear el proyecto

```bash
python -m venv nombre_del_entorno
source nombre_del_entorno/Scripts/activate
source nombre_del_entorno/bin/activate
nombre_del_entorno\Scripts\activate
```

## Instalar dependencias
```bash
pip install Flask Flask-sqlalchemy python-dotenv psycopg2-binary
```

## Ejecutar las migraciones

```bash
# Crear la carpeta migrations (Solo se ejecuta la primera vez)
flask db init

# Generar los documentos de las migraciones (Se ejecuta cada vez que tengamos cambios en la base de datos)
flask db migrate -m "Primera migracion"

# Ejecutar los cambios de los documentos (Se ejecuta cada vez que tengamos que aplicar los cambios generador en migrate)
flask db upgrade
```

## Ejecutar el proyecto