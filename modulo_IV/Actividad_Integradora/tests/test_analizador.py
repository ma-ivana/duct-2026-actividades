from src.analizador import analizar

def test_frecuencias_basico():
    resultado = analizar("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1

def test_frecuencias_vacio():
    resultado = analizar("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = analizar("Sol sol SOL")
    assert resultado["sol"] == 3

'''
   Prueba para verificar si la función contar_frecuencias
   ignora los signos de puntuación y los espacios adicionales
   al contar la frecuencia de las palabras.
'''
def test_frecuencias_signos_puntuacion():
    resultado = analizar("sol, luna. ¡Sol! luna:  ¿Luna?")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 3