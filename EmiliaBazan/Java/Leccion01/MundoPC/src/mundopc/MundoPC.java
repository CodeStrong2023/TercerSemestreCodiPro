package mundopc;

import ar.com.system2023.mundopc.*;

public class MundoPC {

    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13);//import class
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        //Creamos otros objetos
        Monitor monitorGamer = new Monitor("Gamer", 32);//import class
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorHP, tecladoHP, ratonHP);

        Monitor monitorSamsung = new Monitor("Samsung", 24);//import class
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("USB", "Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", monitorHP, tecladoHP, ratonHP);
        
        Monitor monitorLG = new Monitor("LG", 24);//import class
        Teclado tecladoLG = new Teclado("USB", "LG");
        Raton ratonLG = new Raton("Bluetooth", "LG");
        Computadora computadoraLG = new Computadora("Computadora LG", monitorHP, tecladoHP, ratonHP);
        
        Monitor monitorDell = new Monitor("Dell", 24);//import class
        Teclado tecladoDell = new Teclado("Bluetooth", "Dell");
        Raton ratonDell = new Raton("Bluetooth", "Dell");
        Computadora computadoraDell = new Computadora("Computadora Dell", monitorHP, tecladoHP, ratonHP);
        
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora ComputadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        Computadora ComputadorasVarias1 = new Computadora("Multimarca", monitorSamsung, tecladoDell, ratonLG);
        Computadora ComputadorasVarias2 = new Computadora("Multimarca", monitorSamsung, tecladoLG, ratonDell);
        
        orden2.agregarComputadora(ComputadorasVarias);
        orden2.agregarComputadora(ComputadorasVarias1);
        orden2.agregarComputadora(ComputadorasVarias2);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();

    }

}
