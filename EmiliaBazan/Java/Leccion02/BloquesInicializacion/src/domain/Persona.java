/*
 * BloquesInicializacion
 */
package domain;

/*
 * @author Adriana
 */
public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ //Bloque de inicializacion ESTATICO
        System.out.println("Ejecucion de bloque estatico");
        ++Persona.contadorPersonas;
        //idPersona = 10; //un atributo no es estatico por eso aparece error
    }
    { //Bloque de inicializacion NO ESTATICO (contexto dinamico)
        System.out.println("Ejecucion del bloque NO ESTATICO");
        this.idPersona = Persona.contadorPersonas++; //Incrementamos el atributo
    }
    
    //Los bloques de inicializacion se ejecutan antes del constructor
    
    public  Persona(){
        System.out.println("Ejecucion del constructor");
    }
    
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
