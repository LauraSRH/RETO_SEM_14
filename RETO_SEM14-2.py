#RETO DE LA SEMANA 14, AGENDA DE CONTACTOS
#Programa en el que se abra un archivo generado y se
# pueda modificar los datos de algún contacto.
# ● El programa mostrará en la pantalla la información de los contactos
# guardados numerada.
# ● Preguntará de cuál de los contactos se desea modificar la información.
# ● Se podrá modificar el nombre, el teléfono y el correo.
# ● Se debe actualizar la información en el archivo.
# ● El programa no debe interrumpirse al ingresar mal los datos o las opciones.

import os

personas = []

# Definir la ruta del archivo en la misma carpeta del script
ruta = os.path.join(os.path.dirname(__file__), "contactos.txt")

# Si ya existe el archivo, cargar contactos
if os.path.exists(ruta):
    with open(ruta) as f:
        for linea in f:
            nombre, tel, correo = linea.strip().split(",")
            personas.append({"nombre": nombre, "telefono": tel, "correo": correo})

while True:
    print("1. Agregar contacto")
    print("2. Modificar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        personas.append({"nombre": nombre, "telefono": telefono, "correo": correo})
        with open(ruta, "w") as archivo:
            for persona in personas:
                archivo.write(f"{persona['nombre']},{persona['telefono']},{persona['correo']}\n")
        print("Contacto agregado exitosamente.")
        print("Archivo guardado en:", os.path.abspath(ruta))

    elif opcion == "2":
        if not personas:
            print("No hay contactos para modificar.")
            continue
        for i, persona in enumerate(personas):
            print(f"{i + 1}. {persona['nombre']} - {persona['telefono']} - {persona['correo']}")
        try:
            indice = int(input("Seleccione el número del contacto a modificar: ")) - 1
            if 0 <= indice < len(personas):
                nombre = input("Ingrese el nuevo nombre del contacto (deje en blanco para no cambiar): ")
                telefono = input("Ingrese el nuevo teléfono del contacto (deje en blanco para no cambiar): ")
                correo = input("Ingrese el nuevo correo del contacto (deje en blanco para no cambiar): ")
                if nombre:
                    personas[indice]['nombre'] = nombre
                if telefono:
                    personas[indice]['telefono'] = telefono
                if correo:
                    personas[indice]['correo'] = correo
                with open(ruta, "w") as archivo:
                    for persona in personas:
                        archivo.write(f"{persona['nombre']},{persona['telefono']},{persona['correo']}\n")
                print("Contacto modificado exitosamente.")
                print("Archivo guardado en:", os.path.abspath(ruta))
            else:
                print("Número de contacto inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    elif opcion == "3":
        if not personas:
            print("No hay contactos para mostrar.")
        else:
            for i, persona in enumerate(personas):
                print(f"{i + 1}. {persona['nombre']} - {persona['telefono']} - {persona['correo']}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break