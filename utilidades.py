def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

def convertir_minusculas(texto):
    resultado = ""
    for c in texto:
        codigo = ord(c)
        if 65 <= codigo <= 90:
            resultado += chr(codigo + 32)
        else:
            resultado += c
    return resultado

def es_nombre_valido(nombre):
    for c in nombre:
        if c != " ":
            return True
    return False
