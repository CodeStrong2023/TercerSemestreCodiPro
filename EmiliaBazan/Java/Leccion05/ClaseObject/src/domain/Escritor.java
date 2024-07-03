/*
 * Clase Object
 */
package domain;

import java.util.Objects;

/*
 * @author Adriana
 */
public class Escritor extends Empleado{
    final TipoEscritura tipoEscritura;
    
    public Escritor(String nombre, double sueldo, TipoEscritura tipoEscritura){
        super(nombre, sueldo);
        this.tipoEscritura = tipoEscritura;
    }
    
    //Método para sobreescribir
    @Override
    public String obtenerDetalles(){
        return super.obtenerDetalles()+", Tipo Escritura: "+tipoEscritura.getDescripcion();
    }
    
    @Override
    public String toString(){
        return "Escritor{" + "tipoEscritura=" + tipoEscritura + '}'+" "+super.toString();
    }
    
    public TipoEscritura getTipoEscritura(){
        return this.tipoEscritura;
    }
    
    //Para testear opcion
//    @Override
//    public String obtenerDetalles() {
//        return super.obtenerDetalles() + ", Tipo Escritura: " + tipoEscritura.getDescripcion();
//    }
//
//    @Override
//    public String toString() {
//        return "Escritor{" + "tipoEscritura=" + tipoEscritura + '}' + " " + getClass().getSimpleName() + "[nombre=" + nombre + ", sueldo=" + sueldo + "]";
//    }
//
//    @Override
//    public boolean equals(Object obj) {
//        if (this == obj) {
//            return true;
//        }
//        if (obj == null || getClass()!= obj.getClass()) {
//            return false;
//        }
//        Escritor other = (Escritor) obj;
//        return tipoEscritura == other.tipoEscritura && super.equals(other);
//    }
//
//    @Override
//    public int hashCode() {
//        return Objects.hash(tipoEscritura, super.hashCode());
//    }
//
//    public TipoEscritura getTipoEscritura() {
//        return this.tipoEscritura;
//    }
}
