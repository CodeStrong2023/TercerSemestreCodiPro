// script.js
let userScore = 0;
let computerScore = 0;
let resultElement = document.getElementById('result');

document.getElementById('piedra').addEventListener('click', () => playRound('piedra'));
document.getElementById('papel').addEventListener('click', () => playRound('papel'));
document.getElementById('tijera').addEventListener('click', () => playRound('tijera'));
document.getElementById('reiniciar').addEventListener('click', resetGame);

function playRound(userChoice) {
    const choices = ['piedra', 'papel', 'tijera'];
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];

    let result;
    if (userChoice === computerChoice) {
        result = '¡Empate!';
    } else if ((userChoice === 'piedra' && computerChoice === 'tijera') ||
               (userChoice === 'papel' && computerChoice === 'piedra') ||
               (userChoice === 'tijera' && computerChoice === 'papel')) {
        result = '¡Ganaste!';
        userScore++;
    } else {
        result = '¡Ganó la computadora!';
        computerScore++;
    }

    resultElement.textContent = `Elegiste ${userChoice}, La computadora elige ${computerChoice}. ${result} Puntaje: ${userScore} - ${computerScore}`;
}

function resetGame() {
    userScore = 0;
    computerScore = 0;
    resultElement.textContent = '¡Juego reiniciado!';
}