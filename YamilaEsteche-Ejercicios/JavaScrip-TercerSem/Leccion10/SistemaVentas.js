class Producto{
    static contadorProdutos = 0;
    constructor(nombre, precio){
        this._idProducto = ++Producto.contadorProdutos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto(){
        return this._idProducto;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get precio(){
        return this._precio;
    }

    set precio(precio){
        this._precio = precio;
    }

    toString(){ //Template Literals: nos permite insertar codigo dinamicamente
        return `idProducto : ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`;

    }
} //Fin de la clase Producto

class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODCUTOS(){ //Simula una constante
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    }

    agregarProductos(Producto){
        if(this._productos.length < Orden.getMAX_PRODCUTOS()){
            this._productos.push(Producto); //Tenemos 2 tipos de sintaxis: 1
            //this._productos[this._contadorProductosAgregados++] = producto; //Segunda sintaxis
        }
        else{
            console.log('No se pueden agregar mas productos');
        }
    } //Fin del metodo agregarProducto

    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        }//Fin ciclo forr
        return totalVenta;
    }//Fin del metodo calcularTotal

    mostrarOrden(){
        let productosOrden = ' ';
        for(let producto of this._productos){
            productosOrden += '\n{ '+producto.toString()+' }';
        }//Fin del ciclo for
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productosOrden}`);
    }//Fin metodo mostrarOrden
}//Fin de la clase Orden

let producto1 = new Producto('Pantalon', 200);
let producto2 = new Producto('Camisa', 150);
let producto3 = new Producto('Cinturon', 50);
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProductos(producto1);
orden1.agregarProductos(producto2);
orden1.agregarProductos(producto3);
orden2.agregarProductos(producto1);
orden2.agregarProductos(producto2);
orden2.agregarProductos(producto3);
orden1.mostrarOrden();
orden2.mostrarOrden()