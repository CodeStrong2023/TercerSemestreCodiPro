let personajeSeleccionado = null;
let vidasJugador = 3;
let vidasEnemigo = 3;

function seleccionarPersonajeJugador() {
  let personajeRadio = document.querySelector('input[name="personaje"]:checked');
  if (personajeRadio) {
    personajeSeleccionado = personajeRadio.id;
    alert(`SELECCIONASTE A ${personajeSeleccionado.toUpperCase()}`);
  } else {
    alert('NO SELECCIONASTE UN PERSONAJE');
  }
}

function atacar(ataque) {
  let enemigoAtaque = getRandomAtaque();
  let mensaje = '';
  if (ataque === enemigoAtaque) {
    mensaje = `EMPATE! Ambos personajes atacaron con ${ataque.toUpperCase()}`;
  } else if (ataque === 'punio' && enemigoAtaque === 'barrida') {
    mensaje = `GANASTE! Tu personaje atacó con PUNIO y el enemigo atacó con BARRIDA`;
    vidasEnemigo--;
  } else if (ataque === 'patada' && enemigoAtaque === 'punio') {
    mensaje = `PERDISTE! Tu personaje atacó con PATADA y el enemigo atacó con PUNIO`;
    vidasEnemigo--;
  } else if (ataque === 'barrida' && enemigoAtaque === 'patada') {
    mensaje = `GANASTE! Tu personaje atacó con BARRIDA y el enemigo atacó con PATADA`;
    vidasEnemigo--;
  } else {
    mensaje = `PERDISTE! Tu personaje atacó con ${ataque.toUpperCase()} y el enemigo atacó con ${enemigoAtaque.toUpperCase()}`;
    vidasJugador--;
  }
  document.getElementById('mensaje').innerHTML = mensaje;
  document.getElementById('vidas-jugador-num').innerHTML = vidasJugador;
  document.getElementById('vidas-enemigo-num').innerHTML = vidasEnemigo;
}

function getRandomAtaque() {
  let ataques = ['punio', 'patada', 'barrida'];
  return ataques[Math.floor(Math.random() * ataques.length)];
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

let botonAtaquePunio = document.getElementById('boton-punio');
botonAtaquePunio.addEventListener('click', () => atacar('punio'));

let botonAtaquePatada = document.getElementById('boton-patada');
botonAtaquePatada.addEventListener('click', () => atacar('patada'));

let botonAtaqueBarrida = document.getElementById('boton-barrida');
botonAtaqueBarrida.addEventListener('click', () => atacar('barrida'));
