import tkinter as tk
from tkinter import simpledialog, messagebox

import os

def main():
    root = tk.Tk()
    root.title("TIENDA HOLA MUNDO ANIMAL")
    root.geometry("600x210") # Para establecer tamaño de la ventana principal

    # Para centrar la ventana en la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (600 / 2)
    y = (screen_height / 2) - (210 / 2)
    root.geometry(f'+{int(x)}+{int(y)}')

    label_title = tk.Label(root, text="BIENVENIDOS AL SISTEMA DE PAGO DE LA PAGINA\n HOLA MUNDO ANIMAL\n 🐶", font=("Candara", 15, "bold"))
    label_title.pack(pady=10)

    label_text = tk.Label(root, text="Para continuar con el proceso de pago haz clic en Aceptar.")
    label_text.pack(pady=10)

    button = tk.Button(root, text="ACEPTAR", command=root.destroy, font=("Candara", 12, "bold"),bg="#87BEF6", fg="white", width=45, height=3)
    button.pack(pady=20)

    root.mainloop()

    matriz = [
        [5515, 5521, 5501],
        [5500, 5539, 5507],
        [5600, 5613, 5620]
    ]
    try:
        costo_de_envio = elegir_codigo_postal(matriz)
        if costo_de_envio is None:
            return None # Salimos de la función main si se presionó "Cancelar"
    except ValueError as e:
        messagebox.showerror("Error", "Error al procesar el código postal: " + str(e))
        return

    matriz_productos = [
        "1. Kit descanso perro chico $3000",
        "2. Kit descanso perro grande $3500",
        "3. Kit baño perro chico $4000",
        "4. Kit baño perro grande $4500",
        "5. Kit paseo perro chico $5000",
        "6. Kit paseo perro grande $5500"
    ]
    try:
        precio_del_producto = agregar_producto(matriz_productos)
        if precio_del_producto is None:
            return None  # Salimos de la función main si se presionó "Cancelar"
    except ValueError as e:
        messagebox.showerror("Error", "Error al procesar el producto: " + str(e))
        return

    try:
        validar_tarjeta_debito(costo_de_envio, precio_del_producto)
    except ValueError as e:
        messagebox.showerror("Error", "Error al procesar la tarjeta de débito: " + str(e))

def elegir_codigo_postal(matriz):
    root = tk.Tk()
    root.withdraw()
    costo_de_envio = 0
    postal = False

    matriz_texto = "\n".join(" ".join(map(str, fila)) for fila in matriz)
    messagebox.showinfo("Información", "A continuación verá las opciones de entrega a domicilio que tenemos para ofrecer dentro de Mendoza")

    while not postal:
        codigo_str = simpledialog.askstring("Código Postal", "Digite el código postal al que quiere recibir su pedido:\n" + matriz_texto)
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
            5620: 0
        }.get(codigo, -1)

        if nuevo_costo >= 0:
            messagebox.showinfo("Costo de envío", f"El costo de envío es de ${nuevo_costo}")
            costo_de_envio = nuevo_costo
            postal = True
        else:
            messagebox.showerror("Error", "El código postal que indicó no está dentro de nuestras zonas de envíos a Domicilio")
            respuesta = messagebox.askyesno("¿Desea volver a intentar?", "¿Desea volver a intentar?")
            if not respuesta:
                messagebox.showinfo("Información", "Lo invitamos a visitar la sucursal de forma presencial y ser atendido por nuestro personal.")
                break

    if postal:
        while True:
            direc = simpledialog.askstring("Dirección","Digite su calle, dirección y el envío llega en las primeras 24 horas desde que usted realiza el pago")
            if direc is None:  # Si se presiona "Cancelar"
                mostrar_mensaje_despedida()
                return
            if direc:  # Verificar si la dirección no está vacía
                messagebox.showinfo("Dirección", f"Usted ingresó la siguiente dirección: {direc}")
                break  # Salir del bucle si la dirección es válida
            else:
                messagebox.showerror("Error", "Debe ingresar una dirección válida. Por favor, inténtelo nuevamente.")

        direc = simpledialog.askstring("Dirección", "Si ha ingresado mal la dirección, vuelva a ingresarla, de lo contrario presione ENTER")

    return costo_de_envio

