# Informe sobre práctica con pruebas Pytest     

*¿Qué pasaría con test_frecuencias_mayusculas si en analizador.py sacaras el .lower()? Probalo y describí qué mensaje de error muestra pytest.*  

El método **.lower()** devuelve el string en minúsculas únicamente, ya que convierte todas las mayúsculas en minúsculas. Al sacar este método de la función, **Sol**, **sol** y **SOL** se consideran tres palabras diferentes, en lugar de ser las tres iguales a **sol**. 
La prueba falla porque no encuentra tres instancias de **sol**, sino una de **Sol**, una de **sol** y una de **SOL**.

---

*¿Por qué contar_frecuencias recibe un string directamente en vez de una ruta de archivo, como en la Clase 2? ¿Qué ventaja tiene eso a la hora de escribir pruebas?*  

En las pruebas se suelen utilizar datos *hardcodeados*, es decir, se pasan los datos (en este caso el string) directamente a la función para que la prueba esté aislada y no dependa de la ejecución de otra parte del código. Pasarle los datos directamente hace que sea también más legible y predecible.
Es una práctica estándar en el caso de estas pruebas. Para probar varios casos de forma automatizada con `pytest`se podría usar la parametrización, que permite ejecutar una misma función de prueba con diferentes conjuntos de datos de entrada y resultados esperados.

---

*Se te ocurre algún otro caso de borde para probar (por ejemplo, texto con signos de puntuación, o con espacios de más)? Escribí una cuarta prueba con ese caso.*  

Para verificar si la función `contar_frecuencias` ignora los signos de puntuación y los espacios adicionales al contar la frecuencia de las palabras, escribí la siguiente prueba:
```python
def test_frecuencias_signos_puntuacion():
    resultado = contar_frecuencias ("sol, luna. ¡Sol! luna:  ¿Luna?")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 3
```
Dio error. Incluso antes que contar mal, dio el error de que la clave "sol" no se encontraba, lo cual tiene sentido, porque en la lista de palabras que le pasé, no existe "sol" sin signos adicionales.
Escribí una línea nueva en el archivo "analizador.py" para que la función `contar_frecuencias` contemple también las palabras con puntuación y con espacios de más.
Reemplacé 
```python
palabras = texto.lower().split()
```
por 
```python
palabras = re.findall(r"\b\w+\b", texto.lower())
```
Primero importé `re` arriba de todo para poder usar expresiones regulares. Con `re.findall(r"\b\w+\b")` puedo encontrar todas las palabras enteras (\b marca los límites de inicio/final de cada palabra), ya que busca todos los caracteres de palabras, incluidos números y guiones bajos.

Con esa línea modificada en el archivo [analizador.py](analizador.py), el resultado de la cuarta prueba en [test_analizador.py](test_analizador.py) da **PASSED**. 

No hace falta seguir usando `.split()` porque la línea con la expresión regular ya extrae cada palabra por separado, solo que sin puntuación ni espacios de más. `.split()` solo separa las palabras en los espacios en blanco, pero conserva los signos especiales que estén pegados a esas palabras.

---

**NOTA:**  
    A modo de prueba, creé otro archivo, llamado [analizador_con_texto.py](analizador_con_texto.py) para probar esta versión de la función `contar_frecuencias` con el mismo texto trabajado en las clases anteriores: [La Biblioteca de Babel](texto.txt).
    Por ejemplo, la palabra "zaguán" aparece en el texto en tres oportunidades: dos en las que está la palabra sola, con un espacio simple antes y otro después (zaguán) y una tercera en la que aparece con una coma (zaguán,). La función `contar_frecuencias` encuentra correctamente las tres instancias de la palabra "zaguán", sin tener en cuenta la coma.  
    En el caso de la palabra "uno", el texto tiene diferentes versiones de esta palabra:  
        - uno 3  
        - Uno 1  
        - Uno, 1  
        - Uno: 1  
        - ¡uno 1  
    La función `contar_frecuencias` encuentra correctamente las siete instancias como "uno".