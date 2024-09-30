import sys

def crear_diccionario():
    return {
        "nombre": "Luis Enrique Astudillo Ramirez",
        "edad": 21,
        "ciudad": "Machala",
        "profesion": "Ingeniera en Tecnologias de la Informacion y Comunicacion"
    }

def mostrar_menu():
    print("\n--- Menú de Gestión de Información Personal ---")
    print("1. Mostrar información")
    print("2. Modificar un valor")
    print("3. Agregar nueva clave-valor")
    print("4. Verificar y agregar teléfono")
    print("5. Eliminar una clave")
    print("6. Salir")

def mostrar_informacion(info):
    print("\nInformación Personal:")
    for clave, valor in info.items():
        print(f"{clave.capitalize()}: {valor}")

def modificar_valor(info):
    clave = input("Ingrese la clave a modificar: ").lower()
    if clave in info:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}': ")
        info[clave] = nuevo_valor
        print(f"'{clave}' ha sido actualizado.")
    else:
        print("La clave no existe en el diccionario.")

def agregar_clave_valor(info):
    nueva_clave = input("Ingrese la nueva clave: ").lower()
    if nueva_clave not in info:
        nuevo_valor = input(f"Ingrese el valor para '{nueva_clave}': ")
        info[nueva_clave] = nuevo_valor
        print(f"'{nueva_clave}' ha sido agregado al diccionario.")
    else:
        print("La clave ya existe. Use la opción de modificar si desea cambiar su valor.")

def verificar_agregar_telefono(info):
    if "telefono" not in info:
        telefono = input("No existe un teléfono. Ingrese un número de teléfono: ")
        info["telefono"] = telefono
        print("Teléfono agregado exitosamente.")
    else:
        print(f"Ya existe un teléfono: {info['telefono']}")

def eliminar_clave(info):
    clave = input("Ingrese la clave a eliminar: ").lower()
    if clave in info:
        confirmacion = input(f"¿Está seguro de eliminar '{clave}'? (s/n): ").lower()
        if confirmacion == 's':
            del info[clave]
            print(f"'{clave}' ha sido eliminado del diccionario.")
        else:
            print("Operación cancelada.")
    else:
        print("La clave no existe en el diccionario.")

def main():
    informacion_personal = crear_diccionario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            mostrar_informacion(informacion_personal)
        elif opcion == '2':
            modificar_valor(informacion_personal)
        elif opcion == '3':
            agregar_clave_valor(informacion_personal)
        elif opcion == '4':
            verificar_agregar_telefono(informacion_personal)
        elif opcion == '5':
            eliminar_clave(informacion_personal)
        elif opcion == '6':
            print("Gracias por usar el programa. ¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()