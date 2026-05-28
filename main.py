"""Programa de transformacion de texto."""
import transform

def main():
    """Muestra un menu y aplica una transformacion."""
    texto = input("Introduce un texto:")

    print("Que transformacion quieres?")
    print("[1] Texto en mayusculas")
    print("[2] Texto en minusculas")
    print("[3] Texto capitalizado")

    opcion = input("Opcion elegida: ")

    if opcion == "1":
        print(transform.to_upper_case(texto))
    elif opcion == "2":
        print(transform.to_lower_case(texto))
    elif opcion == "3":
        print(transform.to_capitalize(texto))
    else:
        print("Opcion no reconocida")

if __name__ == '__main__':
    main()
