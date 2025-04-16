def comparar_palabras(nombre_archivo):
    # Cargar palabras correctas
    palabras_archivo = open("palabras.txt", 'r', encoding='utf-8') # encoding='utf-8 soporta todos los caracteres especiales del español
    palabras_correctas = {palabra.strip().lower(): 0 for palabra in palabras_archivo}
    palabras_archivo.close()

    # Abrir archivo a revisar
    archivo_usuario = open(nombre_archivo, 'r', encoding='utf-8')
    texto = archivo_usuario.read().lower()
    archivo_usuario.close()

    errores = 0
    palabra_actual = ""

    for caracter in texto:
        if caracter.isalpha() or caracter == "'":
            palabra_actual += caracter
        else:
            if palabra_actual:
                #Verificar si la palabra esta en el diccionario
                if palabra_actual not in palabras_correctas:
                    errores += 1
                    print("Palabra incorrecta: ", palabra_actual)
                palabra_actual = ""

    return errores
