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
  } else if (ataque === 'fuego' && enemigoAtaque === 'tierra') {
    mensaje = `GANASTE! Tu personaje atacó con FUEGO y el enemigo atacó con TIERRA`;
    vidasEnemigo--;
  } else if (ataque === 'agua' && enemigoAtaque === 'fuego') {
    mensaje = `GANASTE! Tu personaje atacó con AGUA y el enemigo atacó con FUEGO`;
    vidasEnemigo--;
  } else if (ataque === 'tierra' && enemigoAtaque === 'aire') {
    mensaje = `GANASTE! Tu personaje atacó con TIERRA y el enemigo atacó con AIRE`;
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
  let ataques = ['fuego', 'agua', 'tierra', 'aire'];
  return ataques[Math.floor(Math.random() * ataques.length)];
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

let botonAtaqueFuego = document.getElementById('boton-fuego');
botonAtaqueFuego.addEventListener('click', () => atacar('fuego'));

let botonAtaqueAgua = document.getElementById('boton-agua');
botonAtaqueAgua.addEventListener('click', () => atacar('agua'));

let botonAtaqueTierra = document.getElementById('boton-tierra');
botonAtaqueTierra.addEventListener('click', () => atacar('tierra'));

let botonAtaqueAire = document.getElementById('boton-aire');
botonAtaqueAire.addEventListener('click', () => atacar('aire'));
