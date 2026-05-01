# Sistema de Inventario Modular

Proyecto del Reto Semana 4 — Programación para Ciencia de Datos, IPN.

## Descripción
Lee un inventario CSV, identifica productos con stock bajo y genera un reporte de reorden.

## Estructura
reto_semana_04/
├── main.py
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   └── producto.py
├── utils/
│   ├── __init__.py
│   ├── io.py
│   └── validators.py
├── data/
│   └── inventario.csv
└── outputs/
└── reporte_inventario.csv
## Cómo ejecutar
```bash
python main.py
```

## Salida esperada
El archivo `outputs/reporte_inventario.csv` contendrá los productos cuyo stock está por debajo del mínimo, ordenados de mayor a menor urgencia.