def agregar_producto(matriz_productos):
    root = tk.Tk()
    root.withdraw()
    precio = 0
    codigop = False

    matriz_p = "\n".join(matriz_productos)

    while not codigop:
        producto_str = simpledialog.askstring("Producto", "Digite el CÓDIGO del producto que desea:\n" + matriz_p)
        if producto_str is None:
            mostrar_mensaje_despedida()
            return None

        try:
            producto = int(producto_str)
        except ValueError:
            messagebox.showerror("Error", "El código del producto debe ser un número entero")
            continue

        precio_producto = {
            1: 3000,
            2: 3500,
            3: 4000,
            4: 4500,
            5: 5000,
            6: 5500
        }.get(producto, -1)

        if precio_producto >= 0:
            messagebox.showinfo("Precio del producto", f"El PRECIO del producto es de ${precio_producto}")
            precio = precio_producto
            codigop = True
        else:
            messagebox.showerror("Error", "Producto no registrado, ingrese otro CÓDIGO")
            respuesta = messagebox.askyesno("¿Desea continuar?", "¿Desea continuar con la compra del producto?")
            if not respuesta:
                messagebox.showinfo("Información", "Comuníquese con Atención al cliente o reingrese nuevamente el CÓDIGO del producto")
                break

    if codigop:
        while True:
            nombre = simpledialog.askstring("Datos", "A continuación ingrese sus DATOS para confirmar la compra del producto\nDigite su NOMBRE y APELLIDO")
            if nombre:  # Verificar si se ingresó un nombre
                messagebox.showinfo("Datos ingresados", f"DATOS ingresados:\n {nombre}")
                messagebox.showinfo("Muchas Gracias", f"MUCHAS GRACIAS {nombre}\nLe invitamos a continuar el proceso de PAGO")
                break  # Salir del bucle si se ingresó un nombre válido
            else:
                messagebox.showerror("Error", "Debe ingresar su nombre y apellido")
    return precio

def validar_tarjeta_debito(costo_de_envio, precio_producto):
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Información", "Recuerde que solo puede pagar con tarjeta de débito")
    precio_final = costo_de_envio + precio_producto
    messagebox.showinfo("Total a pagar", f"El monto total a pagar es: ${precio_final}")

    while True:
        numero_tarjeta = simpledialog.askstring("Número de tarjeta", "Ingrese el número de su tarjeta de débito (deben ser 16 dígitos): ")
        if numero_tarjeta is None:  # Si se presiona "Cancelar"
            mostrar_mensaje_despedida()
            return

        if len(numero_tarjeta) == 16:
            messagebox.showinfo("Número de tarjeta", "El número de la tarjeta es válido")
            break
        else:
            messagebox.showerror("Error", "El número de la tarjeta debe contener exactamente 16 dígitos. Intente nuevamente")

    while True:
        codigo_seguridad = simpledialog.askstring("Código de seguridad", "Ingrese el código de seguridad de su tarjeta (son los 3 dígitos que se encuentran en la parte posterior de su tarjeta): ")
        if codigo_seguridad is None:  # Si se presiona "Cancelar"
            mostrar_mensaje_despedida()
            return

        if len(codigo_seguridad) == 3:
            messagebox.showinfo("Código de seguridad", "El código ingresado es válido")
            break
        else:
            messagebox.showerror("Error", "El código de seguridad es incorrecto, ingréselo nuevamente")

    while True:
        try:
            mes = int(simpledialog.askstring("Mes de vencimiento", "Ingrese el mes de vencimiento de su tarjeta (MM): "))
            anio = int(simpledialog.askstring("Año de vencimiento", "Ingrese el año de vencimiento de su tarjeta en formato (AA): "))
        except ValueError:
            messagebox.showerror("Error", "El mes y año de vencimiento deben ser números enteros")
            continue

        if mes is None or anio is None:  # Si se presiona "Cancelar"
            mostrar_mensaje_despedida()
            return

        if 1 <= mes <= 12 and 24 <= anio <= 99:
            messagebox.showinfo("Fecha de vencimiento", "La fecha de vencimiento es válida")
            break
        else:
            messagebox.showerror("Error", "La fecha de vencimiento NO es válida, intente nuevamente")

    messagebox.showinfo("TIENDA HOLA MUNDO ANIMAL", "Finalizado, pago realizado exitosamente ¡Gracias por su compra!")

def mostrar_mensaje_despedida():
    messagebox.showinfo("TIENDA HOLA MUNDO ANIMAL", "¡Gracias por utilizar este sistema de pago! ¡Hasta luego!")

if __name__ == "__main__":
    main()

# CODIGO BY PRUEBAS ADRY:
# He reemplazado los input y print por
# simpledialog.askstring y messagebox.showinfo respectivamente,
# para mostrar los mensajes de diálogo.

# He agregado algunos messagebox.showerror para mostrar errores en caso
# de que el usuario ingrese datos incorrectos.

# He agregado control de errores y bucles while para el caso de datos no ingresados correctamente
# o para el caso de cancelar el proceso en curso
