
package domain;


public class Rectangulo extends FiguraGeometrica {
    
    public Rectangulo(String tipoFigura){  //constructor
        super(tipoFigura);
    }
    
    @Override
    public void dibujar(){ //implementar el metodo
        System.out.println("Se imprime un: "+this.getClass().getSimpleName());
    }
}

