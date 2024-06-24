
package ar.com.system2024.mundopc;

public class Teclado extends DispositivoEntrada {
    private final int idTeclado;
    private static int contadorTeclado;
    
    public Teclado(String tipoEntrada, String marca){
        super(tipoEntrada, marca);
        this.idTeclado = ++Teclado.contadorTeclado;
    }

    @Override
    public String toString() {
        return  "Teclado{" + "idTeclado" + ", " + super.toString()+'}';
    }
}

