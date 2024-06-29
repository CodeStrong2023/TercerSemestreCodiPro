import tkinter as tk
from tkinter import simpledialog, messagebox
from typing import Any, List

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
from sqlalchemy.orm import Session as SessionType


##################################################
#          Modelos: Base de datos                #
##################################################


class Base(DeclarativeBase):
    pass


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    nombre = Column(String(50), nullable=False)
    precio = Column(Float(3), nullable=False)
    cantidad_disponible = Column(Integer, nullable=False)
    cantidad_comprada = Column(Integer, nullable=False)

    def __init__(
            self,
            nombre: str,
            precio: float,
            cantidad_disponible: int,
            cantidad_comprada: int,
            **kw: Any,
    ):
        super().__init__(
            nombre=nombre,
            precio=precio,
            cantidad_disponible=cantidad_disponible,
            cantidad_comprada=cantidad_comprada,
            **kw,
        )

    def __repr__(self):
        return f"Producto(id={self.id}, nombre={self.nombre}, precio={self.precio}, cantidad_disponible={self.cantidad_disponible}, cantidad_comprada={self.cantidad_comprada})"


class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True)
    nombre_cliente = Column(String(100), nullable=False)
    direccion_cliente = Column(String(100), nullable=False)
    localidad = Column(String(100), nullable=False)
    costo_total = Column(Float(3), nullable=False)
    pago_realizado = Column(Boolean, nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)

    producto = relationship("Producto")

    def __init__(
            self,
            nombre_cliente: str,
            direccion_cliente: str,
            localidad: str,
            costo_total: float,
            pago_realizado: bool,
            producto_id: int,
            **kw: Any,
    ):
        super().__init__(
            nombre_cliente=nombre_cliente,
            direccion_cliente=direccion_cliente,
            localidad=localidad,
            costo_total=costo_total,
            pago_realizado=pago_realizado,
            producto_id=producto_id,
            **kw,
        )

    def __repr__(self):
        return f"Compra(id={self.id}, nombre_cliente={self.nombre_cliente}, direccion_cliente={self.direccion_cliente}, localidad={self.localidad}, costo_total={self.costo_total})"


##########################################################
#     Clase para manejar Consultas Sql En General        #
##########################################################


class Query:

    def __init__(self, session: SessionType):
        self.session = session

    def get_all(self, model):
        # Retorna todos los registros de un modelo.
        return self.session.query(model).all()

    def get_by_id(self, model, id: int):
        # Retorna un registro por su ID.
        return self.session.query(model).get(id)

    def get_one(self, model, **kwargs):
        # Retorna el primer registro que cumpla con los filtros
        return self.session.query(model).filter_by(**kwargs).first()

    def add(self, instance):
        # Agrega una nueva instancia a la base de datos.
        self.session.add(instance)
        self.session.commit()

    def update(self):
        # Guarda (commit) los cambios realizados en la sesión.
        self.session.commit()

    def delete(self, instance):
        # Elimina una instancia de la base de datos.
        self.session.delete(instance)
        self.session.commit()

    def filter_by(self, model, **kwargs):
        # Retorna registros que cumplan con los filtros especificados.
        return self.session.query(model).filter_by(**kwargs).all()

    def execute_raw_query(self, raw_query):
        # Ejecuta una consulta SQL en crudo.
        return self.session.execute(raw_query).fetchall()

    def close_session(self):
        self.session.close()
        self.session = None


#############################################################
#    Clase para manejar consultas especificas con tipos     #
#############################################################


class TypedQuery(Query):

    def __init__(self, session: SessionType):
        super().__init__(session)

    def obtener_productos(self) -> List[Producto]:
        return self.get_all(Producto)

    def obtener_compras(self) -> List[Compra]:
        return self.get_all(Compra)

    def obtener_producto(self, **kw) -> None | Producto:
        return self.get_one(Producto, **kw)

    def obtener_compra(self, **kw) -> None | Compra:
        return self.get_one(Compra, **kw)

    def registrar_compra(self, **kw) -> None:
        nueva_compra = Compra(**kw)
        self.add(nueva_compra)


############################################################


