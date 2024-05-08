let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); //Convierrte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //Metodo o funcion
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return 'El nombre es: '+this.nombre+', edad: '+this.edad;
    }
    
}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto')
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direcccion = 'Salada 14';
persona2.telefono = '89238928';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']) //Acedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');
//for in
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]) 
}
console.log('Cambiamos y eliminamos un error')
persona.apellida = 'Betancud'; //Cambiamos dinamicamente el valor de un objeto
delete persona.apellida; //Eliminamos el error
persona.apellido = 'Betancud' //Cambiamos dinamicamente el valor sin el error
console.log(persona);

//Distinta formas de imprimir un objeto
//numero 1: es la mas sencilla: concatenar cada valor de la propieddad
console.log('Distinta formas de imprimir un objeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Numero 2: A traves del ciclo for in
console.log('Distinta formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Object.values()
console.log('Distinta formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray)

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Distinta formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ //constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';//Modificacion del nombre
padre.telefono = '435632354'; //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //Utilizamos la funcion
let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //la propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos

//caso objeto 1
let miObjeto = new Object(); //Esta es una opcion formal
//caso objeto 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//caso string 1
let miCadena1 = new String('Hola'); //Sintaxis formal
//caso String 2
let miCadena2 = 'Hola'; //Esta es la sintaxis simplificada y recomendada

//caso con numeros 1
let miNumero = new Number(1); //Es formal no recomendable
//caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada

//caso boolean 1
let miBoolean = new Boolean(false); //Formal
//caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada

//Caso arreglos 1
let miArreglo1 = new Array(); //Formal
//caso arreglos 2
let miArreglo2 = []; //Sintaxis recomendada

//Caso function 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//caso function 2
let miFuncion2 = function(){}; //Sintaxis recomendada

//Uso de prototype
Persona3.prototype.telefono = '2611832340';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '261898433333';
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+ ' '+telefono;
        //return this.nombre+ ' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic', '45454534'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '555-444-5555'));

//Metodo Apply
let arreglo = ['Ing.', '5493232965'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));