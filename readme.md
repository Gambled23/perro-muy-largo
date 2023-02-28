# Manual para esta madre #
### [Inicio](manage.py)
Despues de clonar el repositorio:
Antes de nada, es necesario instalar las librerías especificadas [aquí](requirements.txt) usando `pip install -r requirements.txt` desde la terminal en el root del proyecto.

### Carpetas principales
El proyecto se divide (de momento) en 2 carpetas, proyectoSBBDD y proyectoSBBDDAPP, la primera incluye los archivos globales para el funcionamiento de django, como es [settings.py](proyectoSBBDD/settings.py) o las [urls](proyectoSBBDD/urls.py) de la pagina web.
a
Además está la carpeta proyectoSBBDDAPP dónde se encuentran la mayoría de archivos del proyecto, las plantillas HTML y las views (más adelante explicaré qué es una view)

### [settings.py](proyectoSBBDD/settings.py)
Aquí están todas las configuraciones del proyecto, las cuales se guardan en tuplas(?) de python, de momento, todo lo que debes saber de este archivo es que en TEMPLATES se encuentra el directorio de donde se guardaran (ya me dio pereza poner acentos prdon) todos los documentos HTML que tenga la página.
Además, en DATABASES se encuentran los datos para conectarse a la base de datos de postgres (por defecto es mysql, pero ya hice las migraciones), el proyecto ya está básicamente listo para usarse conectado a la base de datos, de ahí puedes obtener los datos para conectarte a la base de datos desde pgadmin.
Also ahí puedes cambiarle el lenguaje al panel de admin xd.

--------
### [views.py](proyectoSBBDDAPP/views.py)
En este archivo están todas las views de la página web, ya incluí yo todas las que creo vamos a necesitar, pero puedes añadir otra usando la siguiente sintaxis

`def nombreView(request):`

`    return render(request, 'nombreView.html')`

**¿Qué es una view?**
Cada funcion es una view, una view es basicamente el metodo que le dice a django que debe cargar ese archivo HTML, en el ejemplo anterior, esa función está diciendo que debe cargar __nombreView.html__, el cual en teoría, se encuentra en la carpeta [templates](proyectoSBBDDAPP/templates).
el metodo render puedde recibir, además, un diccionario, con el que podemos pasarle datos al documento HTML, pero ahorita no te voy a marear con eso pq me da flojera explicarlo.

