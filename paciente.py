from cola import Cola
from utilidades import es_nombre_valido, contar_elementos, convertir_minusculas

class Clinica:
    def __init__(self):
        self.cola = Cola()

    def agregar_paciente(self, nombre):
        if not es_nombre_valido(nombre):
            print("El nombre no puede estar vacío.")
        else:
            self.cola.agregar(nombre)
            print(f"Paciente '{nombre}' agregado a la cola de clínica.")

    def atender_paciente(self):
        if self.cola.esta_vacia():
            print("No hay pacientes en espera (clínica).")
        else:
            paciente = self.cola.eliminar()
            print(f"Atendiendo a: {paciente} (clínica)")

    def mostrar_cola(self):
        if self.cola.esta_vacia():
            print("No hay pacientes en la cola (clínica).")
        else:
            print("\nPacientes en espera (clínica):")
            lista = self.cola.mostrar()
            i = 0
            while i < contar_elementos(lista):
                print(f"{i + 1}. {lista[i]}")
                i += 1

class Farmacia:
    def __init__(self):
        self.cola = Cola()

    def agregar_paciente(self, nombre, servicio):
        servicio_min = convertir_minusculas(servicio)
        if servicio_min not in ["compra", "consulta", "receta"]:
            print("Tipo de servicio no válido. Use: compra, consulta o receta.")
        else:
            self.cola.agregar({"nombre": nombre, "servicio": servicio_min})
            print(f"Paciente '{nombre}' registrado para '{servicio_min}'.")

    def atender_paciente(self):
        if self.cola.esta_vacia():
            print("No hay pacientes en espera (farmacia).")
        else:
            paciente = self.cola.eliminar()
            print(f"Atendiendo a: {paciente['nombre']} (Servicio: {paciente['servicio']})")

    def mostrar_cola(self):
        if self.cola.esta_vacia():
            print("No hay pacientes en la cola (farmacia).")
        else:
            print("\nPacientes en espera (farmacia):")
            lista = self.cola.mostrar()
            i = 0
            while i < contar_elementos(lista):
                paciente = lista[i]
                print(f"{i + 1}. {paciente['nombre']} - {paciente['servicio']}")
                i += 1
