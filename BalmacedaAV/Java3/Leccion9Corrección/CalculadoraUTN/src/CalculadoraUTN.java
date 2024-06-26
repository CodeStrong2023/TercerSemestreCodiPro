import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true){ //ciclo infinito
            System.out.println("******* Aplicacion Calculadora *******");
            mostrarMenu();
            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {

                    ejecutarOperacion(operacion, entrada);
                } //Fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto... ");
                    break; //rompe el ciclo y sale
                } else {
                    System.out.println("Opcion erronea: " + operacion);
                }
                //Imprimir un salto de linea antes de repetir el menu
                System.out.println();
            } catch (Exception e){ //Fin del try y comienzo del catch
                System.out.println("Ocurrio un error: "+e.getMessage());
            }
        } //Fin while
    } //Fin main

    private static void mostrarMenu(){
        //mostrar el menu
        System.out.println("""
                       1. Suma
                       2. Resta
                       3. Multplicacion
                       4. Division
                       5. Salir
                       """);
        System.out.print("Operacion a ralizar? ");
    } //Fin metodo mostrarMenu

    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando 1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando 2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> { //suma
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: " + resultado);
            }
            case 2 -> { //resta
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: " + resultado);
            }
            case 3 -> { //mutiplicacion
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicacion: " + resultado);
            }
            case 4 -> { //division
                resultado = operando1 / operando2;
                System.out.println("Resultado de la division: " + resultado);
            }
            default -> System.out.println("Opcion erronea: " + operacion);
        } //Fin switch
    } //Fin metodo ejecutar
}//Fin clase
