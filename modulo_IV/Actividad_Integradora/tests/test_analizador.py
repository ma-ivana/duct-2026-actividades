from src.analizador import analizar as analizar_sin_palabras_vacias
from src.analizador_con_palabras_vacias import analizar as analizar_con_palabras_vacias 

"""
   Verifica si la función analizar_sin_palabras_vacias
   cuenta correctamente la frecuencia de las palabras sin palabras vacías.
"""

def test_frecuencias_basico():
    resultado = analizar_sin_palabras_vacias("sol luna sol el en")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1

"""
   Verifica si la función analizar_sin_palabras_vacias
   devuelve un diccionario vacío para un texto vacío.
"""

def test_frecuencias_vacio():
    resultado = analizar_sin_palabras_vacias("")
    assert resultado == {}

"""
   Verifica si la función analizar_sin_palabras_vacias
   cuenta correctamente la frecuencia de las palabras
   en un texto con mayúsculas y minúsculas.
   
"""

def test_frecuencias_mayusculas():
    resultado = analizar_sin_palabras_vacias("Sol sol SOL")
    assert resultado["sol"] == 3

"""
   Verifica si la función analizar_sin_palabras_vacias
   ignora los signos de puntuación y los espacios adicionales
   al contar la frecuencia de las palabras.

"""

def test_frecuencias_signos_puntuacion():
    resultado = analizar_sin_palabras_vacias("sol, luna. ¡Sol! luna:  ¿Luna?")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 3



"""
   Verifica si la función analizar_con_palabras_vacias
   cuenta correctamente la frecuencia de las palabras
    incluyendo las palabras vacías.
"""
def test_frecuencias_con_palabras_vacias():
    resultado = analizar_con_palabras_vacias("sol luna sol el en")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1
    assert resultado["el"] == 1
    assert resultado["en"] == 1
