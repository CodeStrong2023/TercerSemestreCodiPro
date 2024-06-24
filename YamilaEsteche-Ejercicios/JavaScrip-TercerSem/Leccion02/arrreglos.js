
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);


console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]);
}

autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); 
console.log(autos);

autos[autos.length] = 'Porche';
console.log(autos);

//Tercera forma de agregar elementos
autos[6] = 'Renault';
console.log(autos);

console.log(Array.isArray(autos)); 

console.log(autos instanceof Array);
//Preguntamos si la variable es una instancia de la clase Array!!
