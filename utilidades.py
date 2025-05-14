# ------------------------------
# utilidades.py - Funciones auxiliares
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
