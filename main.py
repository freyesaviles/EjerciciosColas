# ------------------------------
# Sistema de atención - Clínica y Farmacia
# ------------------------------

# Colas vacías
cola_clinica = []
cola_farmacia = []

# ------------------------------
# Funciones auxiliares
# ------------------------------

def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def convertir_minusculas(texto):
    resultado = ""
    for c in texto:
        codigo = ord(c)
        if codigo >= 65 and codigo <= 90:
            resultado += chr(codigo + 32)
        else:
            resultado += c
    return resultado

def es_nombre_valido(nombre):
    valido = False
    for c in nombre:
        if c != " ":
            valido = True
    return valido

# ------------------------------
# Funciones para clínica
# ------------------------------

def agregar_paciente_clinica(nombre):
    global cola_clinica
    if not es_nombre_valido(nombre):
        print("El nombre no puede estar vacío.")
    else:
        nuevo_tamano = contar_elementos(cola_clinica) + 1
        nueva_cola = [None] * nuevo_tamano
        i = 0
        for p in cola_clinica:
            nueva_cola[i] = p
            i += 1
        nueva_cola[i] = nombre
        cola_clinica = []
        for x in nueva_cola:
            cola_clinica += [x]
        print("Paciente '" + nombre + "' agregado a la cola de clínica.")

def atender_paciente_clinica():
    global cola_clinica
    if contar_elementos(cola_clinica) == 0:
        print("No hay pacientes en espera (clínica).")
    else:
        paciente = cola_clinica[0]
        nueva_cola = []
        i = 1
        while i < contar_elementos(cola_clinica):
            nueva_cola += [cola_clinica[i]]
            i += 1
        cola_clinica = []
        for x in nueva_cola:
            cola_clinica += [x]
        print("Atendiendo a: " + paciente + " (clínica)")

def mostrar_clinica():
    if contar_elementos(cola_clinica) == 0:
        print("No hay pacientes en la cola (clínica).")
    else:
        print("\nPacientes en espera (clínica):")
        i = 0
        while i < contar_elementos(cola_clinica):
            print(str(i + 1) + ". " + cola_clinica[i])
            i += 1

# ------------------------------
# Funciones para farmacia
# ------------------------------

def agregar_paciente_farmacia(nombre, servicio):
    global cola_farmacia
    servicio_min = convertir_minusculas(servicio)
    if servicio_min != "compra" and servicio_min != "consulta" and servicio_min != "receta":
        print("Tipo de servicio no válido. Use: compra, consulta o receta.")
    else:
        nuevo_tamano = contar_elementos(cola_farmacia) + 1
        nueva_cola = [None] * nuevo_tamano
        i = 0
        for p in cola_farmacia:
            nueva_cola[i] = p
            i += 1
        nueva_cola[i] = {"nombre": nombre, "servicio": servicio_min}
        cola_farmacia = []
        for x in nueva_cola:
            cola_farmacia += [x]
        print("Paciente '" + nombre + "' registrado para '" + servicio_min + "'.")

def atender_paciente_farmacia():
    global cola_farmacia
    if contar_elementos(cola_farmacia) == 0:
        print("No hay pacientes en espera (farmacia).")
    else:
        paciente = cola_farmacia[0]
        nueva_cola = []
        i = 1
        while i < contar_elementos(cola_farmacia):
            nueva_cola += [cola_farmacia[i]]
            i += 1
        cola_farmacia = []
        for x in nueva_cola:
            cola_farmacia += [x]
        print("Atendiendo a: " + paciente["nombre"] + " (Servicio: " + paciente["servicio"] + ")")

def mostrar_farmacia():
    if contar_elementos(cola_farmacia) == 0:
        print("No hay paciente en la cola (farmacia).")
    else:
        print("\nPaciente en espera (farmacia):")
        i = 0
        while i < contar_elementos(cola_farmacia):
            paciente = cola_farmacia[i]
            print(str(i + 1) + ". " + paciente["nombre"] + " - " + paciente["servicio"])
            i += 1

# ------------------------------
# Menú principal
# ------------------------------

def menu():
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
            agregar_paciente_clinica(nombre)
        elif opcion == "2":
            atender_paciente_clinica()
        elif opcion == "3":
            mostrar_clinica()
        elif opcion == "4":
            nombre = input("Ingrese el nombre del paciente (farmacia): ")
            servicio = input("Ingrese el servicio (compra, consulta, receta): ")
            agregar_paciente_farmacia(nombre, servicio)
        elif opcion == "5":
            atender_paciente_farmacia()
        elif opcion == "6":
            mostrar_farmacia()
        elif opcion == "7":
            print("Saliendo del sistema.")
            salir = True
        else:
            print("Opción inválida. Intente nuevamente.")

# ------------------------------
# Ejecutar el programa
# ------------------------------
menu()
