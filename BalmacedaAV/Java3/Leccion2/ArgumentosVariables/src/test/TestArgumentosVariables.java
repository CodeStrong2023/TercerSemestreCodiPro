/*
 * ArgumentosVariables
 */
package test;

/*
 * @author Adriana
 */
public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        variosParametros("Juan", "Perez", 7, 8, 9);
    }
    private static void variosParametros(String nombre, String apellido, int...numeros){
        System.out.println("Nombre: " + nombre + "Apellido : " + apellido); //Se imprime sin salto de linea
        //System.out.println("Apellido: " + apellido); //Para ahorrar lineas de codigo se escribe arriba
        imprimirNumeros(numeros);
    }
    private static void imprimirNumeros(int ...numeros){
        for (int i = 0; i < numeros.length; i++){
            System.out.println("Elementos: " + numeros[i]);
        }
    } 
}
