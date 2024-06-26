import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Persona {  //Comienzo del código para probar 
    private String nombre;
    private String telefono;
    private String correo;

    public Persona(String nombre, String telefono, String correo) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.correo = correo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public String getCorreo() {
        return correo;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", telefono='" + telefono + '\'' +
                ", correo='" + correo + '\'' +
                '}';
    }
}  //Fin del código para probar

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        List<Persona> personas = new ArrayList<>();  //Definimos la lista fuera del ciclo while
        
        var salir = false; //Empezamos con el menu
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e){
                System.out.println("Ocurrio un error: "+e.getMessage());
            }
            System.out.println();
        }//Fin del ciclo while

    }//Fin metodo main
    private static void mostrarMenu(){
        //Mostramos las opciones
        System.out.print("""
                ******Listado de personas ******
                1. Agregar
                2. Listar
                3. Salir
                """);
        System.out.print("Digite una de las opciones: ");
    } //Fin del metodo mostrarMenu

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        
        switch (opcion){  //Revisamos la opcion digita a traves de un switch
            case 1 -> {//Agregar una persona a la lista
                System.out.print("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.print("Digite el correo: ");
                var email = entrada.nextLine();
                
                var persona = new Persona(nombre,tel, email);  //Creamos el objeto persona
                
                personas.add(persona);  //Agregamos la persona a la lista
                System.out.println("La lista tiene: "+ personas.size()+" elementos");
            }//Fin caso 1
            case 2 -> { //Listar a las personas
                System.out.println("Listado de personas: ");
                //Mejoras con lambda y el metodo de referencia
                personas.forEach((persona) -> System.out.println(persona));
                //personas.forEach(System.out::println);
                //puntos dobles :: se conoce como metodo de referencia
                //iteramos cada uno de los objetos de la clase persona para mostrarlos
            }//Fin caso 2
            case 3 -> {//Salir del ciclo
                System.out.println("Hasta pronto...");
                salir = true;
            }//Fin caso 3
            default -> System.out.println("Opcion incorrecta: "+opcion);
        }//Fin del switch
        return salir;
    }//fin del metodo ejecutarOperacion
}//Fin de la clase ListadoPersonasApp