import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    print(
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        + "\n%     BIENVENIDOS AL SISTEMA DE PAGO DE LA PAGINA     %"
        + "\n%                HOLA MUNDO ANIMAL                    %"
        + "\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    )

    matriz = [
        [5515, 5521, 5501],
        [5500, 5539, 5507],
        [5600, 5613, 5620]
    ]
    costo_de_envio = elegir_codigo_postal(matriz)

    matriz_productos = [
        "1. Kit descanso perro chico $3000",
        "2. Kit descanso perro grande $3500",
        "3. Kit baño perro chico $4000",
        "4. Kit baño perro grande $4500",
        "5. Kit paseo perro chico $5000",
        "6. Kit paseo perro grande $5500"
    ]
    precio_del_producto = agregar_producto(matriz_productos)

    validar_tarjeta_debito(costo_de_envio, precio_del_producto)

def elegir_codigo_postal(matriz):
    root = tk.Tk()
    root.withdraw()
    costo_de_envio = 0
    postal = False

    matriz_texto = "\n".join(" ".join(map(str, fila)) for fila in matriz)
    messagebox.showinfo("Información", "A continuación vera las opciones de entrega a domicilio que tenemos para ofrecer dentro de Mendoza")

    while not postal:
        codigo_str = simpledialog.askstring("Código Postal", "Digite el código postal al que quiere recibir su pedido:\n" + matriz_texto)
        if codigo_str is None:
            mostrar_mensaje_despedida()
            return

        codigo = int(codigo_str)
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
            print(f"El costo de envío es de ${nuevo_costo}")
            costo_de_envio = nuevo_costo
            postal = True
        else:
            print("El código postal que indicó no está dentro de nuestras zonas de envíos a Domicilio")
            respuesta = input("¿Desea volver a intentar? (S/N): ")
            if respuesta.lower() != 'n':
                print("Lo invitamos a visitar la sucursal de forma presencial y ser atendido por nuestro personal.")
                break

    if postal:
        direc = input("Perfecto, digite su calle, dirección y el envío llega en las primeras 24 horas desde que usted realiza el pago\nDigite su dirección: ")
        print(f"Usted ingresó la siguiente dirección: {direc}")
        direc = input("Sí ingresó mal la dirección, vuelva a ingresarla, de lo contrario presione ENTER: ")

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
            return

        producto = int(producto_str)
        precio_producto = {
            1: 3000,
            2: 3500,
            3: 4000,
            4: 4500,
            5: 5000,
            6: 5500
        }.get(producto, -1)

        if precio_producto >= 0:
            print(f"El PRECIO del producto es de ${precio_producto}")
            precio = precio_producto
            codigop = True
        else:
            print("Producto no registrado, ingrese otro CÓDIGO")
            respuesta = input("Digite (S/N) para continuar con la compra del producto: ")
            if respuesta.lower() != 's':
                print("Comuníquese con Atención al cliente o reingrese nuevamente el CÓDIGO del producto")
                break

    if codigop:
        nombre = input("A continuación ingrese sus DATOS para confirmar la compra del producto\nDigite su NOMBRE y APELLIDO: ")
        messagebox.showinfo("Datos ingresados", f"DATOS ingresados:\n {nombre}")
        messagebox.showinfo("Muchas Gracias", f"MUCHAS GRACIAS {nombre}\nLe invitamos a continuar el proceso de PAGO")

    return precio

def validar_tarjeta_debito(costo_de_envio, precio_producto):
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Información", "Recuerde que solo puede pagar con tarjeta de débito")
    precio_final = costo_de_envio + precio_producto
    messagebox.showinfo("Total a pagar", f"El monto total a pagar es: ${precio_final}")
    print(f"Total compra: ${precio_final}")

    while True:
        numero_tarjeta = input("Ingrese el número de su tarjeta de débito (deben ser 16 dígitos): ")
        if len(numero_tarjeta) == 16:
            print("El número de la tarjeta es válido")
            break
        else:
            print("El número de la tarjeta debe contener exactamente 16 dígitos. Intente nuevamente")

    while True:
        codigo_seguridad = input("Ingrese el código de seguridad de su tarjeta (son los 3 dígitos que se encuentran en la parte posterior de su tarjeta): ")
        if len(codigo_seguridad) == 3:
            print("El código ingresado es válido")
            break
        else:
            print("El código de seguridad es incorrecto, ingréselo nuevamente")

    while True:
        mes = int(input("Ingrese el mes de vencimiento de su tarjeta (MM): "))
        anio = int(input("Ingrese el año de vencimiento de su tarjeta en formato (AA): "))
        if 1 <= mes <= 12 and 24 <= anio <= 99:
            print("La fecha de vencimiento es válida")
            break
        else:
            print("La fecha de vencimiento NO es válida, intente nuevamente")

    print("Finalizado, pago realizado exitosamente ¡Gracias por su compra!")

def mostrar_mensaje_despedida():
    messagebox.showinfo("Despedida", "¡Gracias por utilizar el sistema! ¡Hasta luego!")

if __name__ == "__main__":
    main()