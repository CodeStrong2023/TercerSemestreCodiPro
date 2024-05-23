CONSIGNA DE LA CLASE
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
