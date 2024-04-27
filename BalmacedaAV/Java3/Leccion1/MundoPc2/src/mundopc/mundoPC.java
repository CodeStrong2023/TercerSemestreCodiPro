/*
 * MundoPc
 */
package mundopc;

import ar.com.system2023.mundopc.*;

/**
 * @author Adriana
 */
public class mundoPC {
    public static void main(String[] args){
        
        Monitor monitorHP = new Monitor("HP", 13); //Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP"); 
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //Crear otros objetos de diferente marca
        Monitor monitorGamer = new Monitor("Gamer", 32); 
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer"); 
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Orden orden1 = new Orden(); //Inicializar el arreglo vacio
        Orden orden2 = new Orden(); //Nueva lista para el objeto orden2
        //Orden orden3 = new Orden(); //Nueva lista para el objeto orden3
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora computadorasVarias = new Computadora("Computadoras de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);
        
        //Computadora computadoraPerifericosEntrada = new Computadora ("Perifericos de entrada", tecladoHP, tecladoGamer, ratonHP, ratonGamer);
        //orden3.agregarComputadora(computadoraPerifericosEntrada);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        //orden3.mostrar();
         
        //Crear mas objetos de tipo computadora con todos sus elementos
        //Completar una lista en el objeto orden1 que llegue a los 10 elementos
        /*Nuevos elementos: 
        Impresora
        
        
        */
        //Probar de esta manera los metodos al maximo rendimiento
    }
}
