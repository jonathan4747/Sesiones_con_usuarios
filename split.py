# Crea una función llamada split. Esta función recibe como parámetro un string.
# La función se encarga de dividir el string recibido en un arreglo de strings y los separa
# acorde a sus espacios. El arreglo es retornado.

def split( texto ):
    resultado = []
    palabra = ""
    for caracter in texto:
        if caracter == " ":
            resultado.append( palabra )
            palabra = ""
        else:
            palabra += caracter
    resultado.append( palabra )
    return resultado

text = "Crea una función llamada split. Esta función recibe como parámetro un string."
print( split( text ) )
