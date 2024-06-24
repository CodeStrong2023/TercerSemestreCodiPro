
package test;

import domain.Persona;


public class TestBloqueinicializacion {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        System.out.println("Persona1= "+ persona1);
        Persona persona2 = new Persona();
        System.out.println("Persona2 = "+ persona2);
    }
}
