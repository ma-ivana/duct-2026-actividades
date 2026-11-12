# Práctica de Python - Módulo 4 - Actividad Integradora

* Código de analizador de frecuencias: [**analizador.py**](src/analizador.py). Lee el archivo de texto proporcionado. Usa *try/except* para controlar lo que sucede si el archivo no existe y cuenta la frecuencia de cada palabra de ese archivo usando un diccionario. Además, genera y guarda un gráfico de barras con las 10 palabras más frecuentes.  
En este archivo, también agregué `nltk` para filtrar las palabras vacías y generar el gráfico solo con las palabras significativas más frecuentes. A modo de comparación, dejé el código del analizador sin este filtro: [**analizador_con_palabras_vacias.py**](src/analizador_con_palabras_vacias.py), el cual genera el [gráfico de barras que incluye las palabras vacías](output/grafico_frecuencias_con_palabras_vacias.png).

* Código de pruebas con Pytest para el analizador de frecuencias: [**test_analizador.py**](tests/test_analizador.py)
* Datos: [**El mercado de las palabras**](data/texto_integradora.txt)
* Salida: [**gráfico de palabras más frecuentes (sin palabras vacías)**](output/grafico_frecuencias_sin_palabras_vacias.png) y [**gráfico de palabras más frecuentes (con palabras vacías)**](output/grafico_frecuencias_con_palabras_vacias.png)
* Los requisitos se proporcionan en un archivo separado, llamado [**requirements.txt**](requirements.txt): archivo generado con el comando `python -m pip freeze > requirements.txt`

## Ejecución

- Clonar el proyecto o descargarlo como zip.  
- El proyecto se creó usando Python 3.12.0.
- Crear un entorno virtual. Comando sugerido: `py -3.12 -m venv .venv`  
- Abrir los archivos.  
- Ejecutar `pip install -r requirements.txt`  
- Ejecutar [**analizador.py**](src/analizador.py) para obtener el [**gráfico de palabras más frecuentes (sin palabras vacías)**](output/grafico_frecuencias_sin_palabras_vacias.png).
- Ejecutar [**analizador_con_palabras_vacias.py**](src/analizador_con_palabras_vacias.py) para obtener el [**gráfico de palabras más frecuentes (con palabras vacías)**](output/grafico_frecuencias_con_palabras_vacias.png).
- Para ejecutar las pruebas, abrir el archivo [**test_analizador.py**](tests/test_analizador.py) y ejecutar el siguiente comando en la consola: `python -m pytest -v`. Los cinco tests deberían dar $\color{green}{\text{**PASSED**}}$ como resultado.