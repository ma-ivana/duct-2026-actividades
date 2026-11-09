# Informe sobre Ejercicio 1 y Ejercicio 2 - Analizador de frecuencias      

*¿Qué palabras aparecen en el top 10 de la Secuencia A del Ejercicio 2 pero desaparecen en la Secuencia B? ¿Por qué desaparecen?*

Todas las palabras de la **Secuencia A** del **Ejercicio 2** (**de, que, la, el, y, los, en, es, un, las**) desaparecen en la **Secuencia B** porque están incluidas en el conjunto `STOP_WORDS` y en la **Secuencia B** se incluye una sentencia `if` que excluye del listado a las palabras mencionadas en `STOP_WORDS`.

---

*Comparando el Ejercicio 1 con el Ejercicio 2: ¿cambia el resultado por usar tokenizar() en lugar de un simple .split()? ¿En qué casos se nota la diferencia (por ejemplo, con signos de puntuación pegados a una palabra)?*

El resultado cambia al usar `tokenizar()` en lugar de `.split()` porque en la función se reemplazan todos los signos de puntuación ASCII: `!"#\$%&'()*+,-./:;<=>?@[\]^_{` por nada (**""**), mientras que el método `split` cuenta solo las instancias de la palabra completa sin signos de puntuación, por eso $\color{blue}{\text{que}}$, $\color{blue}{\text{que,}}$ y $\color{blue}{\text{(que}}$ son palabras distintas según este método, que solo cuenta las instancias de **que** con espacio anterior y posterior. Con la función `tokenizar`, se limpian los signos de puntuación incluidos en el módulo `string` de Python y esas palabras se incluyen en el conteo (104 con `split` vs. 106 con `tokenizar`). Lo mismo ocurre con la conjunción **y** [64 con `split` vs. 67 con `tokenizar` por los dos casos en que $\color{blue}{\text{y}}$ va precedida de paréntesis: $\color{blue}{\text{\(y}}$ y un caso en el que va seguida de coma $\color{blue}{\text{y,}}$].

---

*¿Qué relación encontrás entre la línea que faltaba completar en el Ejercicio 1 y las dos líneas que faltaba completar en el Ejercicio 2? ¿Por qué se repite la misma lógica dos veces en el Ejercicio 2?*  

En ambos casos, se hacen operaciones con el archivo txt proporcionado y se asigna el resultado de una operación a una variable.  
En el **Ejercicio 1**, se usa la función integrada en Python `open()` para abrir el archivo y asignarle el nombre "archivo". Esta función lleva acá tres parámetros para especificarla: nombre/ruta del archivo, modo de apertura del archivo (`r`: lectura con un archivo que obligatoriamente debe existir para que no se genere un error) y `utf-8` como codificación para el texto dado.  
En el **Ejercicio 2**, también se trabaja con el mismo archivo txt, al que se le asigna el nombre archivo y cuyo contenido de lectura se guarda en la variable `texto`. Este contenido se divide en tokens que se guardan en dos diccionarios: un diccionario que contiene todas las palabras y otro que contiene todas las palabras, menos las incluidas en el conjunto `STOP_WORDS`.  
La línea que faltaba completar en el bucle de `frecuencias_todas` y en el de `frecuencias_sin_stopwords` era la misma: una para cada diccionario, por eso se repite la lógica. En el primer caso, guarda todas las palabras en el diccionario `frecuencias_todas`, asigna 0 si es la primera vez que la palabra aparece y suma uno (`+ 1`) cada vez que la palabra vuelve a aparecer. En el segundo caso, hace lo mismo, pero sin contar las palabras incluidas en el conjunto `STOP_WORDS`, y las agrega al diccionario `frecuencias_sin_stopwords`.  
El método `.get()`, que se usa en ambos casos para contabilizar cada token, lleva dos parámetros: la clave (`token`) y el valor (cantidad). Este bucle no es infinito porque se detiene cuando termina de recorrer todos los tokens del texto.  
Al igual que en la línea que había que completar en el **Ejercicio 1**, que asignaba el resultado de leer el archivo a la variable `texto`, en el **Ejercicio 2** se asigna el resultado del método `.get()` a la variable (*diccionario*) correspondiente (`frecuencias_todas` o `frecuencias_sin_stopwords`).

---