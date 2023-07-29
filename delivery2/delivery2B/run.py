"""
B. Resuelve el sigiuente ejercicio táctico:
    i. Construye una expresión regular para identificar en la URL de los PEP de python:
       - el esquema
       - el subdominio
       - el dominio
       - el TLD
       - el número identificativo del PEP.
    ii. Usa herramientas de validación para afinar el resultado si hace falta.
"""

import re
import webbrowser

def main():
    # Expresión regular con grupos nombrados
    pattern = r"^(?P<esquema>https?://)?(?P<subdominio>[a-zA-Z0-9-]+)\.(?P<dominio>[a-zA-Z0-9-]+)\.(?P<tld>[a-zA-Z]{2,3})/(?P<numero_pep>pep-\d+)/?$"
    """
    Patrones usados:
        esquema: http o https. El ? matchea el ultimo caracter 0 o 1 veces
        subdominio dominio y ltd cualquier combinacion de los caracteres [a-zA-Z0-9-] un numero indeterminado de veces
        dominio combinacion de letras que ocurre entre 2 y tres veces
        numero pep una combinacion de digitos precedida de pep-
        
    """
    #Le prompteo al usuario para una URL
    url = input("Introducir para verificar: ")

    # Validar la URL con la expresión regular de modo que se cumplan todos los patrones
    match = re.fullmatch(pattern, url)

    if match:
        # Acceder a los grupos nombrados
        esquema = match.group("esquema")
        subdominio = match.group("subdominio")
        dominio = match.group("dominio")
        tld = match.group("tld")
        numero_pep = match.group("numero_pep")

        # Imprimir los resultados
        print("Esquema:", esquema)
        print("Subdominio:", subdominio)
        print("Dominio:", dominio)
        print("TLD:", tld)
        print("Número PEP:", numero_pep)

        # Abrimos la URL en el explorador predeterminado
        web_url = f"{esquema}{subdominio}.{dominio}.{tld}/{numero_pep}"
        webbrowser.open(web_url)
    else:
        print("No es el formato esperado.")

if __name__ == "__main__":
    main()

    


