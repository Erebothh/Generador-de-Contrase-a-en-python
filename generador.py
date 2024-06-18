import random
import string

def generador_passwd(longitud=20, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    passwd = ''.join(random.choice(caracteres) for _ in range(longitud))

    return passwd


def main():
    print("Buenas, Generemos una Contraseña")

    try:
        longitud = int(input("Ingrese la longitud de la contraseña (hasta el 20, número entero) "))
    except ValueError:
        print("Por favor, un número entero")
        return

    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    passwd = generador_passwd(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)

    print(f"Tu contraseña has sido generada: {passwd}")

if __name__==  "__main__":
    main()