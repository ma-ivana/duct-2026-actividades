# Informe sobre práctica de Analizador gráfico de frecuencias      

*¿Por qué el gráfico usa palabras[::-1] y valores[::-1] en lugar de palabras y valores directamente? (Pista: probá sacar el [::-1] y compará el orden de las barras).*  
"**[::-1]**" hace referencia a la anotación de slice que usa Python para indicar el índice en el que comienza el corte (incluido) de una secuencia y el índice en el que termina (no incluido). Si ambos índices se omiten, significa que la secuencia se incluye en su totalidad (desde el primero al último índice), y se dejan los dos puntos solamente. 
El tercer valor indica el paso, en este caso 1, y el signo menos indica que se debe invertir el orden predeterminado. En este gráfico, las frecuencias se muestran de mayor a menor, pero el orden predeterminado hubiera sido de menor a mayor.

---

*¿Qué pasaría con el gráfico si cambiás top_n=10 por top_n=20? ¿Seguiría siendo legible?*  
"**top_n=10**" es un parámetro que define cuántas de las palabras más frecuentes se graficarán. Con 10 palabras, el gráfico es claro y fácil de interpretar; con 20, se ve bastante aglutinado y resulta más difícil notar con claridad a qué palabra corresponde cada barra.

---

*¿Por qué usar plt.barh() (barras horizontales) en vez de plt.bar() (barras verticales) para este caso?*  
Porque hay más de 5 categorías, que es lo recomendado para el gráfico de barras verticales. Además, el Eje X en este caso contiene los valores de frecuencia, que ocupan pocos caracteres. En cambio, las palabras mencionadas en el Eje Y podrían tener mucho más que tres caracteres. Por eso, es preferible mostrarlas en el Eje Y más que en el X, para que las etiquetas se lean correctamente.

---