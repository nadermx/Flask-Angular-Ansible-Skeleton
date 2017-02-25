# flask-blueprints-pony-skeleton
Flask Blueprints PonyOrm Skeleton app python3.4.3

#TODO
User Login

## Angular App

La aplicación en angular está utilizando Grunt, Bower, Sass and Angular 1.5

```
/angula-app/
```

### Setup

Es necesario tener instalado NodeJs, nosotros hemos usado `Node v6.*; ten en cuenta que las versiones pares de Node son las versiones estables, mientras que las impares son versiones aun en desarrollo y pueden tener bugs.

```
https://nodejs.org/es/
```

Para poder iniciar la aplicación es necesario instalar las dependencias:

```
npm install
```

Además, tienes que instalar las diferentes tecnologías y/o librerías, en nuestro caso usaremos Bower para instalar `Angular, Bootstrap y Angular UI Router:

```
bower install
```

### Let's start

Para iniciar la aplicación usaremos `Grunt`, es necesario estar dentro del directorio en donde tenemos alojado la aplicación:

```
cd angular-app
grunt serve
```

La aplicación debería levantar una nueva pestaña de tu `navegador por defecto, si esta pestaña no se abro entonces deberás acceder a:

```
localhost:9000
````

### Angular Boilerplate

Esta aplicación de Angular fue creada utilizando el style guide de John Papa como referencia, la hemos modificado para nuestro propio uso.

#### Structure

```
/app
....index.html
..../images
..../styles
........main.scss
..../scripts
........app.js
........route.jss
......../views
......../shared
......../core
............config.js
............model.js
............persist.js
............utils.js
............api.js
............main.js
```

El achivo index.html contiene nuestro ng-app y crea la primera estructura de nuestra aplicación; es necesario agregar los nuestros controladores o directivas en este archivo para ser utilizados posteriormente.

*   **styles**: Contiene nuestra hoja de estilo Sass
*   **scripts**: Contiene todos nuestros scripts, controlladores, directivas, templates, etc.
*   **scripts/core**: Contiene nuestros archivos que manejan la data de la aplicación y la configuración; así como la persistencia de datos.
*   **script/views**: Contiene nuestras vistas, cada debe estar en su propia carpeta y debe contar con un template y un controlador.
*   **scripts/shared**: Contiene nuestras directivas, cada directiva debe estar en su propia carpeta y contener o no un template

### Build and Deploy

Para hacer un pase a producción utilizaremos grunt:

```
grunt build
```

Este comando creará los archivos compilados dentro de:

```
./app/templates
./app/static
```

En esta versión del boilerplate es necesario acceder al archivo index.html, generador por **grunt build** y guardado en la carpeta templates y modificar los atributos **href** y **src** de las etiquetas **links** y **scripts**, y agregar en cada uno **/static/**:

```
<link rel="stylesheet" href="/static/styles/...
<script src="/static/scripts/...
```