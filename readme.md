# Manual para esta madre #
## [Inicio](manage.py)
Despues de clonar el repositorio:
Antes de nada, es necesario instalar las librerías especificadas [aquí](requirements.txt) usando `pip install -r requirements.txt` desde la terminal en el root del proyecto.

## Carpetas principales
El proyecto se divide (de momento) en 2 carpetas, proyectoSBBDD y proyectoSBBDDAPP, la primera incluye los archivos globales para el funcionamiento de django, como es [settings.py](proyectoSBBDD/settings.py) o las [urls](proyectoSBBDD/urls.py) de la pagina web.
Además está la carpeta proyectoSBBDDAPP dónde se encuentran la mayoría de archivos del proyecto, las plantillas HTML y las views (más adelante explicaré qué es una view)

### [settings.py](proyectoSBBDD/settings.py)
Aquí están todas las configuraciones del proyecto, las cuales se guardan en tuplas(?) de python, de momento, todo lo que debes saber de este archivo es que en TEMPLATES se encuentra el directorio de donde se guardaran (ya me dio pereza poner acentos prdon) todos los documentos HTML que tenga la página.
Además, en DATABASES se encuentran los datos para conectarse a la base de datos de postgres (por defecto es mysql, pero ya hice las migraciones), el proyecto ya está básicamente listo para usarse conectado a la base de datos, de ahí puedes obtener los datos para conectarte a la base de datos desde pgadmin.
Also ahí puedes cambiarle el lenguaje al panel de admin xd.

--------
### [views.py](proyectoSBBDDAPP\views.py)
En este archivo están todas las views de la página web, ya incluí yo todas las que creo vamos a necesitar, pero puedes añadir otra usando la siguiente sintaxis

`def nombreView(request):`

`    return render(request, 'nombreView.html')`

**¿Qué es una view?**
Cada funcion es una view, una view es basicamente el metodo que le dice a django que debe cargar ese archivo HTML, en el ejemplo anterior, esa función está diciendo que debe cargar __nombreView.html__, el cual en teoría, se encuentra en la carpeta [templates](proyectoSBBDDAPP\templates).
el metodo render puedde recibir, además, un diccionario, con el que podemos pasarle datos al documento HTML, pero ahorita no te voy a marear con eso pq me da flojera explicarlo.

