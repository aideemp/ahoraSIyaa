import sys

def fahrenheit_a_celsius(f):
    """Convierte grados Fahrenheit a Celsius usando la fórmula estándar."""
    return (f - 32) * 5 / 9

def clasificar_temperatura(celsius):
    """Asigna una categoría climática según los rangos establecidos."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:  # Rango 0 a 15
        return "Frio"
    elif celsius <= 25:  # Rango 16 a 25
    	return "Templado"
    elif celsius <= 35:  # Rango 26 a 35
        return "Calido"
    else:                # Mayor a 35
        return "Extremo"

def main():
    # Paso 1: Imprimir el encabezado de salida obligatorio
    print("ciudad,temperatura_celsius,clasificacion")
    
    # Usamos una bandera para saltar la primera línea (encabezados de entrada)
    es_primera_linea = True
    
    # Paso 2: Leer línea por línea desde la entrada estándar (stdin)
    for linea in sys.stdin:
        linea = linea.strip() # Limpia espacios y saltos de línea
        
        if es_primera_linea:
            es_primera_linea = False
            continue
            
        if not linea: # Salta líneas vacías
            continue
            
        # Paso 3: Separar y validar los datos
        partes = linea.split(',')
        if len(partes) != 3:
            continue # Ignora si faltan columnas
            
        ciudad = partes[0].strip()
        temp_str = partes[1].strip()
        unidad = partes[2].strip().upper() # Asegura que sea C o F
        
        # Validar unidad y número
        if unidad not in ['C', 'F']:
            continue
            
        try:
            temp_original = float(temp_str)
        except ValueError:
            continue # Ignora si la temperatura no es un número válido
            
        # Paso 4: Procesar conversión
        if unidad == 'F':
            celsius = fahrenheit_a_celsius(temp_original)
        else:
            celsius = temp_original
            
        # Paso 5: Clasificar y mostrar resultado con 1 decimal
        categoria = clasificar_temperatura(celsius)
        print(f"{ciudad},{celsius:.1f},{categoria}")

if __name__ == "__main__":
    main()