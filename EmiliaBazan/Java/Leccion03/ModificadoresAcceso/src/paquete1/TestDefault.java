/*
 * Modificadores de acceso
    Default
 */
package paquete1;

import paquete2.Clase4;

/*
 * @author Adriana
 */
public class TestDefault {
    public static void main(String[] args) {
        //Clase2 clase2 = new Clase2();
        ClaseHija2 claseH2 = new ClaseHija2();
        claseH2.atributoDefault = "Cambio desde la prueba";
        System.out.println("claseH2 atributoDefault = " + claseH2.atributoDefault);
        
        Clase4 clase4 = new Clase4("Público");
        System.out.println(clase4.getAtributoPrivate());
        clase4.setAtributoPrivate("Cambio");
        System.out.println("clase4 = " + clase4.getAtributoPrivate());
    }
}
