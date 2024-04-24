
package mundopc;

import ar.com.system2023.mundopc.*;


public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); //Importar la clase 
        Teclado tecladoRedDragon = new Teclado("Bluetooth", "RedDragon");
        Raton ratonRedDragon = new Raton("USB","RedDragon");
       
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoRedDragon, ratonRedDragon);
        //Completar una lista en el objeto orden1 que llegue a los 10 elementos
        Monitor monitorAoc = new Monitor("AOC", 28);
        Teclado tecladoLogiTech = new Teclado("USB", "LogiTech");
        Raton ratonLogitech = new Raton("USB", "Logitech");
        
        Computadora computadoraAOC = new Computadora("Computadora AOC", monitorAoc, tecladoLogiTech, ratonLogitech);
        
        Monitor monitorAcer = new Monitor("Acer", 32);
        Teclado tecladoAcer = new Teclado("Bluetooth", "Acer");
        Raton ratonAcer = new Raton("USB", "Acer");
        
        Computadora computadoraAcer = new Computadora("Computadora Acer", monitorAcer, tecladoAcer, ratonAcer);
        
        
   
        Monitor monitorGamer = new Monitor("Viewsonic", 23); //Importar la clase 
        Teclado tecladoViewsonic = new Teclado("USB", "Viewsonic");
        Raton ratonViewsonic = new Raton("USB","Gamer" );
        Computadora computadoraIntel = new Computadora("ComputadoraIntel", monitorGamer, tecladoViewsonic, ratonViewsonic);
        Orden orden1 = new Orden();//Inicializamos el arreglo
        Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraIntel);
        orden1.agregarComputadora(computadoraAOC);
        orden1.agregarComputadora(computadoraAcer);
        
        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoViewsonic, ratonViewsonic);
        orden2.agregarComputadora(computadorasVarias); 
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
        //Crear mas objetos de tipo computadora con todos sus elementoos
        //Completar una lista en el objeto orden1 que llegue a los 10 elementos
        //probar de esta manera los metodos al maximo rendimiento
        
        Monitor monitorAOC = new Monitor ("AOC", 29);
        Teclado tecladoNova = new Teclado("Bluetooth", "Nova");
        Raton ratonNova = new Raton("USB", "Nova");
        
        Computadora computadoraNova = new Computadora("Computadora Nova", monitorAOC, tecladoNova, ratonNova);
        Orden orden3 = new Orden();
        orden3.agregarComputadora(computadoraNova);
        orden3.mostrarOrden();
        
        
        
        
        
    }
}
