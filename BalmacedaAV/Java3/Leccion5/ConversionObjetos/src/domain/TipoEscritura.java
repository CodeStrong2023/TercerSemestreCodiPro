/*
 * Conversión de objetos
 */
package domain;

/*
 * @author Adriana
 */
public enum TipoEscritura {
    CLASICO ("Escritura a mano"),
    MODERNO("Escritura digital");
    
    private String descripcion; //declaración variable
    
    private TipoEscritura(String descripcion){ //Constructor
        this.descripcion = descripcion; //marca error
    }
    
    //Método get
    
    public String getDescripcion(){
        return this.descripcion; //marca error
    }
}
