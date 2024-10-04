
def contar_vocales(frase):
    vocales = "aáeéiíoóuúAÁEÉIÍOÓUÚ"
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    return contador

frase = input("Ingrese una frase: ")
print(f"El número de vocales en la frase es de: {contar_vocales(frase)}")
