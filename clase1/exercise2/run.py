"""
a.	Escoge 1 libro de tu estantería. Copia en una 
    lista de palabras las primeras 20 palabras. 
b.	Escribe una función generadora que devuelva 
    un iterador que aguarde cada palabra de la 
    lista modificándola de tal forma que acabe 
    siempre con la terminación “spam”.
c.	Escribe una función recursiva que utilice como 
    input el resultado de la función generadora 
    convertido en lista y que devuelva una única 
    palabra nueva juntando  todas las palabras y 
    modificando las que tengan 8 o 9 caracteres
    con el prefijo “ham”.
"""

#palabras = "Finalizando su viaje al Moratorio de los Amados hermanos Glenn Runciter aterrizó con una imponente limusina eléctrica de alquiler en el techo del edificio central de Runciter Asociados en Nueva York"

def spamificar_palabras(palabras):
    """
    Función generadora que agrega la terminación "spam" a cada palabra de una lista de palabras.

    Args:
        palabras (str): Cadena de palabras separadas por espacios.

    Yields:
        str: Palabra con la terminación "spam".
    """
    for palabra in palabras.split(" "):
        yield f"{palabra} spam"


def hamificar_palabras(spam_lista):
    """
    Función recursiva que une las palabras de una lista, modificando las palabras de 8 o 9 caracteres con el prefijo "ham".

    Args:
        spam_lista (list): Lista de palabras spamificadas.

    Returns:
        str: Palabra resultante después de aplicar las modificaciones.
    """
    if len(spam_lista) == 0:
        return ""
    else:
        palabra = spam_lista[0].split(" ")[0]  # Retomar la palabra sin spam
        palabra = f"ham {palabra}" if 7 < len(palabra) < 10 else palabra
        return f"{palabra} {hamificar_palabras(spam_lista[1:])}"


if __name__ == "__main__":
    palabras = input("Por favor, introduzca su lista de palabras: \n")
    palabras_spamificadas = list(spamificar_palabras(palabras))
    resultado = hamificar_palabras(palabras_spamificadas)
    print(resultado)
    