/*
 * Conversión de objetos
 */
package test;

import domain.*;

/*
 * @author Adriana
 */
public class TestConversionObjetos {
    public static void main(String[] args){
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        //System.out.println("empleado="+empleado);
        System.out.println(empleado.obtenerDetalles()); //si queremos acceder a métodos Escritor
        //empleado.getTipoEscritura(); //no se puede hacer, marca error
        //Downcasting
        //((Escritor)empleado).getTipoEscritura(); //Tenemos 2 opciones: esta es una
        Escritor escritor = (Escritor)empleado; //esta es la segunda opción
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
