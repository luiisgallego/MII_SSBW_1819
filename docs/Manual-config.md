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

### Uso

Como estamos haciendo uso de *Docker Compose* para levantar nuestra aplicación tan solo tenemos que realizar lo siguiente:
~~~~
docker-compose up
~~~~

Una vez que nuestra aplicación esta corriendo, ya podemos hacer uso de ella *localhost:8000*.

## Nota

Se ha eliminado del docker-compose mongo-express, ya que estaba causando problemas a la hora de iniciar los contenedores. Por tanto, las consultas con mongo se tendrán que realizar desde terminal (contendor). Para acceder al contenedor en concreto:

- docker exec -it mii_ssbw_1819_mongo_1 bash
    Luego dentro del contenedor ejecutaremos *mongo* para interactuar con la BD.

### Varios

- Eliminar todos los contenedores: docker rm $(docker ps -a -q) => primero hacer stop
