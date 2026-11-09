import re
ruta = "texto.txt"

def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    #palabras = texto.lower().split()
    palabras = re.findall(r"\b\w+\b", texto.lower())
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def main():
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    resultado = contar_frecuencias(texto)

    for palabra, frecuencia in resultado.items():
        print(f"{palabra}: {frecuencia}")

if __name__ == "__main__":
    main()