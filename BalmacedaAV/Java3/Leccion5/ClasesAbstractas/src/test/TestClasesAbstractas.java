/*
 * Clases abstractas
 */
package test;

import domain.*;

/*
 * @author Adriana
 */
public class TestClasesAbstractas {
    public static void main(String[] args) {
        FiguraGeometrica figura = new Rectangulo("Rectangulo");
        figura.dibujar();
    }
}
