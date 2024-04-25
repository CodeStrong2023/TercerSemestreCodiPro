
package test;

public class TestAutoBoxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        /*
            Clases envolventes de tipos primitivos
            int = la clase envolvente es Integer
            long = la clase envolvente es Long
            float = la clase envolvente es Float
            double = La clase envolvente es double
            boolean = la clase envolvente es boolean
            byte = la clase envolvente es Byte
            char = la clase envolvente es Character
            short = la clase envolvente es Short
        */
        
        int enteroPrim = 10; //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //Tipo object con la clase Integer
        System.out.println("entero = " + entero.toString());
        //Con la clase integer podemos convertir el numero de la clase entero en una cadena
        System.out.println("entero = " + entero.doubleValue());
        //Autobixing es cuando pasamos un valor primitivo lo convertimos a otro tipo
        
        int entero2 = entero; //Unboxing es pasar un valor al tipo primitivo
        System.out.println("entero2 = " + entero2);
        
        
    }
}
