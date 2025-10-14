import random

def obtener_palabra_secreta():
    palabras = ["python", "programacion", "juego", "computadora", "universidad"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    print("Progreso:", " ".join(progreso))
    return progreso

def procesar_intento(intento, palabra, letras_adivinadas):
    if len(intento) == 1:
        if intento in palabra:
            if intento not in letras_adivinadas:
                letras_adivinadas.append(intento)
                print("Letra correcta:", intento)
            else:
                print("Ya intentaste esa letra")
        else:
            print("Letra incorrecta")
        return False
    elif len(intento) == len(palabra):
        if intento == palabra:
            print("¡Adivinaste la palabra!", palabra)
            return True
        else:
            print("Esa no es la palabra")
            return False
    else:
        print("Entrada inválida. Intenta de nuevo")
        return False

def jugar_adivinanza_palabra():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 0

    print("Bienvenido al juego de adivinar la palabra secreta")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")

    while True:
        intento = input("Ingresa tu intento: ").lower()
        intentos += 1

        if procesar_intento(intento, palabra_secreta, letras_adivinadas):
            break

        progreso = mostrar_progreso(palabra_secreta, letras_adivinadas)

        if "_" not in progreso:
            print("¡Ganaste! La palabra era:", palabra_secreta)
            break

    print("Intentos totales:", intentos)

if __name__ == "__main__":
    jugar_adivinanza_palabra()