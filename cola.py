from utilidades import contar_elementos

class Cola:
    def __init__(self):
        self.lista = []

    def agregar(self, elemento):
        nuevo_tamano = contar_elementos(self.lista) + 1
        nueva_lista = [None] * nuevo_tamano
        i = 0
        for elem in self.lista:
            nueva_lista[i] = elem
            i += 1
        nueva_lista[i] = elemento
        self.lista = []
        for x in nueva_lista:
            self.lista += [x]

    def eliminar(self):
        if contar_elementos(self.lista) == 0:
            return None
        primero = self.lista[0]
        nueva_lista = []
        i = 1
        while i < contar_elementos(self.lista):
            nueva_lista += [self.lista[i]]
            i += 1
        self.lista = []
        for x in nueva_lista:
            self.lista += [x]
        return primero

    def mostrar(self):
        return self.lista

    def esta_vacia(self):
        return contar_elementos(self.lista) == 0

    def cantidad(self):
        return contar_elementos(self.lista)
