frase = input("Ingrese una frase o palabra: ")
if frase and frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)