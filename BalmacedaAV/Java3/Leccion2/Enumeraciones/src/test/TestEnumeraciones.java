/*
 * Enumeraciones
 */
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

/*
 * @author Adriana
 */
public class TestEnumeraciones {
    public static void main(String[] args) {
        /*System.out.println("Dia 1: " + Dias.LUNES);
        indicarDiaSemana(Dias.LUNES); //Las enumeraciones se tratan como cadenas
        //No se debene utilizar comillas, se accede a traves del operador de punto
        System.out.println("Dia 2: " + Dias.MARTES);
        indicarDiaSemana(Dias.MARTES);
        
        System.out.println("Dia 3: " + Dias.MIERCOLES);
        indicarDiaSemana(Dias.MIERCOLES);
        
        System.out.println("Dia 4: " + Dias.JUEVES);
        indicarDiaSemana(Dias.JUEVES);
        
        System.out.println("Dia 5: " + Dias.VIERNES);
        indicarDiaSemana(Dias.VIERNES);
        
        System.out.println("Dia 6: " + Dias.SABADO);
        indicarDiaSemana(Dias.SABADO);
        
        System.out.println("Dia 7: " + Dias.DOMINGO);
        indicarDiaSemana(Dias.DOMINGO);*/
        
        System.out.println("Continente n° 4: " + Continentes.AMERICA);
        System.out.println("N° de paises en el 4to continente: "
            + Continentes.AMERICA.getPaises());
          System.out.println("N° de gabitantes en el 4to continente: "
            + Continentes.AMERICA.getHabitantes());
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break; 
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;     
        }
        /*Ejercicio: 
        agregar todos los días de la semana
        agregar default
        */
    }
}
