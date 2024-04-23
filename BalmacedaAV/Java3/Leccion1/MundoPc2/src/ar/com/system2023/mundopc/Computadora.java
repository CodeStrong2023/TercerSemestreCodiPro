/*
 * MundoPc
 */
package ar.com.system2023.mundopc;

/*
 * @author Adriana
 */
public class Computadora {
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;
    
    //Constructor vacio
    private Computadora(){
        this.idComputadora = ++Computadora.contadorComputadoras;
    }
    //Constructor 2
    public Computadora(String nombre){
        
    }
}
