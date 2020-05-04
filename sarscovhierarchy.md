# Documentación SarsCovHierarchy

A continuación se va a explicar el funcionamiento de las distintas funciones.

## Función main()

Es la encargada de tratar los datos del archivo .csv (contiene la información de todas las muestras).
Esta función organiza las muestras dentro de un diccionario usando el país como clave. Cada país (clave) lleva asociado una lista con los identificadores de las muestras (*Accession*) y otra lista con las longitudes de estas (*Length*).

A continuación, esta misma función llama a la función **median()** que es la encargada de rellenar un nuevo diccionario con la longitud mediana de cada país.

## Función median()

Esta función recibe como parámetro una lista de valores y devuelve el valor mediano de esta. Para realizar su funcionamiento se apoya en la función **sort**.

## Función sort()

Esta función recibe una lista como parámetro y la devuelve ordenada de menor a mayor valor.
En esta función se aplica la técnica *divide y vencerás* para realizar la ordenación. 
Los costes de ejecución de la función serían:

|Peor de los casos  |Caso medio         |Mejor de los casos |
|-------------------|-------------------|-------------------|
|O(n^2^)			|   O(n·log(n))     |O(n·log(n))        |

## Función final_median_dict()

Esta función recibe un diccionario que contiene todos los países con su valor mediano asociado y recibe también el diccionario original (cada país contiene dos listas: una con las *Accessions*, y otra con las *Lengths*). 
A continuación crea un nuevo diccionario que contiene la *Accession* correspondiente a la mediana de cada país.

