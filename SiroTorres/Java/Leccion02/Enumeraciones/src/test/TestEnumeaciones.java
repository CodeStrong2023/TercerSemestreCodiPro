
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;


public class TestEnumeaciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: "+Dias.LUNES);
        //indicarDiaSemana(Dias.DOMINGO); //Las enumaeraciones se tratan como cadenas
        //Ahora no se deeben utilizar comillas, se accede a traves de el operador del punto
        System.out.println("Continente No. 1: "+Continentes.AFRICA);
        System.out.println("No. de paises en el 1er continente: "+
                Continentes.AFRICA.getPaises());
        System.out.println("No. de habitantes en el 1er continente: "+
                Continentes.AFRICA.getHabitantes());
        
        System.out.println("Continente No. 2: "+Continentes.EUROPA);
        System.out.println("No. de paises en el 2do continente: "+
                Continentes.EUROPA.getPaises());
        System.out.println("No. de habitantes en el 2do continente: "+
                Continentes.EUROPA.getHabitantes());
        
        System.out.println("Continente No. 3: "+Continentes.ASIA);
        System.out.println("No. de paises en el 3er continente: "+
                Continentes.ASIA.getPaises());
        System.out.println("No. de habitantes en el 3er continente: "+
                Continentes.ASIA.getHabitantes());
        
        System.out.println("Continente No. 4: "+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to continente: "+
                Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes en el 4to continente: "+
                Continentes.AMERICA.getHabitantes());
        
        System.out.println("Continente No. 5: "+Continentes.OCEANIA);
        System.out.println("No. de paises en el 4to continente: "+
                Continentes.OCEANIA.getPaises());
        System.out.println("No. de habitantes en el 4to continente: "+
                Continentes.OCEANIA.getHabitantes());
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
                System.out.println("Quinto dia de la semana. Empieza el finde :p");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;
            default:
                System.out.println("Lo indicado no corresponde a un dia de la semana");
        }
    }
}