class CompraActual:
    def __init__(self):
        self._nombre_cliente: str | None = None
        self._direccion_cliente: str | None = None
        self._localidad: str | None = None
        self._costo_total: float | None = None
        self._pago_realizado: bool | None = None
        self._producto_id: int | None = None

    # Getters
    def get_nombre_cliente(self) -> str | None:
        return self._nombre_cliente

    def get_direccion_cliente(self) -> str | None:
        return self._direccion_cliente

    def get_localidad(self) -> str | None:
        return self._localidad

    def get_costo_total(self) -> float | None:
        return self._costo_total

    def get_pago_realizado(self) -> bool | None:
        return self._pago_realizado

    def get_producto_id(self) -> int | None:
        return self._producto_id

    # Setters
    def set_nombre_cliente(self, nombre_cliente: str | None) -> None:
        self._nombre_cliente = nombre_cliente

    def set_direccion_cliente(self, direccion_cliente: str | None) -> None:
        self._direccion_cliente = direccion_cliente

    def set_localidad(self, localidad: str | None) -> None:
        self._localidad = localidad

    def set_costo_total(self, costo_total: float | None) -> None:
        self._costo_total = costo_total

    def set_pago_realizado(self, pago_realizado: bool | None) -> None:
        self._pago_realizado = pago_realizado

    def set_producto_id(self, producto_id: int | None) -> None:
        self._producto_id = producto_id


##########################################################
#           Funciones auxiliares                         #
##########################################################


def elegir_codigo_postal(matriz):
    costo_de_envio = 0
    postal = False

    matriz_texto = "\n".join(" ".join(map(str, fila)) for fila in matriz)
    messagebox.showinfo(
        "Información",
        "A continuación vera las opciones de entrega a domicilio que tenemos para ofrecer dentro de Mendoza",
    )

    while not postal:
        codigo_str = simpledialog.askstring(
            "Código Postal",
            "Digite el código postal al que quiere recibir su pedido:\n" + matriz_texto,
        )
        if codigo_str is None:
            mostrar_mensaje_despedida()
            return None

        try:
            codigo = int(codigo_str)
        except ValueError:
            messagebox.showerror("Error", "El código postal debe ser un número entero")
            continue

        nuevo_costo = {
            5515: 1000,
            5521: 1200,
            5501: 1300,
            5500: 1400,
            5539: 1550,
            5507: 1700,
            5600: 0,
            5613: 0,
            5620: 0,
        }.get(codigo, -1)

        if nuevo_costo >= 0:
            messagebox.showinfo(
                "Costo de envío", f"El costo de envío es de ${nuevo_costo}"
            )
            costo_de_envio = nuevo_costo
            postal = True
        else:
            messagebox.showerror(
                "Error",
                "El código postal que indicó no está dentro de nuestras zonas de envíos a Domicilio",
            )
            respuesta = messagebox.askyesno(
                "¿Desea volver a intentar?", "¿Desea volver a intentar?"
            )
            if not respuesta:
                messagebox.showinfo(
                    "Información",
                    "Lo invitamos a visitar la sucursal de forma presencial y ser atendido por nuestro personal.",
                )
                break

    if postal:
        while True:
            direc = simpledialog.askstring(
                "Dirección",
                "Digite su calle, dirección y el envío llega en las primeras 24 horas desde que usted realiza el pago",
            )
            if direc:  # Verificar si la dirección no está vacía
                messagebox.showinfo(
                    "Dirección", f"Usted ingresó la siguiente dirección: {direc}"
                )

                break  # Salir del bucle si la dirección es válida
            else:
                messagebox.showerror(
                    "Error",
                    "Debe ingresar una dirección válida. Por favor, inténtelo nuevamente.",
                )

    compra_actual.set_direccion_cliente(direc)
    compra_actual.set_localidad(f"{codigo}")

    return costo_de_envio


