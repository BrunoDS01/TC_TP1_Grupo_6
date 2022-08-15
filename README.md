# Plot Tool Grupo 6
## Herramienta para graficar funciones con dominio temporal o en frecuencia

En caso de querer importar un archivo, se debe especificar si es una señal temporal o si es un gráfico con dominio
en frecuencia. En el caso de ser CSV, se puede especificar si la magnitud está en decibeles o en una escala lineal.
Tanto en Spice por CSV sólo se puede ingresar un Bode/Respuesta en frecuencia, indicando frecuencia, magnitud y fase.
Se pueden ingresar varias respuestas temporales tanto por Spice como por CSV, indicando tiempo, señal 1, señal2, etc.

En formato CSV, los renglones que empiecen con un número o signo serán considerados como el inicio de los datos,
por lo que no se deben ingresar dichos caracteres antes de los datos.