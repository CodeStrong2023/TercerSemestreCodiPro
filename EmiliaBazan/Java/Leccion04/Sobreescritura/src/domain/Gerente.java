/*
 * Sobreescritura
 */
package domain;

/*
 * @author Adriana
 */
public class Gerente extends Empleado{
    private String departamento;
    
    public Gerente(String nombre, double sueldo, String departamento){
        super(nombre, sueldo);
        this.departamento = departamento;
    }
    
    //Sobreescribimos el método
    @Override
    //public String obtenerDetalles(){ //para testeos
    public String obtenerDetalles(){
        return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }
}
