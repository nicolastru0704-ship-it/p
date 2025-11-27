# Sistema de Gestión de Transporte Urbano

Proyecto organizado con una estructura de paquete en `src/` y un punto de entrada sencillo (`main.py`).

## Estructura del proyecto

```text
Proyecto-Sistema-de-Transporte/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ main.py
├─ src/
│   └─ sistema_transporte/
│       ├─ __init__.py
│       ├─ cli.py
│       ├─ core.py
│       ├─ models/
│       │   ├─ __init__.py
│       │   ├─ conductor.py
│       │   ├─ pasajero.py
│       │   ├─ persona.py
│       │   └─ ruta.py
│       └─ storage/
│           ├─ __init__.py
│           └─ csv_store.py
├─ data/
│   └─ .gitkeep
└─ assets/
    └─ (imágenes, por ejemplo portada.png)
```

Los archivos `.csv` que usa el sistema se guardan en la carpeta `data/`.

---

## Cómo ejecutar el proyecto localmente

1. **Crear y activar un entorno virtual (recomendado)**

```bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

2. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

3. **Ejecutar el sistema (CLI)**

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

Se abrirá el menú interactivo del sistema de gestión de transporte urbano.

---

## Notas

- La carpeta `data/` está pensada para almacenar los CSV de conductores, pasajeros, rutas y viajes.
- La carpeta `assets/` la puedes usar para guardar la portada o imágenes que quieras mostrar en el README o documentación.
