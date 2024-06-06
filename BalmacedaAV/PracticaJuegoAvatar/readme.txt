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



CONSIGNA DE LA CLASE 29/05/24 

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


CONSIGNA DE LA CLASE 05/06/24
-cambiar estrategia de ataque 
-borrar boton aire
-cambios: 
elemento fuegoxpunio
elemento aguaxpatada
elemento tierraxbarrida

-crear función aleatoria para elegir personaje
(parecido a piedrapapeltijera)

-crear una funcion para enemigo

-llamar a la funcion enemigo

-ataques seguir la logica de los elementos

-js:
crear variables globales fuera
ataquejugador
crear funciones

CÓDIGO BÁSICO:
CÓDIGO HTML

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>LA LEYENDA DE AANG: AVATAR</title>
        <script src="./js/avatar.js"></script>
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
            <p>Tu personaje <span id="personaje-jugador"></span> tiene <span>3</span> vidas</p> <!--Pero esto debe ser dinamico, necesitamos que cambie-->
            <p>El personaje <span id="personaje-enemigo"></span> del enemigo tienen <span>3</span> vidas</p> <!--Con la etiqueta spam vamos a modificar el 3 con JS-->
            <p>
                <button id="boton-punio">Punio ✊</button>
                <button id="boton-patada">Patada 🦶</button>
                <button id="boton-barrida">Barrida 👣</button>
            </p>
        </section>

        <section id="mensajes"> <!--Será un párrafo dinamico-->
            <p>Tu personaje atacó con todo el poder del FUEGO, el personaje del enemigo atacó con el medio poder de la TIERRA - GANASTE 🎉</p>
        </section>

        <section id="reiniciar">
            <button id="boton-reiniciar">Reiniciar</button>
        </section>
    </body>
</html>



CÓDIGO JS
let ataqueJugador
let ataqueEnemigo

function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    let botonPunio = document.getElementById('boton-punio') //Ahora creamos un escuchador de eventos
    botonPunio.addEventListener('click', ataquePunio)
    let botonPatada = document.getElementById('boton-patada')
    botonPatada.addEventListener('click', ataquePatada)
    let botonBarrida = document.getElementById('boton-barrida')
    botonBarrida.addEventListener('click', ataqueBarrida)

}

function seleccionarPersonajeJugador(){
    let inputZuko = document.getElementById('zuko')
    let inputKatara = document.getElementById('katara')
    let inputAang = document.getElementById('aang')
    let inputToph = document.getElementById('toph')
    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    if(inputZuko.checked){
        spanPersonajeJugador.innerHTML = 'Zuko'
    }else if(inputKatara.checked){
        spanPersonajeJugador.innerHTML = 'Katara'
    }else if(inputAang.checked){
        spanPersonajeJugador.innerHTML = 'Aang'
    }else if(inputToph.checked){
        spanPersonajeJugador.innerHTML = 'Toph'
    }else{
        alert('Selecciona un personaje')
    }
    seleccinarPersonajeEnemigo()
}

function seleccinarPersonajeEnemigo(){ //esta función va dentro de seleccionarPersonajeJugador() al final
    let personajeAleatorio = aleatorio(1, 4) //A continuación creamos las variables para cada personaje
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo')

    //comenzamos con la lógica
    if(personajeAleatorio == 1){
        spanPersonajeEnemigo.innerHTML = 'Zuko'
    } else if(personajeAleatorio == 2){
        spanPersonajeEnemigo.innerHTML = 'Katara'
    } else if(personajeAleatorio == 3){
        spanPersonajeEnemigo.innerHTML = 'Aang'
    } else {
        spanPersonajeEnemigo.innerHTML = 'Toph'
    }
}

function ataquePunio(){ //Modificamos la variable global ataqueJugador
    ataqueJugador = 'Punio'
    ataqueAleatorioEnemigo()
}

function ataquePatada(){ //Modificamos la variable global ataqueJugador
    ataqueJugador = 'Patada'
    ataqueAleatorioEnemigo()
}

function ataqueBarrida(){ //Modificamos la variable global ataqueJugador
    ataqueJugador = 'Barrida'
    ataqueAleatorioEnemigo()
}

function ataqueAleatorioEnemigo(){//Ahora ocupando la variable global nueva le decimos el ataque y necesitamos la función aleatorio
    let ataqueAleatorio = aleatorio(1, 3)
   
    if(ataqueAleatorio == 1){
        ataqueEnemigo = 'Punio'
    } else if(ataqueAleatorio == 2){
        ataqueEnemigo = 'Patada'
    } else {
        ataqueEnemigo = 'Barrida'
    }
}



function aleatorio(min, max){
    return Math.floor( Math.random() * (max - min +1) + min)
}

window.addEventListener('load', iniciarJuego)