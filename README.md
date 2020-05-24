# PIPCoders
Proyecto en el cual se ha analizado y tratado muestras del virus COVID-19, haciendo una diferenciación en función de 
sus secuencias de RNA por cada país.

Para llevar acabo este proceso en un primer lugar se ha descargado un archivo csv [*sequences.csv*](data/sequences.csv), este archivo contiene 
todas las muestras disponibles en la base de datos de la web. Una vez descargado este archivo el módulo 1 se encarga de tratarlo. 
Después de este tratamiento obtenemos la muestra mediana del virus por cada país. Una vez obtenidas estas muestras medianas el 
módulo 2 obtenemos las distancias entre las muestras de cada país. Y finalmente el módulo 3, agrupa estas muestras según su grado
de diferencia creando clusters.

### Documentación
La documentación de este proyecto está repartida en 4 ficheros *MarkDown* ([SarsCovHierarchy](documentation/sarscovhierarchy.md), [Module 1](documentation/module1.md), 
[Module 2](documentation/module2.md) y [Module 3](documentation/module3.md)), uno por cada fichero de código. 
Aún así, dentro de los ficheros python, también encontramos un comentario por cada función.

### Requerimientos
Para que nuestro programa funcione correctamente es necesario tener instalados los requerimientos del fichero
[*requeriments.txt*](requirements.txt).

### Tests
Para ejecutar los tests de los módulos 1, 2 y 3 hay que posicionarse en el directorio del proyecto y ejecutar 
el comando *python -m unittest* .

### Ejecución
Para ejecutar el programa hay que ejecutar el fichero [*sarscovhierarchy.py*](sarscovhierarchy.py) .

### Multiplataforma
Para que se pueda ejecutar el programa tanto en Linux como en Windows hemos añadido el módulo *needleman_wunsch* 
en dos formatos: *.pyd* para *Windows* y *.so* para *Linux* 

### Autores
*Proyecto de Algorítmica y Complejidad de Ilyass Mahdiyan, Pablo Alás y Josep Sala*

*[Doble Grado Ingeniería Informática y Administración de Empresas (GEIADE)](http://www.doblegrauinformaticaiade.udl.cat/es)*

*Universitat de Lleida (UdL)*



