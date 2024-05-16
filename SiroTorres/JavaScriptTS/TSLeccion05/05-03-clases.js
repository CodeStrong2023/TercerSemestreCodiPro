//let persona3 = new Persona('Carla', 'Ponce'); Esto no se debe hacer

class Persona{ //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
}

let persona1 = new Persona('Martin', 'Perez');
//console.log(persona1);
console.log(persona1.nombre);
console.log(persona1.apellido)
persona1.nombre = 'Juan Carlos Bodoque';
console.log(persona1.nombre);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2._nombre)
//console.log(persona2);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//Ejercicios
persona1.apellido = 'Segundo';
console.log(persona1.apellido);
persona2.apellido = 'Paredes';
console.log(persona2.apellido);

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.departamento);
console.log(empleado1.nombre);