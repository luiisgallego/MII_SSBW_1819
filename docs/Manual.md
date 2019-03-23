# Apuntes sobre el proceso seguido

## Configuración y uso de Django - Docker

Como vamos a usar Python primero necesitamos definir un Dockerfile para este, y además en el requirements indicaremos las dependencias (siendo especialmente interersante Django).

Luego definimos el docker-compose, donde especificamos los servicios, en principio tendremos solo el web, pero posteriormente añadiremos la BD. Llegados a este punto ya podemos crearnos un proyecto de Django con docker-compose:
~~~~
docker-compose run web django-admin startproject nombreProyecto .
~~~~

Bien, una vez creado el proyecto, ya podemos crear diferentes aplicaciones dentro de un mismo proyecto. Para ello hacemos lo siguiente:
~~~~
docker-compose run web python manage.py startapp ejercicios
~~~~

Muy importante dirigirnos al archivo *proyecto/settings.py* y en *INSTALLED_APPS* añadir el nombre de la aplicación creada, sino, no podremos verlo por el navegador. También tendremos que añadir las direcciones en *proyecto/urls.py*.

Llegados a este punto ya podemos trabajar con nuestra aplicación concreta. Para poder mostrar las diferentes urls en el navegador se sigue un poco la idea de lo anterior, dentro de la carpeta de nuestra aplicación concreta, en *urls.py* tendremos que definir las diferentes rutas que queramos usar. Ya estariamos en algo como *localhost:8000/ejercicios/rutas_especificadas_aqui*. Finalmente, el código que interpretará cada ruta lo definiremos en *views.py*.


### Configuración .... REALIZAR

- Eliminar todo lo creado (imagenes - contenedor)
- Buscar versiones Alpine
- Montar Dockerfile (web)
- Montar Docker-compose (mongo)

### Uso

Como estamos haciendo uso de *Docker Compose* para levantar nuestra aplicación tan solo tenemos que realizar lo siguiente:
~~~~
docker-compose up
~~~~

Una vez que nuestra aplicación esta corriendo, ya podemos hacer uso de ella *localhost:8000*.

### Tarea 2

Llegados a este punto ya tenemos creado todo el directorio de ficheros necesarios para realizar los ejercicios, por lo que para desarrollarlos haremos uso de los ficheros denominados *urls.py* y *views.py* que podemos encontrar dentro del directorio *ejercicios*.

La idea base para poder realizar cada ejercicio será definir la url en urls.py y la lógica de cada ejercicio en la función que se definirá en views.py.

## TEMPLATES

Hemos creado una carpeta dentro de *ejercicios* denominada *templates* que usaremos para separar el *HTML* del resto del código.

- nombres.html => Podemos ver que hemos creado la variable {{ año }}. Se supone que esa variable podemos editarla desde python....

- views.py => importante lo de render. Es lo que se encarga de generar el contenido.

### TAREA 3

Usamos *REQUEST* para coger la URL de ... (preguntar).... y de esa url tomamos el código fuente de la página. Luego sobre ese código fuente completo hay que pasar expresiones regulares para localizar cosas como imágenes y su título. Posteriormente nos quedamos con ese par titulo - imagen y tendremos que mostrarlo en el template.

El request hay que especificarlo en el requirements, por tanto, el contenedor hay que construirlo de nuevo (docker-compose build .....)


### TAREA 4

Actualmente es necesario realizar dos veces *docker-compose up* para que funcione correctamente.

### TAREA 5

- Hay que realizar esa consulta tanto para pymongo como mongoengine => una de estas consultas es tarea 4 y la otra tarea 5... creo.
- Mongoengine en pelis, pymongo en ejercicios

- Entonces la idea es mediante pymongo hacer un ejercicio de consulta mediante formulario (o URL?), luego además, como aplicación definitiva(peli) lo haremos con mongoengine.
- Usar expresiones regulares para la consulta del actor.

#### RESUMEN

Hemos estado creando el docker-compose de mongo y mongoexpress, hemos importado la BD y utilizado PYMONGO para realizar consultas. Para poder realizar estas consultas y resolver el ejercicio es neceario crearse un formulario mediante un template donde el usuario introduce los parámetros de búsqueda. Tras esto, mediante pymongo se realiza la consulta. Esto se realiza en el proyecto de EJERCICIOS.

Ahora, en el proyecto PELIS, tenemos que realizar los mismo pero con MONGOENGINE.