--------
**¿Cuando se carga una view?**
### [urls.py](proyectoSBBDDAPP/urls.py)
Hay 2 archivos urls.py, uno dentro de proyectoSBBDD y otro dentro de proyectoSBBDDAPP, básicamente el de la 1ra carpeta se conecta al de la 2da carpeta, así que por ese no te preocupes.
El importante es el que se encuentra dentro de proyectoSBBDDAPP, pues ahí están todas las urls que va a usar la página web, por ejemplo, **mipagina.com/home/** es una url, **mipagina.com/admin/** es otra, etc.

En la linea 4 yo ya importé el archivo [views.py](proyectoSBBDDAPP\views.py) que expliqué más arriba, así que ya puedes usar cualquier view creada en ese archivo.
Las urls se guardan, nuevamente, en una tupla, con la siguiente sintaxis

`path('faq/', views.faq, name='faq')`

'faq/' es el nombre que se pondra en el navegador de internet despues del .com (siempre debe tener un / al final), despues, views.faq es la view que se va a cargar al introducir esa url en el navegador, en este ejemplo, estamos diciendo que al entrar a mipagina.com/faq/ va a cargar la funcion faq que se encuentra en [views.py](proyectoSBBDDAPP\views.py), y si nos vamos a [views.py](proyectoSBBDDAPP\views.py) vemos que la funcion faq carga el documento [faq.html](proyectoSBBDDAPP\templates\faq.html). Por ultimo, name='faq' de momento solo es para darle formalidad, no es necesario, pero es buena practica incluirlo porque puede ayudarnos más adelante.

No es necesario que los 3 campos de path() se llamen igual (faq, en este caso), pero es una buena practica, e intenta mantenerlo así para que en un futuro no confundamos archivos que son de la misma url pero se llaman diferente.

--------
### Carpeta templates
Por si aún no te has dado cuenta, dentro de proyectoSBBDDAPP hay una carpeta llamada templates, ahí están todos los documentos HTML que estaremos usando para la página, de momento ninguno tiene mucha cosa.

Además del documento HTML de cada view, hay 3 extras, [base.html](proyectoSBBDDAPP\templates\base.html), [navBar.html](proyectoSBBDDAPP\templates\navBar.html) y [footer.html](proyectoSBBDDAPP\templates\footer.html). Estas son las plantillas principales, ahora no sé bien cómo explicarlo así q lo dejo para luego XD.
De momento parece que django es más complicado q HTML, y sí, pero ahorra bastante trabajo a la larga gracias a estas plantillas que acabo de mencionar.

### Iniciar el server
Para iniciar el servidor web (suponiendo que ya instalaste requirements.txt), solo debes abrir la terminal en el root del proyecto y escribir `python .\manage.py runserver`. Esto iniciará el servidor y te dará la direccion en la que se inició, por defecto es 
127.0.0.1:8000/ si no mal recuerdo.
Al entrar a esta direccion ya puedes ver la página, como está en [urls.py](proyectoSBBDDAPP/urls.py) `path('', views.home, name='home'),`, es decir, cuando no hay ninguna direccion especificada se carga la view home, y viendo [views.py](proyectoSBBDDAPP\views.py) vemos que la view home carga el archivo [home.html](proyectoSBBDDAPP\templates\home.html).

Puedes ir a distintas urls para probar los distintos HTML, y por si olvidé mencionarlo, cada view que crees y quieras asignarla a una URL especifica, debes agregarla a [urls.py](proyectoSBBDDAPP/urls.py) con la sintaxis que mencioné más arriba.

### Base de datos
En views y urls manejamos todo lo relacionado al frontend (los html y urls), para crear la base de datos usaremos [models.py](proyectoSBBDDAPP/models.py)

Como dije al principio, la base de datos ya está creada y hosteada en azure, y el proyecto conectado a ella, por lo que solo queda crear las tablas.
Para crear una tabla, debes crear una clase dentro de [models.py](proyectoSBBDDAPP/models.py), cada clase es una tabla de la base de datos, y cada variable es un campo de esta.
La sintaxis para crearlas es la siguiente:
```
class nombreTabla(models.Model):
    nombreCampo=models.CharField(max_length=50)
    nombreCampo2=models.BigAutoField(primary_key=True)
    nombreCampo3=models.IntegerField(default='1')
```
En este ejemplo, esa tabla tendrá 3 campos, nombreCampo que es de tipo caracter, con un maximo de 50 caracteres, nombreCampo2 que es de tipo auto (o 'serial' como lo conoces en postgres) y nombreCampo3 que es de tipo entero.

Siempre se debe especificar que pertenece a models, y como es un metodo, no olvides los () del final. Dentro de estos parentesis puedes agregar los constrains del campo, por ejemplo, nombreCampo2 es de tipo serial, y tiene el constrain de que es la llave primaria de la tabla, si al crear la tabla no especificas cual campo es la llave primaria, automaticamente se creará un campo llamado id que será de tipo auto/serial y será la llave primaria de la tabla.

Para eliminar o modificar una tabla, a diferencia de en SQL común, aquí basta con modificar la clase que creaste y que contiene la tabla, si quieres agregarle un campo simplemente lo agregas en el .py, si quieres eliminar la tabla simplemente eliminas la clase.

Ahora, esto es de manera local, pues tienes que empujar estos cambios a la base de datos. Una vez hayas terminado de crear las tablas que quieras, debes abrir la consola como cuando iniciaste el servidor, y escribir los siguientes comando.
` python .\manage.py makemigrations` Esto pone los cambios 'en la mesa'
`python .\manage.py sqlmigrate proyectoSBBDDAPP 0001`(el 0001 es el numero que dio al hacer el comando anterior, puede ser 0001,0002, etc)
`python .\manage.py migrate` Este comando agarra los cambios que ya habías puesto sobre la mesa, y los hace oficiales en la base de datos.


Casi siempre me da errores pq toi menso, entonces no recuerdo si es primero el comando makemigrations, luego sqlmigrate y al final migrate, y primero makemigrations, luego migrate y al ultimo sqlmigrate. No importa, si te falla en el 1er orden intentalo en el 2do xd.

También notarás que en models.py hay unas tablas con una funcion `__self__`, esta no es obligatoria para la base de datos, pero ya explicaré para qué sirve cuando explique el panel de administrador

### Panel de administrador
La mejor parte de django es q ya nos hace la mitad de la tarea, pues ya cuenta con un panel de administrador integrado que se conecta a nuestra base de datos, t tqm mucho django.
Luego sigo explicando lol