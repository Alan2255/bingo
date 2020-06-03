[![Build Status](https://travis-ci.org/Alan2255/bingo.svg?branch=master)](https://travis-ci.org/Alan2255/bingo)

# Bingo :8ball:
Éste repositorio es un proyecto para la materia Adaptación al Ambiente de Trabajo (ATT) de 6to año informática del Instituto Politécnico Superior (IPS) de la Universidad Nacional de Rosario (UNR) 2020.<br>
En el mismo se trabajó sobre un generador de talonario de bingo escrito en python.

## Información básica :open_book:
El tipo de juego utilizado es el bingo de 90 bolas, donde un talonario posee 6 cartones de 3 x 9 celdas (o casillas) cada uno, como se muestra en la imagen a continuación.<br>
![Talonario de bingo 90](../imagenes/talonario.png?raw=true)

### Aplicaciones y requisitos :floppy_disk:
A continuacion se detallan las herramientas necesarias para obtener y utilizar los archivos de este repositorio en el sistema operativo Linux.<br>
* Git
* Python
* Pytest
<br>
Antes de comenzar con la instalación actualizamos los repositorios:
<pre><code>sudo apt update</pre></code>

##### Git
Debemos instalar Git si es que no lo tenemos.<br>
Comprobar versión de git:
<pre><code>git --version</pre></code>
Instalar git:
<pre><code>sudo apt install git</pre></code>

##### Python
Debemos instalar python si no lo tenemos.<br>
Comprobar versión de python:
<pre><code>python --version</pre></code>
Instalar python:
<pre><code>sudo apt install python</pre></code>

##### Pytest
Pytest es una herramienta de pip, por lo tanto debemos instalar pip.<br>
Comprobar versión de pip:
<pre><code>pip --version</pre></code>
Instalar pip:
<pre><code>sudo apt install python-pip</pre></code>
Luego instalamos pytest.<br>
Comprobar version de pytest:
<pre><code>pytest --version</pre></code>
Instalar pytest:
<pre><code>pip install pytest</pre></code>

### Documentación y uso :crossed_swords:

#### Clonando el repositorio
Una vez que tenemos todas las herramientas y aplicaciones lo siguiente es:
1. Cree una carpeta nueva donde más le guste, que contendrá los archivos de este repositorio.
<pre><code>mkdir 'nombre_de_la_carpeta'</pre></code>
2. A continuación, entre en dicha carpeta, y ejecute el siguiente codigo.
<pre><code>git pull https://github.com/Alan2255/bingo.git</pre></code>

#### Corriendo el programa
Para correr el programa simplemente ejecutamos el archivo bingo.py
<pre><code>python src/bingo.py</pre></code>

## Licencia :page_facing_up:

## Comentarios :star:
### Agradecimientos
A Mariano D'Agostino, profesor encargado de la asignatura.
