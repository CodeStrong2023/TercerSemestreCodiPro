miFuncion(8, 2); //Esto se le conocec cccomo Hosting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;
}

//Llamamos la funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una funcion de tipo expresion o funcion anonima
let x = function(a, b){return a + b}; //necesita cierre con punto y coma por que es una sola linea
resultado = x(5, 6);// al llamar se pone la variable y parentesis
console.log(resultado);


//Funciones de tipo self y invoking
(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6);


console.log(typeof miFuncion);
function miFuncion2(a, b){
    console.log(arguments.length);
}

miFuncion2(5, 7, 3, 6);

//toString
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFunciconFlecha = (a, b) => a + b;
resultado = sumarFunciconFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado);

//Funcion tipo expresion
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); //muestra el parametro de: a
    console.log(arguments[1]); //muestra el parametro de: b
    return a + b + arguments[2];
}
resultado = sumar(3, 2 , 9);
console.log(resultado);


//sumar todos los argumentos con el concpeto de Hoisting
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i <arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}

//Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k);

//Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona)
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = "Perez";
}

cambiarValorObjeto(persona);
console.log(persona)