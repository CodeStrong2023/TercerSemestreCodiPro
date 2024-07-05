/*
 * TestForEach
 */
package test;

import domain.Persona;

/*
 * @author Adriana
 */
public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9}; //sintaxis resumida
        
        for (int edad: edades) { //prueba1 sintaxis del ForEach
        //for (var edad: edades) { //prueba2
            System.out.println("edad =  " + edad);
        }
        Persona personas[] = {new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};
        
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = " + persona);
        }
    }
}
    
    
    
    
    
    

