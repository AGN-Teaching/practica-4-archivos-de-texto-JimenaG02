import Correccion_textos as ct

archivo = input("¿Cual archivo quieres leer?: ")

texto = open(archivo)

correcion = ct.comparar_palabras(texto)

print("Se encontraron ", correcion, "errores de ortografia en el archivo")