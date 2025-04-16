

def comparar_palabras(texto):

    palabras_correctas = {open("palabras.txt", 'r')}

    errores = 0
    for caracter in texto:
        caracter += caracter
        if caracter.isspace() or caracter in ".!?,;:":  # Si hay un espacio o contiene esos caracteres los cuenta como palabras
            print(caracter)

            if caracter != palabras_correctas:
                errores += 1
            else:
                caracter = ""
                return

    return errores