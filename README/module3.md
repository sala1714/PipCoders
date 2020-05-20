# Documentación Module 3
A continuación vamos a explicar el funcionamiento de las distintas funciones del fichero *module3.py* .

Cabe destacar que, en este módulo, importamos la librería *random* para calcular los primeros centros de manera aleatoria.

## Función clustering()
Esta función recibe como parámetros un diccionario sobre el que se quieren calcular los *clusters* y el número de *clusters*
a calcular. Con estos datos, aplicando el algortimo de *k-medoids*, calcula el *clustering* de los países pasados como 
parámetros. 

El coste teórico de ejecución de la función será (siendo n el número de elementos a hacer el *clustering* y k el número 
de *clusters*):

|Caso medio         |
|-------------------|
|O(k·(n - k<sup>2</sup>))| 

Los costes experimentales de ejecución de la función seran:

|Peor de los casos  |Caso medio         |Mejor de los casos |
|-------------------|-------------------|-------------------|
|O( )			|   O( )     |O( )        |

## Función new_centers()
Esta función recibe como parámetros un diccionario que contiene listas de sumas asociadas a cada país y un diccionario 
que contiene los *clusters* de la vuelta actual. Con estos datos calcula los nuevos centros de cada vuelta del *clustering* 
y devuelve una lista que los contiene.
  
## Función get_center()
Esta función recibe como parámetros el país sobre el que se calcularà el centro, una lista que contiene los centros del 
*clustering* y un diccionario que contiene las distancias entre países. Con estos datos calcula el pais de la lista 
*centers* con menos distancia al pais *country*.