--------
**¿Cuando se carga una view?**
### [urls.py](proyectoSBBDDAPP/urls.py)
Hay 2 archivos urls.py, uno dentro de proyectoSBBDD y otro dentro de proyectoSBBDDAPP, básicamente el de la 1ra carpeta se conecta al de la 2da carpeta, así que por ese no te preocupes.
El importante es el que se encuentra dentro de proyectoSBBDDAPP, pues ahí están todas las urls que va a usar la página web, por ejemplo, **mipagina.com/home/** es una url, **mipagina.com/admin/** es otra, etc.

En la linea 4 yo ya importé el archivo [views.py](proyectoSBBDDAPP/views.py) que expliqué más arriba, así que ya puedes usar cualquier view creada en ese archivo.
Las urls se guardan, nuevamente, en una tupla, con la siguiente sintaxis

`path('faq/', views.faq, name='faq')`

'faq/' es el nombre que se pondra en el navegador de internet despues del .com (siempre debe tener un / al final), despues, views.faq es la view que se va a cargar al introducir esa url en el navegador, en este ejemplo, estamos diciendo que al entrar a mipagina.com/faq/ va a cargar la funcion faq que se encuentra en [views.py](proyectoSBBDDAPP/views.py), y si nos vamos a [views.py](proyectoSBBDDAPP/views.py) vemos que la funcion faq carga el documento [faq.html](proyectoSBBDDAPP/templates/faq.html). Por ultimo, name='faq' de momento solo es para darle formalidad, no es necesario, pero es buena practica incluirlo porque puede ayudarnos más adelante.

No es necesario que los 3 campos de path() se llamen igual (faq, en este caso), pero es una buena practica, e intenta mantenerlo así para que en un futuro no confundamos archivos que son de la misma url pero se llaman diferente.

--------
### Carpeta templates
Por si aún no te has dado cuenta, dentro de proyectoSBBDDAPP hay una carpeta llamada templates, ahí están todos los documentos HTML que estaremos usando para la página, de momento ninguno tiene mucha cosa.

Además del documento HTML de cada view, hay 3 extras, [base.html](proyectoSBBDDAPP/templates/base.html), [navBar.html](proyectoSBBDDAPP/templates/navBar.html) y [footer.html](proyectoSBBDDAPP/templates/footer.html). Estas son las plantillas principales, ahora no sé bien cómo explicarlo así q lo dejo para luego XD.
De momento parece que django es más complicado q HTML, y sí, pero ahorra bastante trabajo a la larga gracias a estas plantillas que acabo de mencionar.

### Iniciar el server
Para iniciar el servidor web (suponiendo que ya instalaste requirements.txt), solo debes abrir la terminal en el root del proyecto y escribir `python .\manage.py runserver`. Esto iniciará el servidor y te dará la direccion en la que se inició, por defecto es 
127.0.0.1:8000/ si no mal recuerdo.
Al entrar a esta direccion ya puedes ver la página, como está en [urls.py](proyectoSBBDDAPP/urls.py) `path('', views.home, name='home'),`, es decir, cuando no hay ninguna direccion especificada se carga la view home, y viendo [views.py](proyectoSBBDDAPP/views.py) vemos que la view home carga el archivo [home.html](proyectoSBBDDAPP/templates/home.html).

Puedes ir a distintas urls para probar los distintos HTML, y por si olvidé mencionarlo, cada view que crees y quieras asignarla a una URL especifica, debes agregarla a [urls.py](proyectoSBBDDAPP/urls.py) con la sintaxis que mencioné más arriba.

---------
### Base de datos
En views y urls manejamos todo lo relacionado al frontend (los html y urls), para crear la base de datos usaremos [models.py](proyectoSBBDDAPP/models.py)

Como dije al principio, la base de datos ya está creada y hosteada en azure, y el proyecto conectado a ella, por lo que solo queda crear las tablas.
Para crear una tabla, debes crear una clase dentro de [models.py](proyectoSBBDDAPP/models.py), cada clase es una tabla de la base de datos, y cada variable es un campo de esta.
La sintaxis para crearlas es la siguiente:
```python
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

Para cada cambio hecho en la base de datos es necesario hacer el comando `makemigrations`, y luego el comando `migrate`

También notarás que en models.py hay unas tablas con una funcion `__self__`, esta no es obligatoria para la base de datos, pero ya explicaré para qué sirve cuando explique el panel de administrador

---------
### Panel de administrador
La mejor parte de django es q ya nos hace la mitad de la tarea, pues ya cuenta con un panel de administrador integrado que se conecta a nuestra base de datos, t tqm mucho django.

Para ingresar al panel de administrador debes entrar a [127.0.0.1:8000/admin/](127.0.0.1:8000/admin/), se abrirá una pantalla de login dónde ingresas los datos de administrador que están en la carpeta compartida de drive. Adentro del panel puedes controlar varias tablas de la base de datos, crear grupos de usuarios, etc.

Por defecto, las nuevas tablas creadas no aparecerán en este panel de administrador, para que aparezcan es necesario modificar el archivo [admin.py](proyectoSBBDDAPP/admin.py), aquí debes importar la tabla (clase) creada en [models.py](proyectoSBBDDAPP/models.py) y activarla para el panel de admin con `admin.site.register(nombreTabla)`. Una vez hayas hecho estos cambios, solo basta con guardar y ya aparecerá en el panel de admin.
Como no se está modificando la base de datos, solo el panel de admin, no es necesario el comando makemigrations.

Puedes modificar cómo se muestran las tablas en el panel de admin creando una clase, como está por ejemplo en la clase **reporteAdmin**, pero creo yo no es necesario hacer esto con más tablas del proyecto, así que me ahorro 6 lineas de explicación.

### Plantillas de django en html
La ventaja de usar django a simplemente usar html, es que ahorra mucho código al momento de diseñar la página web, por ejemplo, el archivo [base.html](proyectoSBBDDAPP/templates/base.html) tiene varias partes propias de django, todo lo que tenga la siguiente sintaxis `{% ____________ %}` es una caracteristica propia de django.

Con django podemos crear documentos HTML 'pantillas', es decir, como una función común de programación, pero en HTML.

Por ejemplo, tengo la plantilla [base.html](proyectoSBBDDAPP/templates/base.html), y si te vas a [home.html](proyectoSBBDDAPP/templates/home.html) verás que lo primero que dice es `{% extends 'base.html' %}` (siempre debe ir en la 1ra linea del html), esto significa, que se extiende del documento [base.html](proyectoSBBDDAPP/templates/base.html), o sea, home.html tendrá todos los aspectos de home.html, y aparte más.

No sé si me explico, pero con esto podemos hacer que todos los elementos que se repiten en una página web como el logo, el header, el footer, etc, solo los incluyamos como si fuera una función, en vez de tener que escribirlos con HTML en cada documento como lo haríamos normalmente.

Ahora, dentro de [base.html](proyectoSBBDDAPP/templates/base.html) tenemos más cosas, por ejemplo:
```HTML
    <title>
        {% block title %} {% endblock %}
    </title>
```
Esto lo que dice es, que en la etiqueta title, esa parte va a cambiar en cada documento HTML, para seguir diciendolo con terminos de programación, es como si crearas la variable (block) title, y dentro de [home.html](proyectoSBBDDAPP/templates/home.html) vemos que en la 2da linea dice `{% block title %}HOME{% endblock %}`, es decir, a la variable title le damos el valor de 'HOME'.

Lo mismo pasa en el body de base.html, donde creamos la variable content,
```HTML
    {% block content %}


    {% endblock %}
```
y en home.html dentro de esta 'variable' escribimos lo que va a cambiar en este HTML.

Por ultimo, está la parte de `{% include 'navBar.html' %}`, esto hace algo parecido al extends, pero lo inserta directamente en esa linea, en [base.html](proyectoSBBDDAPP/templates/base.html) dentro del body lo primero que tenemos es, el logo de la página (perro muy largo), despues `{% include 'navBar.html' %}`, que lo que hace es insertar todo lo que esté dentro de [navBar.html](proyectoSBBDDAPP/templates/navBar.html) en esa parte de la página, despues el block content, donde irá todo el contenido de la página que cambia en cada url, y por ultimo, `{% include 'footer.html' %}`, lo cual de misma manera que la navBar, inserta todo el código HTML que esté en [footer.html](proyectoSBBDDAPP/templates/footer.html).

Sé que suena confuso, pero es bastante más simple de lo que lo hago parecer, solo que no sé bien cómo explicarlo por escrito. Además nos ayuda a escribir código HTML mucho más rápido y menos revoltoso.

---------
### Variables de python en HTML
Podemos pasar variables comúnes de python al documento HTML, así, por ejemplo, podemos hacer una función en python para sacar el día y hora actuales, guardarlos en una variable, pasarlas a un documento HTML y escribirlos ahí. Esto lo hacemos en el metodo render de la view en [views.py](proyectoSBBDDAPP/views.py).

Las variables las debes pasar usando un diccionario de python, por ejemplo la view de home ahora la tenemos así:
```python
def home(request):
    return render(request, 'home.html')
```
Debemos crear un diccionario con las variables a pasar al HTML, y pasarlo en el metodo render, de la siguiente manera:
```python
def home(request):
    diccionario = {'nombre_persona':'juancho',
    'apellido_persona':'reancho',
    'edad':24}

    return render(request, 'home.html', diccionario)
```
Con esto, ya podemos usar las variables guardadas en *diccionario* en **home.html**.

Para usarlas solo debes escribir el nombre entre {{}}, usando el ejemplo de las variables anteriores, si en home.html escribes
```HTML
<p>{{nombre_persona}} {{apellido_persona}} tiene {{edad}} años</p>
```
En la página de HTML se mostraría:
**juancho reancho tiene 24 años**.

La ventaja de esto es, como puedes imaginarte, todas las posibilidades que tienes para obtener datos y guardarlos en una variable de python, para luego imprimirlos en la página HTML. Datos que pueden cambiar según la hora del día o del usuario, sin necesidad de modificar el HTML. Así pasamos de hacer una página HTML estatica (que no cambia) a una dinamica (que cambia segun las condiciones) simon ya me dio flojera acentar y q

----------
### Ciclos y condicionales en HTML
Por defecto, en HTML no existen if, else, for, while, etc. Pero django los implementa para hacer el código más sencillo, así si queremos imprimir los 10 elementos de una lista, no tenemos que poner 10 parrafos, si no meter la lista dentro de un for que lo haga 10 veces.
#### IF
```HTML
        {% if edad < 18 %}
            <p>No tienes la edad suficiente para visitar esta página</p>
        {% else %}    
            <p>Bienvenido</p>
        {% endif %}
```
No creo que haga falta explicar cómo funciona un if, solo revisa la sintaxis, en este condicional lo que hace es, si edad (variable que pasamos desde view.py anteriormente) es menor de 18, imprimir un parrafo que diga que es menor de edad, y un else por si la edad es mayor de 18.
#### FOR
```HTML
        <ul>
            {% if temas%}
                {% for elTema in temas %}
                    <li>{{elTema}}</li>
                {% endfor %}
            {% else %}    
                <p>No hay elementos que mostrar</p>
            {% endif %}
        </ul>
```
Este es un for dentro de un if, tengo una variable llamada temas, que es un arreglo con varios temas, lo primero que hace es verificar que el arreglo tenga elementos, si no tiene, solo escribe 'no hay elementos que mostrar', si sí tiene, entra al for en el que recorre cada elemento y lo imprime en una etiqueta `<li>` (list item). Así, si mi arreglo tiene 30 temas, solo con ese bucle ya me imprime los 30 elementos en una lista de HTML, sin tener que escribir lo mismo 30 veces, como se haría comunmente con HTML.

Creo q es todo lo que necesitas saber para todo el proyecto, un saludo 👍