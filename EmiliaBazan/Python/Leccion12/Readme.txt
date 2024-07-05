Sobrecarga de un operador:
Significa que un mismo operador puede comportarse de diferentes formas.

Operador de suma (+)
Es un buen ejemplo de la Sobrecarga de operadores
Este operador se puede comportar de distintas maneras dependiendo si está trabajando con tipos String,
con tipos enteros o por ejemplo con tipos lista.

Dependiendo del tipo con el que esté trabajando, es el tipo de resultado que vamos a obtener.
Por lo tanto, un mismo operador puede trabajar de distintas formas.
Esto se conoce como Sobrecarga de operadores.

Caso 1
a = 2
b = 3
print(a + b)

Caso 2
a = 'Hola '
b = 'Mundo'
print(a + b)

El segundo caso, en lugar de obtener una suma, obtenemos una concatenación de tipos String de tipos cadenas,
con eso estamos obteniendo la Sobrecarga del operador.

Si tenemos tipos numéricos, se comporta de una forma, y si tenemos  tipos Strings se comporta de otra forma.

Agregamos unas listas:
a = [3, 4, 5]
b = [6, 7, 8, 9]
print(a + b)
Se va a comportar de manera diferente, obtenemos la unión de los dos listas, creando una sola.
Es el mismo operador, pero dependiendo del tipo de dato con el que estemos trabajando va a ser el resultado.

La Pregunta es si esto mismo lo podemos hacer con clases en Python.
La respuesta es que sí, pero tenemos que agregar la Sobrecarga de un método dependiendo del operador que 
queramos sobrecargar.

Por ejemplo, esta es la lista de métodos según el operador que queramos sobrecargar.
Todos están definidos en la clase object

Operadores Aritméticos      magic method
+                           __add__(self, other)
-                           __sub__(self, other)
*                           __mul__(self, other)
/                           __truediv__(self, other)
//                          __floordiv__(self, other)
%                           __mod__(self, other)
**                          __pow__(self, other)

Operador Comparación (lógicos)
<                           __lt__(self, other)
>                           __gt__(self, other)
<=                          __le__(self, other)
>=                          __ge__(self, other)
==                          __eq__(self, other)
!=                          __ne__(self, other)

Entonces tenemos que sobreescribir el método respectivo definido en la clase object.
Si queremos sobrecargar la suma, tenemos que sobreescribir el método de aad.

Todos so métodos de tipo dunder.
Esto quiere decir que está definido en la clase Object.

Si queremos sobrecargar el operador de resta, entonces tenemos que sobreescribir el método de sub.

La sobrecarga y la escritura son dos conceptos diferentes.
La sobrecarga de un operador significa que se puede comportar de maneras distintas dependiendo de los
operandos con los cuales esté trabajando y la sobreescritura tiene que ver con herencia.

En este caso estaríamos sobreescribiendo un método definido en una clase padre.
Son conceptos muy distintos.
La sobrecarga de operadores y la sobreescritura de métodos.

Operadores de asignación(compuestos)        magic method
-=                                          __isub__(self, other)
+=                                          __iadd__(self, other)
*=                                          __imul__(self, other)
/=                                          __idiv__(self, other)
//=                                         __ifloordiv__(self, other)
%=                                          __imod__(self, other)
**=                                         __ipow__(self, other)
Aquí están todas estas tablas con todos los operadores que podemos sobrecargar.

Tenemos también más operadores, como pueden ser los operadores de menor que, mayor que, 
menor, igual que etc.
También los operadores, como pueden ser operadores compuestos de menor, igual, mayor igual, etc.
También los Operadores unarios con los cuales solamente trabajamos con un solo operando.

Operadores unarios          magic method
-                           __neg__(self, other)
+                           __pos__(self, other)
~                           __invert__(self, other)

Tabla para el caso que necesiten sobrecargar alguna de estos operadores.

Ahora saben cuál es el método que tienen que sobreescribir de la clase Object.