def agregar_producto(productos: List[Producto]):
    codigop = False
    precio = 0

    lista_productos = ""

    for i in range(0, len(productos)):

        # Si no hay productos disponibles no se muestra
        if productos[i].cantidad_disponible <= 0:
            continue

        lista_productos += f"{i}. {productos[i].nombre} ({productos[i].precio})"
        lista_productos += "\n"

    while not codigop:
        producto_index = simpledialog.askstring(
            "Producto", "Digite el CÓDIGO del producto que desea:\n" + lista_productos
        )

        if producto_index is None:
            mostrar_mensaje_despedida()
            return None

        try:
            producto_index = int(producto_index)
        except ValueError:
            messagebox.showerror(
                "Error", "El código del producto debe ser un número entero"
            )
            continue

        precio_producto = productos[producto_index].precio

        if precio_producto >= 0:
            messagebox.showinfo(
                "Precio del producto",
                f"El PRECIO del producto es de ${precio_producto}",
            )
            precio = precio_producto
            compra_actual.set_producto_id(productos[producto_index].id)
            codigop = True
        else:
            messagebox.showerror("Error", "Producto no registrado, ingrese otro CÓDIGO")
            respuesta = messagebox.askyesno(
                "¿Desea continuar?", "¿Desea continuar con la compra del producto?"
            )
            if not respuesta:
                messagebox.showinfo(
                    "Información",
                    "Comuníquese con Atención al cliente o reingrese nuevamente el CÓDIGO del producto",
                )
                break

    while codigop:
        nombre = simpledialog.askstring(
            "Datos",
            "A continuación ingrese sus DATOS para confirmar la compra del producto\nDigite su NOMBRE y APELLIDO",
        )
        if nombre:  # Verificar si se ingresó un nombre
            messagebox.showinfo("Datos ingresados", f"DATOS ingresados:\n {nombre}")
            messagebox.showinfo(
                "Muchas Gracias",
                f"MUCHAS GRACIAS {nombre}\nLe invitamos a continuar el proceso de PAGO",
            )
            compra_actual.set_nombre_cliente(nombre)
            break  # Salir del bucle si se ingresó un nombre válido
        else:
            messagebox.showerror("Error", "Debe ingresar su nombre y apellido")

    return precio


def validar_tarjeta_debito():
    messagebox.showinfo(
        "Información", "Recuerde que solo puede pagar con tarjeta de débito"
    )
    precio_final = compra_actual.get_costo_total()
    messagebox.showinfo("Total a pagar", f"El monto total a pagar es: ${precio_final}")

    while True:
        numero_tarjeta = simpledialog.askstring(
            "Número de tarjeta",
            "Ingrese el número de su tarjeta de débito (deben ser 16 dígitos): ",
        )
        if numero_tarjeta is None:  # Si se presiona "Cancelar"
            mostrar_mensaje_despedida()
            return

        if len(numero_tarjeta) == 16:
            messagebox.showinfo(
                "Número de tarjeta", "El número de la tarjeta es válido"
            )
            break
        else:
            messagebox.showerror(
                "Error",
                "El número de la tarjeta debe contener exactamente 16 dígitos. Intente nuevamente",
            )

    while True:
        codigo_seguridad = simpledialog.askstring(
            "Código de seguridad",
            "Ingrese el código de seguridad de su tarjeta (son los 3 dígitos que se encuentran en la parte posterior de su tarjeta): ",
        )
        if codigo_seguridad is None:  # Si se presiona "Cancelar"
            mostrar_mensaje_despedida()
            return

        if len(codigo_seguridad) == 3:
            messagebox.showinfo("Código de seguridad", "El código ingresado es válido")
            break
        else:
            messagebox.showerror(
                "Error", "El código de seguridad es incorrecto, ingréselo nuevamente"
            )

    while True:
        try:
            mes = int(
                simpledialog.askstring(
                    "Mes de vencimiento",
                    "Ingrese el mes de vencimiento de su tarjeta (MM): ",
                )
            )
            anio = int(
                simpledialog.askstring(
                    "Año de vencimiento",
                    "Ingrese el año de vencimiento de su tarjeta en formato (AA): ",
                )
            )
        except ValueError:
            messagebox.showerror(
                "Error", "El mes y año de vencimiento deben ser números enteros"
            )
            continue

        if mes is None or anio is None:  # Si se presiona "Cancelar"
            mostrar_mensaje_despedida()
            return

        if 1 <= mes <= 12 and 24 <= anio <= 99:
            messagebox.showinfo(
                "Fecha de vencimiento", "La fecha de vencimiento es válida"
            )
            break
        else:
            messagebox.showerror(
                "Error", "La fecha de vencimiento NO es válida, intente nuevamente"
            )

    compra_actual.set_pago_realizado(True)

    messagebox.showinfo(
        "TIENDA HOLA MUNDO ANIMAL",
        "Finalizado, pago realizado exitosamente ¡Gracias por su compra!",
    )


def mostrar_mensaje_despedida():
    messagebox.showinfo(
        "TIENDA HOLA MUNDO ANIMAL",
        "¡Gracias por utilizar este sistema de pago! ¡Hasta luego!",
    )


######################################################
#       Inicio del programa                          #
######################################################


