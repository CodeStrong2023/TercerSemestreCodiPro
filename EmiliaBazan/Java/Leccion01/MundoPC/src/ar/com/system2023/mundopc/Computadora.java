package ar.com.system2023.mundopc;

public class Computadora {
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;
    
    
    //Constructor vacío
    private Computadora(){
        this.idComputadora=++Computadora.contadorComputadoras;
    }
    
    //constructor2
    
    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton){
       this();
       this.nombre = nombre;
       this.monitor = monitor;
       this.raton = raton;
       this.teclado = teclado;
     }
   
   public int getidComputadora(){
       return idComputadora;
   }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Monitor getMonitor() {
        return this.monitor;
    }

    public void setMonitor(Monitor monitor) {
        this.monitor = monitor;
    }

    public Teclado getTeclado() {
        return this.teclado;
    }

    public void setTeclado(Teclado teclado) {
        this.teclado = teclado;
    }

    public Raton getRaton() {
        return this.raton;
    }

    public void setRaton(Raton raton) {
        this.raton = raton;
    }

    @Override
    public String toString() {
        return "Computadora{" + "idComputadora=" + idComputadora + ", nombre=" + nombre + ", monitor=" + monitor + ", teclado=" + teclado + ", raton=" + raton + '}';
    }
   
   
}
