
package test;

import static aritmetica.Aritmetica.division;
import excepciones.OperacionExcepcion;


public class TestExcepciones {
    public static void main(String[] args) {
        int resultado = 0;
        try{
            resultado = division(10, 0);
        }catch(OperacionExcepcion e){  //se pueden agregar + catch respetando jerarquias de clases          
            //las de menor jerarquía arriba y las de menor jerarquia abajo
            System.out.println("Oucrrio un error de tipo OperacionExcepcion");
            System.out.println(e.getMessage());
        }catch(Exception e){
            System.out.println("Ocurrio un Error");
            e.printStackTrace(System.out); //es la pila de excepciones
            System.out.println(e.getMessage());
        }
        finally{
            System.out.println("Se reviso la division entre cero"); //con o sin excepciones el finally
            // siempre se ejecuta
        }
        System.out.println("La variable de resultado tiene como valor: "+resultado);
    }
}
