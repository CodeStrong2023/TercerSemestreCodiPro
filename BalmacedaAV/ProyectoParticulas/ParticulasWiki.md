<h1>✨Partículas Wiki</h1>
<h2>Índice</h2>
<dl>
<dt>Introducción</dt>
<dt>Variables y constantes</dt>
<dt>Funciones</dt>
<dt>Clases y objetos</dt>
<dt>Eventos y listeners</dt>
<dt>Animación y renderizado</dt>
<dt>Configuración y ajustes</dt>

<dt>Introducción</dt>
<dd>Este proyecto utiliza la biblioteca AnimeJS para crear un efecto de partículas en un canvas HTML. El usuario puede interactuar con el efecto mediante clicks o toques en la pantalla.</dd>
<dt>Variables y constantes</dt>
<dd><br>window.human: indica si el usuario ha interactuado con el efecto (true) o no (false)
<br>canvasEl: elemento canvas HTML
<br>ctx: contexto de dibujo del canvas
<br>numberOfParticules: número de partículas a crear (30)
<br>pointerX y pointerY: coordenadas del puntero del usuario
<br>tap: evento de click o toque en la pantalla (dependiendo del dispositivo)
<br>colors: array de colores para las partículas</dd>
<dt>Funciones</dt>
<dd><br>setCanvasSize(): ajusta el tamaño del canvas según el tamaño de la ventana
<br>updateCoords(e): actualiza las coordenadas del puntero del usuario
<br>setParticuleDirection(p): establece la dirección y velocidad de una partícula
<br>createParticule(x, y): crea una partícula en la posición (x, y)
<br>createCircle(x, y): crea un círculo en la posición (x, y)
<br>renderParticule(anim): renderiza las partículas en el canvas
<br>animateParticules(x, y): anima las partículas desde la posición (x, y)</dd>
<dt>Clases y objetos</dt>
<dd><br>Particule: objeto que representa una partícula, con propiedades como x, y, color, radius, endPos y draw
<br>Circle: objeto que representa un círculo, con propiedades como x, y, color, radius, alpha y draw</dd>
<dt>Eventos y listeners</dt>
<dd><br>document.addEventListener(tap, function(e) {...}): listener para el evento de click o toque en la pantalla
<br>window.addEventListener('resize', setCanvasSize, false): listener para el evento de cambio de tamaño de la ventana</dd>
<dt>Animación y renderizado</dt>
<dd><br>anime.timeline(): crea una línea de tiempo de animación
<br>anime({duration: Infinity, update: function() {...}}): crea una animación infinita que se actualiza en cada frame
<br>ctx.clearRect(0, 0, canvasEl.width, canvasEl.height): limpia el canvas antes de renderizar las partículas</dd>
<dt>Configuración y ajustes</dt>
<dd><br>numberOfParticules: ajusta el número de partículas a crear
<br>colors: ajusta los colores disponibles para las partículas
<br>anime.random(): ajusta la aleatoriedad de la animación</dd>
</dl>
<p>Esta wiki ha sido realizada para entender el proyecto Partículas.</p>
