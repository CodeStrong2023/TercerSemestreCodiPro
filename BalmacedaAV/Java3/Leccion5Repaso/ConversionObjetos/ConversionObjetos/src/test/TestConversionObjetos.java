
package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        System.out.println("empleado ="+ empleado); //test
        System.out.println(empleado.obtenerDetalles());//para acceder a métodos escritor
        //empleado.getTipoEscrritura();
        //Downcasting
        //((Escritor)empleado).getTipoEscritura(); //tenemos 2 opciones: esta es una
        Escritor escritor = (Escritor)empleado; //esta es la segunda opcion
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
