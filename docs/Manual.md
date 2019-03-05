# Apuntes sobre el proceso seguido

## Configuración y uso de Django - Docker

### Configuración .... REALIZAR

### Uso

Como estamos haciendo uso de *Docker Compose* para levantar nuestra aplicación tan solo tenemos que realizar lo siguiente:
~~~~
docker-compose up
~~~~

Una vez que nuestra aplicación esta corriendo, ya podemos hacer uso de ella *localhost:8000*.

## Ejercicios

### Tarea 2

Llegados a este punto ya tenemos creado todo el directorio de ficheros necesarios para realizar los ejercicios, por lo que para desarrollarlos haremos uso de los ficheros denominados *urls.py* y *views.py* que podemos encontrar dentro del directorio *ejercicios*.

La idea base para poder realizar cada ejercicio será definir la url en urls.py y la lógica de cada ejercicio en la función que se definirá en views.py.



## TEMPLATES

Hemos creado una carpeta dentro de *ejercicios* denominada *templates* que usaremos para separar el *HTML* del resto del código.

- nombres.html => Podemos ver que hemos creado la variable {{ año }}. Se supone que esa variable podemos editarla desde python....

- views.py => importante lo de render. Es lo que se encarga de generar el contenido.

### TAREA 3

Usamos *REQUEST* para coger la URL de ... (preguntar).... y de esa url tomamos el código fuente de la página. Luego sobre ese código fuente completo hay que pasar expresiones regulares para localizar cosas como imágenes y su título. Posteriormente nos quedamos con ese par titulo - imagen y tendremos que mostrarlo en el template.
