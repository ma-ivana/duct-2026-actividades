import re

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

