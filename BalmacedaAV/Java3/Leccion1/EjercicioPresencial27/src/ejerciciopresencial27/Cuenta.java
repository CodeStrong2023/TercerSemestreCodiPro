/*
 * crear una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tenere decimales)
Crear dos constructores que cumpla lo anterior
crear sus métodos get, set y toString

Tendrá dos métodos especiales:
ingresar(double cantidad): se ingresa una cantidada a la cuenta
si la cantidad es negativa, no se hará nada

retirar(double cantidad): se retira una cantidad a la cuenta,
si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0
 */
package ejerciciopresencial27;

/*
 * @author Adriana
 */
public class Cuenta {
        // Atributos
    private String titular;
    private double cantidad;

    // Constructores
    // Constructor con titular y con cantidad
    public Cuenta(String titular, double cantidad) {
        this.titular = titular;
        this.cantidad = cantidad;
    }

    // Constructor titular, cantidad es 0.0 por defecto
    public Cuenta(String titular) {
        this(titular, 0.0);
    }

    // Getters and Setters
    public String getTitular() {
        return titular;
}

    public void setTitular(String titular) {
        this.titular = titular;
    }

    public double getCantidad() {
        return cantidad;
    }

    public void setCantidad(double cantidad) {
        this.cantidad = cantidad;
    }

    // toString metodo
    @Override
    public String toString() {
        return "Cuenta [titular=" + titular + ", cantidad=" + cantidad + "]";
    }

    // Metodo especial
    public void ingresar(double cantidad) {
        if (cantidad >= 0) {
            this.cantidad += cantidad;
        }
    }

    public void retirar(double cantidad) {
        if (this.cantidad - cantidad >= 0) {
            this.cantidad -= cantidad;
        } else {
            this.cantidad = 0.0;
        }
    }
 
}