def main():
    label_title = tk.Label(
        ventana_principal,
        text="BIENVENIDOS AL SISTEMA DE PAGO DE LA PAGINA\n HOLA MUNDO ANIMAL\n 🐶",
        font=("Candara", 15, "bold"),
    )
    label_title.pack(pady=10)

    label_text = tk.Label(
        ventana_principal,
        text="Para continuar con el proceso de pago haz clic en Aceptar.",
    )
    label_text.pack(pady=10)

    button = tk.Button(
        ventana_principal,
        text="ACEPTAR",
        command=ventana_principal.destroy,
        font=("Candara", 12, "bold"),
        bg="#87BEF6",
        fg="white",
        width=45,
        height=3,
    )
    button.pack(pady=20)

    ventana_principal.mainloop()

    matriz = [[5515, 5521, 5501], [5500, 5539, 5507], [5600, 5613, 5620]]
    try:
        costo_de_envio = elegir_codigo_postal(matriz)
        if costo_de_envio is None:
            return None  # Salimos de la función main si se presionó "Cancelar"
    except ValueError as e:
        messagebox.showerror("Error", "Error al procesar el código postal: " + str(e))
        return

    matriz_productos = query.obtener_productos()

    try:
        precio_del_producto = agregar_producto(matriz_productos)
        if precio_del_producto is None:
            return None  # Salimos de la función main si se presionó "Cancelar"
    except ValueError as e:
        messagebox.showerror("Error", "Error al procesar el producto: " + str(e))
        return

    try:
        compra_actual.set_costo_total(costo_de_envio + precio_del_producto)
        validar_tarjeta_debito()
    except ValueError as e:
        messagebox.showerror(
            "Error", "Error al procesar la tarjeta de débito: " + str(e)
        )


def init_db():
    # Si hay productos dentro de la base de datos no se ejecuta la función
    if len(query.obtener_productos()) > 0:
        print("Usando base de datos anterior...")
        return None

    print("Base de datos: Creada!")

    productos = [
        Producto("Kit descanso perro chico", 3000, 10, 0),
        Producto("Kit descanso perro grande", 4000, 10, 0),
        Producto("Kit baño perro chico", 4000, 13, 0),
        Producto("Kit baño perro grande", 4500, 20, 0),
        Producto("Kit pasea perro chico", 5000, 5, 0),
        Producto("Kit paseo perro grande", 5500, 4, 0),
    ]

    for producto in productos:
        query.add(producto)


if __name__ == "__main__":

    # Se establece la conexión a la base de datos

    #  -- MySQL --
    #
    # pip install pymysql mysqlclient (Yo tuve que instalar eso para que funcione con mysql)
    #
    # engine = create_engine(
    #     "mysql+pymysql://<usuario_mysql>:<contraseña_de_usuario>@<host>/<nombre_de_la_db>",
    #     connect_args=dict(port=3306, host="localhost"),
    # )
    #
    # -- SQLite
    engine = create_engine("sqlite:///database.db")
    # Se crean las tablas necesarias
    Base.metadata.create_all(engine)
    # Se obtiene una función para obtener la sesión actual
    SessionMaker = sessionmaker(bind=engine)
    # Variable global de la sesión
    session = SessionMaker()
    # Variable global para hacer consultas
    query = TypedQuery(session)
    # Se crea la ventana principal del programa
    ventana_principal = tk.Tk()  # Ventana principal
    ventana_principal.title("TIENDA HOLA MUNDO ANIMAL")
    ventana_principal.geometry(
        "600x210"
    )  # Para establecer tamaño de la ventana principal

    # Para centrar la ventana en la pantalla
    screen_width = ventana_principal.winfo_screenwidth()
    screen_height = ventana_principal.winfo_screenheight()
    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (210 / 2)
    ventana_principal.geometry(f"+{int(x)}+{int(y)}")

    # Se inicia el programa y se guarda la compra
    compra_actual = CompraActual()

    init_db()

    main()

    try:
        query.registrar_compra(
            nombre_cliente=compra_actual.get_nombre_cliente(),
            direccion_cliente=compra_actual.get_direccion_cliente(),
            localidad=compra_actual.get_localidad(),
            costo_total=compra_actual.get_costo_total(),
            pago_realizado=compra_actual.get_pago_realizado(),
            producto_id=compra_actual.get_producto_id(),
        )
    except:
        pass
    finally:
        # Se cierra la sesión a la base de datos al terminar
        session.close()
