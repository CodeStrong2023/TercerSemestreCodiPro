/*
 * Modificadores de acceso
    Private
 */
package paquete2;

/*
 * @author Adriana
 */
public class Clase4 {
    private String atributoPrivate = "Atributo Privado";
    
    private Clase4(){
        System.out.println("Constructor privado");
    }
    
    //Creamos un constructor public para poder crear objetos
    public Clase4(String argumento){ //aquí se puede llamar al constructor vacio
        System.out.println("Constructor público");
    }
    
    //Método private
    private void metodoPrivado(){
        System.out.println("Método privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
    

}
