import sys

def main():
    productos = {}
    
    lineas = sys.stdin.readlines()
    if not lineas:
        return
    
    iterador = iter(lineas)
    next(iterador)  # Saltar encabezado
    
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
            precio_unitario = float(partes[3])
            
            if nombre not in productos:
                productos[nombre] = {"unidades": 0, "ingreso": 0.0}
            
            productos[nombre]["unidades"] += cantidad
            productos[nombre]["ingreso"] += cantidad * precio_unitario
            
        except ValueError:
            continue
    
    # Calcular precio promedio y armar reporte
    reporte = []
    for nombre, datos in productos.items():
        unidades = datos["unidades"]
        ingreso = datos["ingreso"]
        promedio = ingreso / unidades if unidades > 0 else 0
        
        reporte.append({
            "producto": nombre,
            "unidades": unidades,
            "ingreso": ingreso,
            "promedio": promedio
        })
    
    # Ordenar por ingreso descendente
    reporte_ordenado = sorted(reporte, key=lambda x: x["ingreso"], reverse=True)
    
    # Imprimir salida
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for p in reporte_ordenado:
        print(f"{p['producto']},{p['unidades']},{p['ingreso']:.2f},{p['promedio']:.2f}")

if __name__ == "__main__":
    main()