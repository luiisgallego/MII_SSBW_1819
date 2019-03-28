# INFO TAREAS

## Tarea 1 

Hola mundo al que además le añadimos la opción de que nos nuestre el nombre que le pasemos.

## Tarea 2

Llegados a este punto ya tenemos creado todo el directorio de ficheros necesarios para realizar los ejercicios, por lo que para desarrollarlos haremos uso de los ficheros denominados *urls.py* y *views.py* que podemos encontrar dentro del directorio *ejercicios*.

La idea base para poder realizar cada ejercicio será definir la url en urls.py y la lógica de cada ejercicio en la función que se definirá en views.py.

### TEMPLATES

Hemos creado una carpeta dentro de *ejercicios* denominada *templates* que usaremos para separar el *HTML* del resto del código.

- nombres.html => Podemos ver que hemos creado la variable {{ año }}. Se supone que esa variable podemos editarla desde python....

- views.py => importante lo de render. Es lo que se encarga de generar el contenido.

## TAREA 3

Usamos *REQUEST* para coger la URL de por ejemplo el pais - futbol y de esa url tomamos el código fuente de la página. Luego sobre ese código fuente completo hay que pasar expresiones regulares para localizar cosas como imágenes y su título. Posteriormente nos quedamos con ese par titulo - imagen y tendremos que mostrarlo en el template.

El request hay que especificarlo en el requirements, por tanto, el contenedor hay que construirlo de nuevo (docker-compose build .....)

#### Nota

Por ahora hemos sacado las expresiones regulares con la que obtener los títulos por un lado y las url de la imágenes por otro, pero estas expresiones hay que comprobarlas.

## TAREA 4

- La tarea 4, 5 y 6 están ligadas. 
- En esta primera realizaremos las consultas con *pymongo*. Además haremos uso de bootstrap para darle una mejor apariencia.
- Esta tarea estará localizada en ejercicios.

Primero vamos a definir un html con un formulario, y este, realizará una consulta get/post con la que se redigirá a una nueva ruta (segundo html que definir), donde mostraremos el resultado de la consulta. El profesor recomendó hacer la consulta mediante GET ya que POST da un error....
- Formulario con bootstrap.
- Pagina con resultado de las consultas, CSS only.

## TAREA 5

- Esta tarea estará localizada en pelis.
- Usamos *mongoengine*.
- Usar expresiones regulares para la consulta del actor.

## TAREA 6

Formulario con Bootstrap y lo demás con CSS.