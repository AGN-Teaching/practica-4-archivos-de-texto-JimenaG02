
import Correccion_textos as ct

archivo = input("¿Qué archivo quieres revisar?: ")
resultado = ct.comparar_palabras(archivo)

if resultado is not None:
    print("\nTotal de palabras incorrectas encontradas: ", resultado)
