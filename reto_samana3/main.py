
import sys

def main():
    productos = {}
    
    lineas = sys.stdin.readlines()
    if not lineas:
        return

    iterador = iter(lineas)
    next(iterador)

    for linea in iterador:
        linea = linea.strip()
        if not linea:
            continue
            
        partes = linea.split(',')
        if len(partes) != 4:
            continue
            
        try:
            nombre = partes[1].strip()
            cantidad = int(partes[2])
            precio_u = float(partes[3])
            
            if nombre not in productos:
                productos[nombre] = {"u": 0, "i": 0.0}
            
            productos[nombre]["u"] += cantidad
            productos[nombre]["i"] += (cantidad * precio_u)
            
        except ValueError:
            continue

    reporte = []
    for nombre, datos in productos.items():
        unidades = datos["u"]
        ingreso = datos["i"]
        promedio = ingreso / unidades if unidades > 0 else 0
        
        reporte.append({
            "p": nombre,
            "u": unidades,
            "i": ingreso,
            "pr": promedio
        })

    reporte_ordenado = sorted(reporte, key=lambda x: x["i"], reverse=True)

    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for p in reporte_ordenado:
        print(f"{p['p']},{p['u']},{p['i']:.2f},{p['pr']:.2f}")

if __name__ == "__main__":
    main()
>>>>>>> 0d1d09598856fab8fe0993fd644d5dfd8200d062
