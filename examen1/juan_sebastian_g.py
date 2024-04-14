# resultadopunto1 = ((-10)*((-2)**1500)) + ((14) * ((-1)**1500))
# print(resultadopunto1)

# PUNTO 2

def buscar_mayusculas(string, resultao=[], i=0):
    if type(string) is not str:
        return "ingrese un "

    if i == len(string):
        return resultao
    
    if string[i].isupper():
        resultao.append((string[i], i))

    return buscar_mayusculas(string, resultao, i+1)

print("Ejemplo con la cadena PaChoooOooOASJASFa: ", buscar_mayusculas("PaChoooOooOASJASFa"))
