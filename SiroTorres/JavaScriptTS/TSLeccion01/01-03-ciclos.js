//While
let contador = 0;
while(contador <3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//Do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while");

//for
for(let contando = 0; contando < 3 ; contando++){
    console.log(contando)
}
console.log("Fin del ciclo for")

// Palabrra reservada Break
for(let contando = 0; contando <= 10;contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los pares
        break; 
    }
}
console.log("Terrmina el ciclo al encontrar el primer numero par")

//La palabra continue y etiquetas labels
inicio:
for(let contando = 0; contando <= 10;contando++){
    if(contando % 2 !== 0){
        continue inicio; // ir a la siguiente iteracion
    }
    console.log(contando)
}
console.log("Terrmina el ciclo.")



