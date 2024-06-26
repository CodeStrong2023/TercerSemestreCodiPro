
package excepciones;


public class OperacionExcepcion extends RuntimeException{
    //constructor
    public OperacionExcepcion(String mensaje){
        super(mensaje);
    }
}
