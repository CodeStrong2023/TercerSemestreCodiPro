/*
 * Clase Object
 */
package domain;

/*
 * @author Adriana
 */
public enum TipoEscritura {
    CLASICO ("Escritura a mano"),
    MODERNO ("Escritura Digital");
    
    private final String descripcion; //declaración variable
    
    private TipoEscritura(String descripcion){ //constructor
        this.descripcion = descripcion; //marcaba error-corregido
    }
    
    //método get
    public String getDescripcion(){
        return this.descripcion; //marcaba error-corregido
    }
    
}
