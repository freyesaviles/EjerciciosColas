from paciente import Clinica, Farmacia

def menu():
    clinica = Clinica()
    farmacia = Farmacia()
    salir = False

    while not salir:
        print("\n--- Sistema de Turnos ---")
        print("1. Clínica - Agregar paciente")
        print("2. Clínica - Atender paciente")
        print("3. Clínica - Mostrar cola")
        print("4. Farmacia - Agregar paciente")
        print("5. Farmacia - Atender paciente")
        print("6. Farmacia - Mostrar cola")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente (clínica): ")
            clinica.agregar_paciente(nombre)
        elif opcion == "2":
            clinica.atender_paciente()
        elif opcion == "3":
            clinica.mostrar_cola()
        elif opcion == "4":
            nombre = input("Ingrese el nombre del paciente (farmacia): ")
            servicio = input("Ingrese el servicio (compra, consulta, receta): ")
            farmacia.agregar_paciente(nombre, servicio)
        elif opcion == "5":
            farmacia.atender_paciente()
        elif opcion == "6":
            farmacia.mostrar_cola()
        elif opcion == "7":
            print("Saliendo del sistema.")
            salir = True
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar
menu()
