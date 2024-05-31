/*
 * InstanceOf
 */
package test;

import domain.*;
/*
 * @author Adriana
 */
public class TestInstanceOf {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
        determinarTipo(empleado1); //test
        empleado1 = new Gerente("José", 5000, "Sistemas");
        //determinarTipo(empleado1); //test
    }
    
    public static void determinarTipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            //((Gerente)empleado).getDepartamento(); //test
            //empleado.getDepartamento(); //test
            Gerente gerente = (Gerente)empleado; //test
            //gerente.getDepartamento(); //test
            //((Gerente) empleado).getDepartamento(); //test
            System.out.println("gerente = "+gerente.getDepartamento()); //test
            //System.out.println("gerente = "+empleado);
        }
        else if(empleado instanceof Empleado){ //test
        //if(empleado instanceof Empleado){ //test
            System.out.println("Es de tipo Empleado");
            //Gerente gerente = (Gerente)empleado; //test
            //System.out.println("gerente = "+gerente.getDepartamento()); //test
        }
        else if(empleado instanceof Object){ //test
        //if(empleado instanceof Object){ //test
            System.out.println("Es de tipo Object");
        }
    }
}
