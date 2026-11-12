import matplotlib.pyplot as plt
import re

from pathlib import Path

ruta = Path(__file__).resolve().parent.parent / "data" / "texto_integradora.txt"
output_dir = Path(__file__).resolve().parent.parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

def analizar(texto):
    """
    Lee un archivo de texto y cuenta la frecuencia de cada palabra. La expresión regular utilizada
    permite capturar palabras que contienen letras, números y guiones bajos,
    sin la puntuación ni espacios que pudiesen acompañarlas.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar

    Retorna:
        dict: diccionario con las palabras y sus frecuencias
    """
    
    palabras_texto = re.findall(r"\b\w+\b", texto.lower())

    frecuencias = {}
    for palabra in palabras_texto:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias
     

def graficar(frecuencias, top_n=10):
    """
    Lee las frecuencias de palabras del texto (incluidas las palabras vacías)
    y genera un grafico de barras horizontales con las top_n
    palabras mas frecuentes.

    Parametros:
        frecuencias (dict): diccionario con las palabras y sus frecuencias
        top_n (int): cantidad de palabras a graficar

    Retorna:
        None (genera y guarda el grafico)
    """
        
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]


    palabras = [p[0] for p in top10]
    valores = [p[1] for p in top10]

    plt.figure(figsize=(10, 6))
    bars = plt.barh(palabras[::-1], valores[::-1], color="lightseagreen")
    plt.bar_label(bars, padding=3)
    plt.title(f"Top {top_n} palabras más frecuentes")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")
    plt.tight_layout()
    plt.savefig(output_dir / "grafico_frecuencias_con_palabras_vacias.png", dpi=150, bbox_inches="tight")
    plt.show()

def main():
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}.")
        return {}
    
    frecuencias = analizar(texto)
    graficar(frecuencias)

if __name__ == "__main__":
    main()