# INFO TAREAS

Directorio principal PROYECTO, luego tenemos uno para las primeras tareas denominado EJERICIOS y el grueso de la app estará en PELIS.

## Tarea 1 

Hola mundo al que además le añadimos la opción de que nos nuestre el nombre que le pasemos.

## Tarea 2

------>  TERMINAR EJERCICIO 5.

Llegados a este punto ya tenemos creado todo el directorio de ficheros necesarios para realizar los ejercicios, por lo que para desarrollarlos haremos uso de los ficheros denominados *urls.py* y *views.py* que podemos encontrar dentro del directorio *ejercicios*.

La idea base para poder realizar cada ejercicio será definir la url en urls.py y la lógica de cada ejercicio en la función que se definirá en views.py.

### TEMPLATES

Hemos creado una carpeta en la reaiz denominada *templates* que usaremos para separar el *HTML* del resto del código.

- nombres.html => Podemos ver que hemos creado la variable {{ año }}. Se supone que esa variable podemos editarla desde python....

- views.py => importante lo de render. Es lo que se encarga de generar el contenido.

## TAREA 3

------> Se ha intentando realizar añadiendo las imagenes pero era imposible unir el numero de titulos con sus imagenes, por lo que se ha preferido mostrar solo el titular.

Usamos *REQUEST* para coger la URL de por ejemplo el pais - futbol y de esa url tomamos el código fuente de la página. Luego sobre ese código fuente completo hay que pasar expresiones regulares para localizar cosas como imágenes y su título. Posteriormente nos quedamos con ese par titulo - imagen y tendremos que mostrarlo en el template.

El request hay que especificarlo en el requirements, por tanto, el contenedor hay que construirlo de nuevo (docker-compose build .....)

#### Nota

Por ahora hemos sacado las expresiones regulares con la que obtener los títulos por un lado y las url de la imágenes por otro, pero estas expresiones hay que comprobarlas.

### Nota 2

- Hay que usar la libreria request, no podemos usar cualquiera.
- Hay que pasar el XML a TREE: arbolito = fromstring(request.content)
- Y ahora podemos recorrer cada item el cual seria cada nodo del arbol, y de ahí recoger titulo - foto.
- La idea es que en una pagina aparezcan titulos, y en otra imágenes. Aunque podemos mostrarlos conjuntamente reduciendo el número de estos a 10, por ejemplo.
- Sacar titulares de aqui: http://ep00.epimg.net/rss/tags/ultimas_noticias.xml
- Expresion regular: <title><!\[CDATA\[(.+?)\]\]><\/title>
- Titular y foto:  https://elpais.com/tag/rss/albumes/a/

## TAREA 4

- La tarea 4, 5 y 6 están ligadas. 
- En esta primera realizaremos las consultas con *pymongo*. Además haremos uso de bootstrap para darle una mejor apariencia.
- Esta tarea estará localizada en ejercicios.

Primero vamos a definir un html con un formulario, y este, realizará una consulta get/post con la que se redigirá a una nueva ruta (segundo html que definir), donde mostraremos el resultado de la consulta. El profesor recomendó hacer la consulta mediante GET ya que POST da un error....
- Formulario con bootstrap.
- Pagina con resultado de las consultas, CSS only.

### IMPORTANTE

Solo hacer con CSS el formulario y listado de respuesta de este en pymongo, y ale. Luego apartir de tarea6 (mongoengine) ya usamos only bootstrap.

Es decir, vamos a hacer el formulario y la respuesta de pymongo con CSS. Luego ya tomamos bootstrap de forma pro para hacer mongoengine.

## TAREA 5

- Esta tarea estará localizada en pelis.
- Usamos *mongoengine*.
- Usar expresiones regulares para la consulta del actor.

## TAREA 6

Formulario con Bootstrap y lo demás con CSS.

## ------> Resumen final Tareas 4-5-6

Para no complicar especialmente estas tareas, primero se ha instalado la BD mongo en nuestro docker-compose, junto con pymongo y mongoengine. Entonces el proceso de resolución que hemos seguido ha sido crear un formulario y su correspondiente vista de información de la pelicula mediante CSS ambos para el caso de hacer uso de pymongo. En el caso de mongoengine usaremos Bootstrap.

- La tarea 4 (url) es pymongo.
- MONGOENGINE:
    - Comprobamos que la consulta nos devuelve algo y en función de ello actuamos ya que sino produce error.
    - Al html que se muestra mandamos una lista de peliculas devueltas.
    - Modificado poster HTTP - HTTPS para que pueda ser mostrada la imagen.
    - Para borrar una pelicula hago uso de Javascript, lo que me permite llamar al método correspondiente y a la vez actualizar la página sin recargar.

----> Terminar parte de CSS (Formulario e Info de película)
----> Terminar parte de BOOTSTRAP (Formulario e Info de película)

## TAREA 8

Instalar nginx y creanos los certificados (/usr/local/etc/ssl), luego añadimos arhcivos de configuracion ale.
https://localhost/ejercicios/tarea4/




