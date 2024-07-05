/*
 * Modificadores de acceso
    Default o package
 */
package paquete1;

/*
 * @author Adriana
 */
class Clase2 extends Clase1{
    String atributoDefault = "Valor del atributo default";
    
//    Clase2(){
//        System.out.println("Constructor Default");
//    }
    public Clase2(){
        super();
        this.atributoDefault = "Modificación del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
    
    void metodoDefault(){
        System.out.println("Método Default");
    }
}
