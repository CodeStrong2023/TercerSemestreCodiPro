
package paquete2;


public class Clase4 {
    private String atributoPrivate = "atributo Privado";
    
    
    private Clase4(){
        System.out.println("Constructor Privado");
    }
    
    //Creamos un constrcutor public para poder crear objetos
    public Clase4(String argumento){ //Aquie se puede llamar al constructor vacio
        this();
        System.out.println("Constructor Publico");
        
    }
    
    //Metodo private 
    private void metodoPrivado(){
        System.out.println("Metodo privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
}
