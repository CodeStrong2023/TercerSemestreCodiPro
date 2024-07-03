
package domain;

import java.io.Serializable;

public class Persona implements Serializable{
    private String nombre;
    private String apellido;
    
    //constructor vacio es OBLIGATORIO para ser considerado Java Beans
    public Persona(){
        
    }
    public Persona(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
    //en Java Beans los getters and setter debe ser encapsulados
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
}
