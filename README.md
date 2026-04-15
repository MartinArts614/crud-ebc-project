# Aplicación CRUD en Django - Inventario de Productos

Este proyecto cumple con la **Fase 2** del proyecto de Aplicaciones Web I: una aplicación web simple en **Python + Django** con operaciones **CRUD** y estilo básico con **Bootstrap**.

## Qué incluye
- Crear productos
- Consultar listado de productos
- Ver detalle de un producto
- Editar productos
- Eliminar productos
- Búsqueda por nombre, categoría o descripción
- Base de datos SQLite
- Pruebas básicas

## Estructura
- `crud_ebc/`: configuración principal del proyecto Django
- `productos/`: app principal del CRUD
- `static/`: estilos CSS
- `db.sqlite3`: base de datos local (se genera después de migraciones)

## Instalación
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Abrir en el navegador:
```bash
http://127.0.0.1:8000/productos/
```

## Ejecutar pruebas
```bash
python manage.py test
```

## Idea para evidencia técnica
- Captura del listado de productos
- Captura del formulario de alta
- Captura de edición
- Captura de confirmación de eliminación
- Captura de la terminal con `python manage.py runserver`

## Nota didáctica
Se eligió el objeto **Producto** porque permite explicar claramente:
- modelo de datos
- vistas
- templates
- formularios
- rutas
- base de datos
- patrón MVC/MVT en Django
