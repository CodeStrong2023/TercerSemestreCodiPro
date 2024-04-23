/*
 * MundoPc
 */
package ar.com.system2023.mundopc;

/*
 * @author Adriana
 */
public class Orden {
    private final int idOrden;
    private Computadora computadora[]; //Arreglo de objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORES = 10;
    private int contadorComputadora;
    
    //Constructor vacio
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORES];
        
    }
    //Metodo para agregar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora){
        if(this.contadorComputadora < Orden.MAX_COMPUTADORES){
            this.computadora[this.contadorComputadora++] = computadora;
        }
    }
}
