texto = input("Dime un texto con espacios al principio y al final: ")

textoNoEspacios = texto.strip()
textoMinusculas = texto.lower()
textoMayusculas = texto.upper()
textoContar = len(textoMayusculas)

print(textoNoEspacios)
print(textoMinusculas)
print(textoMayusculas)
print(textoContar)