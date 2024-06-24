
package mundopc;

import ar.com.system2024.mundopc.Computadora;
import ar.com.system2024.mundopc.Monitor;
import ar.com.system2024.mundopc.Orden;
import ar.com.system2024.mundopc.Raton;
import ar.com.system2024.mundopc.Teclado;


public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13);
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP,tecladoHP,ratonHP);
        
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer,tecladoGamer,ratonGamer);
        
        Orden order1 = new Orden();
        Orden order2 = new Orden();
        order1.agregarComputadora(computadoraHP);
        order1.agregarComputadora(computadoraGamer);
        order1.mostrarOrden();
        
        //Crear mas objetos de tipo computadora con todos sus elementos 
        //completar una lista en el objeto orden1 que llegue a los 10 elementos
        //probar de esta manera los metodos al maximo rendimiento
        
        // Crear más objetos de tipo Computadora
        Monitor monitorDell = new Monitor("Dell", 27);
        Teclado tecladoDell = new Teclado("USB", "Dell");
        Raton ratonDell = new Raton("USB", "Dell");
        Computadora computadoraDell = new Computadora("Computadora Dell", monitorDell, tecladoDell, ratonDell);

        Monitor monitorAsus = new Monitor("Asus", 24);
        Teclado tecladoAsus = new Teclado("Bluetooth", "Asus");
        Raton ratonAsus = new Raton("Bluetooth", "Asus");
        Computadora computadoraAsus = new Computadora("Computadora Asus", monitorAsus, tecladoAsus, ratonAsus);

        Monitor monitorAcer = new Monitor("Acer", 22);
        Teclado tecladoAcer = new Teclado("USB", "Acer");
        Raton ratonAcer = new Raton("USB", "Acer");
        Computadora computadoraAcer = new Computadora("Computadora Acer", monitorAcer, tecladoAcer, ratonAcer);

        // Agregar las computadoras adicionales a la orden
        order1.agregarComputadora(computadoraDell);
        order1.agregarComputadora(computadoraAsus);
        order1.agregarComputadora(computadoraAcer);

        // Mostrar la orden actualizada con 10 elementos
        order1.mostrarOrden();

    }
}
