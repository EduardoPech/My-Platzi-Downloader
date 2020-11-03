# My Platzi Downloader
Este es un proyecto totalmente reinventado basado en el fork de [`leethobbit`](https://github.com/leethobbit/pluradl.py) para `Pluralsight` modificado por <strong>JesusGimenezG</strong> para `Platzi`.

<i>Actualmente el proyecto solo se encuentra disponible para la plataforma GNU/Linux y puede que funcione en MacOS</i>

## Instalaciónes necesarias
Para poder usar el script es recomendable tener los siguientes programas o paquetes instalados en tu sistema:

<ol>
      <i>Por el momento solo se indican los pasos de instalación en distribuciones basadas en Debian GNU/Linux.</i><br><br>
      <li> 
            Python
            <ul><li>Versión: <i>3.X</i></li></ul>
            <hr>
            <p>
                  Para distribuciones com Debian, Ubuntu, Linux Mint, Deepin, PopOS y otras basadas en Debian ejecutamos el siguiente comando:<br>
                  <pre><code>sudo apt-get install python3</code></pre>
            </p>
      </li>
      <li>
            youtube-dl
            <ul><li>Versión: <i>2020.xx.xx</i></li></ul>
            <hr>
            <i>En la mayoria de distribuciones Linux, <strong>youtube-dl</strong> ya biene incluido en el repositorio de paquetes de la distro.</i><br><br>
            <p>
                  Para distribuciones com Debian, Ubuntu, Linux Mint, Deepin, PopOS y otras basadas en Debian ejecutamos el siguiente comando:<br>
                  <pre><code>sudo apt-get install youtube-dl</code></pre>
            </p>
            <i>Si el paquete <strong>youtube-dl</strong> no se encuentra en los repositorios de tu distro puedes instalarlo de la siguiente manera: </i>
            <p>
                  Instalamos <strong>curl</strong> o <strong>wget</strong>:
<pre>sudo apt-get install curl</pre>
<pre>sudo apt-get install wget</pre>
                  Ejecutamos los siguientes comandos para descargar e instalar <strong>youtuble-dl</strong> en su última versión estable
                  <br><strong>Usando curl</strong>
<pre>sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/bin/youtube-dl</pre>
                  <strong>Usando wget</strong>
<pre>sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/bin/youtube-dl</pre>
                  <strong>Por útlimo damos permisos de ejecución</strong>
<pre>sudo chmod a+rx /usr/local/bin/youtube-dl</pre>
            </p>
            Tambies podemos instalar youtube-dl usando pip
            <strong>Instalamos pip</strong>
<pre>sudo apt-get install python3-pip</pre>
            <strong>Instalamos youtube-dl <i>(si esta instalado se actualiza a la versión mas reciente si esta existe).</i></strong>
<pre>sudo pip3 install youtube_dl</pre>
            <strong>o también</strong>
<pre>sudo pip install youtube_dl</pre>
      </li>
</ol>

## Creación de archivos .txt
En los archivos de texto plano se encuentra la información del curso a descargar. 
### Estructura del archivo
Cada línea del archivo contiene información importante del curso ya sean los identificadores de la clases o identificadores de las lecciones.

<b>* NOTA: Las Lineas en blanco son ignoradas.<br>
      No se deben dejar espacions en blaco al principio de las lineas que contienen información como identificadores.</b>
<ol>
      <li><strong>Identificadores de secciones</strong>
            <p>
                  Las secciones son como se agrupan los videos en el curso por ejemplo:<br> <i>Seccion 1 - Introduccion</i>.<br>
                  Y esta a la vez contiene videos relativos a ella por ejemplo:<br> <i>Video 1 - Bienvenida al curso</i><br>
                  <i>Video 2 - Que aprenderas</i><br>
                  <i>Video 3 - Proyectos del curso</i><br>
                  etc..
            </p>
      </li>
      Para crear una sección debes usar la siguiente sintaxis:
<pre>[Nombre de la sección]</pre>
      Debes reemplazar el texto entre '[]' por el nombre de la leccion de tu curso, se recomienda poner los nombres de la lecciones de acuerdo al orden como aparecen en el curso.
      <br>
      <b><i>También es recomendable agregar un número a la sección para poder indentificarla</i></b>
      <br><hr>
      Ejemplo de una sección:<br>
<pre>[001 - Introducción]</pre>
      <li>
            Identificadores de las clases<br>
            <b>*NOTA: Verifica que los identificadores que pongas en el archivo sean clases de video, ya que este programa sirve solo para descargar archivos no de otro tipo, por tanto el programa fallara si no se tiene cuidado.</b><br><br>
            Cada identificador de la clase se obtiene de la siguiente manera:<br>
            Copea el link de la clase en la que te encuentras y editalo de la siguiente forma:<br>
<pre>https://platzi.com/clases/1814-basico-javascript/26297-hoisting/</pre>
<strong>Remuve las partes innecesarias del link para que quede limpio: </strong>
<pre>1814-basico-javascript/26297-hoisting</pre>
      </li>
      Los videos pertenecientes a una sección deben ir debajo de la declarción de esta, ejemplo:
<pre>[001 - Introduccion]
1919-curso-ejemplo/3949-bienvenida
1919-curso-ejemplo/3950-que-aprenderas
1919-curso-ejemplo/3951-proyectos-del-curso

[002 - Seguna sección]
1919-curso-ejemplo/3952-otra-videoclase
[003 - Tercera sección]
1919-curso-ejemplo/3953-algotra-videoclase
</pre>
<b>Al finalizar guarda el archivo de texto, puedes porner cualquier nombre, pero sugiero que evites el uso de carácteres poco comunes como ~"}{`¨ etc.. ya que en algunos sistemas su reprensetación es un poco diferente a como tu querias que fuera.</b>
</ol>

<i>Estoy trabajando en un metodo que permita ahorrase todo este paso de poner identificadores, para que simplementes tengas que ingresar el link del curso y el programa haga el resto de trabajo por ti.</i>
## Modo de uso
Primero deberas clonar el repositorio:
<pre>git clone https://github.com/Devil64-Dev/My-Platzi-Downloader.git</pre>
<strong>y</strong>
<pre>cd My-Platzi-Downloader</pre>
Damos permisos de ejecución al archivo `linux-platzidl-devil.py` para esto ejecutamos:
<pre>chmod a+x linux-platzidl-devil.py</pre>
Ejecutamos como un script normal, el sitema se encargara de buscar el interprete correcto para el script
<pre>./linux-platzidl-devil.py</pre>
A continuación escribimos <i>usuario (correo)</i> y <i>contraseña</i> de nuestra cuenta de <b>Platzi</b>
<br><br>
Luego de ingresar usuario y contraseña deberas poner el nombre del archivo donde se encuantran los detalles de el curso a descargar, seguido de un nombre para el curso ya que este nombre se usara para carpeta donde se guardaran todos los videos del curso.

<i>Tengo pensado en extender este proyecto a otras plataformas, como Cherahana, Domestika etc... Talvez demore algo de tiempo, pero espero poder lograrlo.</i><br>
<b>Si tienes conocimientos programando en Python y crees que este proyecto puede mejorar o tienes algo que aportar puedes escribir en la seccion de inquietudes.</b>

By: Devil64-Dev, https://devil64-dev.com/