#Volviendolo a intentar 
import sys

def limpiar_valor(valor):  #Implementa funcion de limpieza de valores
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos (solo permite digitos, punto y signo negativo)
    - Retorna el numero limpio como string
    """
    # Primero quitamos espacios
    valor = valor.strip()
    
    # Si después de quitar espacios está vacío, retornamos cadena vacía
    if not valor:
        return ""
    
    # Caracteres permitidos: digitos, punto decimal y signo negativo
    caracteres_validos = '0123456789.-'
    
    # Construimos el string solo con caracteres permitidos
    valor_limpio = ''
    for char in valor:
        if char in caracteres_validos:
            valor_limpio += char
    
    return valor_limpio

def convertir_a_entero(texto):
    """
    Convierte texto a entero, truncando decimales.
    Si el texto está vacío o no es un número válido, retorna 0.
    """
    if not texto:  # Si está vacío
        return 0
    
    try:
        # Convertimos a float primero (maneja decimales y negativos)
        numero = float(texto)
        # Truncamos con int() (NO redondeamos)
        return int(numero)
    except ValueError:
        # Si no se puede convertir
        return 0

def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    # Quitamos el salto de linea y espacios al inicio/final de la linea completa
    linea = linea.strip()
    
    # Regla 1: Linea vacia o solo espacios -> 0
    if not linea:
        return 0
    
    # Separamos por comas
    elementos = linea.split(',')
    
    suma = 0
    for elemento in elementos:
        # Limpiamos el valor (quita espacios y caracteres no válidos)
        valor_limpio = limpiar_valor(elemento)
        
        # Convertimos a entero (truncando) y sumamos
        numero = convertir_a_entero(valor_limpio)
        suma += numero
    
    return suma

def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    for linea in sys.stdin:
        linea = linea.rstrip('\n')
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()