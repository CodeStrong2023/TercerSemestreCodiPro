CONSIGNA DE LA CLASE 22/05/24
function seleccionarPersonajeJugador(){ //tarea agregar alerta a la funcion al elegir el personaje
    alert('SELECCIONASTE TU PERSONAJE')
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);


ENSAYO 1
function seleccionarPersonajeJugador(){ 
  alert('SELECCIONASTE TU PERSONAJE')
  let personajeSeleccionado = document.querySelector('input[name="personaje"]:checked');

  if (personajeSeleccionado) {
    let idPersonaje = personajeSeleccionado.id;

    if (idPersonaje === 'zuko') {
      alert('SELECCIONASTE A ZUKO, EL PRÍNCIPE DEL FUEGO 🔥');
    } else if (idPersonaje === 'katara') {
      alert('SELECCIONASTE A KATARA, LA MAESTRA DEL AGUA 💧');
    } else if (idPersonaje === 'aang') {
      alert('SELECCIONASTE A AANG, EL AVATAR DEL AIRE 🌪️');
    } else if (idPersonaje === 'toph') {
      alert('SELECCIONASTE A TOPH, LA MAESTRA DE LA TIERRA 🌱');
    } else {
      alert('NO SELECCIONASTE UN PERSONAJE');
    }
  } else {
    alert('NO SELECCIONASTE UN PERSONAJE');
  }
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);



CONSIGNA DE LA CLASE 29/05/24 (función aleatoria para elegir personajes en pelea)
CÓDIGO HTML

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>LA LEYENDA DE AANG: AVATAR</title>
     </head>
    <body>
        <h1>AVATAR 🔥💧🌱🌪️</h1> <!--Esto es estatico, NO cambia, el h1 se utiliza una vez-->

        <section id="seleccionar-personaje">
            <h2>Elige tu Personaje</h2>

            <label for="zuko">Zuko</label> <!--Esta etiqueta es para darle un indicador a los usuarios de que están seleccionando-->
            <input type="radio" name="personaje" id="zuko"/> <!-- name es para agrupar todos los imputs y poder seleccionar-->

            <label for="katara">Katara</label> <!--El atributo for ayuda a vincular un label con un imput a través del mismo id-->
            <input type="radio" name="personaje" id="katara"/> <!--Acá van los personajes-->

            <label for="aang">Aang</label>
            <input type="radio" name="personaje" id="aang"/> <!--Le damos un atributo id para saber cual es el valor de cada uno-->

            <label for="toph">Toph</label>
            <input type="radio" name="personaje" id="toph"/>

            <button id="boton-personaje">Seleccionar</button> <!-- El botón para seleccionar el personaje-->
        </section>

        <section id="seleccionar-ataque">
            <h2>Elige tu ataque</h2> <!--Se puede utilizar varias veces-->
            <p>Tu personaje tiene <span>3</span> vidas</p> <!--Pero esto debe ser dinamico, necesitamos que cambie-->
            <p>Los personajes del enemigo tienen <span>3</span> vidas</p> <!--Con la etiqueta spam vamos a modificar el 3 con JS-->
            <p>
                <button id="boton-fuego">Fuego 🔥</button>
                <button id="boton-agua">Agua 💧</button>
                <button id="boton-tierra">Tierra 🌱</button>
                <button id="boton-aire">Aire 🌪️</button>
            </p>
        </section>

        <section id="mensajes"> <!--Será un párrafo dinamico-->
            <p>Tu personaje atacó con todo el poder del FUEGO, el personaje del enemigo atacó con el medio poder de la TIERRA - GANASTE 🎉</p>
        </section>

        <section id="reiniciar">
            <button id="boton-reiniciar">Reiniciar</button>
        </section>
        <script src="./js/avatar.js"></script>
    </body>
</html>


CÓDIGO JS
function seleccionarPersonajeJugador(){ //tarea agregar activad a la funcion al elegir el personaje
    alert('SELECCIONASTE TU PERSONAJE')
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

ENSAYO 2
FUNCIONES Y VARIABLES AGREGADAS
-Función atacar  se encarga de generar un ataque aleatorio del enemigo y determinar el resultado del combate.
-Función getRandomAtaque devuelve un ataque aleatorio.
-Eventos de click a los botones de ataque para que llamen a la función atacar con el tipo de ataque correspondiente.
-HTML para que los mensajes dinámicos se muestren en un párrafo con id "mensaje".
-Variables para almacenar las vidas del jugador y del enemigo, el HTML muestra las vidas actuales.
