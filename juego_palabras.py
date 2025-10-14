import random

class JuegoAdivinanza:
    def __init__(self):
        self.palabras = ["python", "programacion", "juego", "computadora", "universidad"]
        self.palabra_secreta = ""
        self.letras_adivinadas = []
        self.intentos = 0
        self.max_intentos = 15

    def obtener_palabra_secreta(self):
        return random.choice(self.palabras)

    def mostrar_progreso(self):
        progreso = [letra if letra in self.letras_adivinadas else "_" for letra in self.palabra_secreta]
        print("Progreso:", " ".join(progreso))
        return progreso

    def validar_entrada(self, intento):
        if not intento.isalpha():
            print("Error: Solo se permiten letras")
            return False
        return True

    def procesar_letra(self, letra):
        if letra in self.palabra_secreta:
            if letra not in self.letras_adivinadas:
                self.letras_adivinadas.append(letra)
                print(" Letra correcta:", letra)
                return True
            else:
                print(" Ya intentaste esa letra")
                return False
        else:
            print(" Letra incorrecta")
            return False

    def procesar_palabra_completa(self, palabra):
        if palabra == self.palabra_secreta:
            print(" ¡Adivinaste la palabra!", self.palabra_secreta)
            return True
        else:
            print("Esa no es la palabra")
            return False

    def verificar_victoria(self):
        progreso = self.mostrar_progreso()
        return "_" not in progreso

    def jugar(self):
        self.palabra_secreta = self.obtener_palabra_secreta()
        self.letras_adivinadas = []
        self.intentos = 0

        print(" Bienvenido al juego de adivinar la palabra secreta")
        print(f" La palabra tiene {len(self.palabra_secreta)} letras.")
        print(f" Tienes un máximo de {self.max_intentos} intentos")

        while self.intentos < self.max_intentos:
            intento = input("\nIngresa tu intento: ").lower().strip()
            
            if not self.validar_entrada(intento):
                continue

            self.intentos += 1
            intentos_restantes = self.max_intentos - self.intentos

            if len(intento) == 1:
                self.procesar_letra(intento)
            elif len(intento) == len(self.palabra_secreta):
                if self.procesar_palabra_completa(intento):
                    break
            else:
                print(" Entrada inválida. Ingresa una letra o la palabra completa")

            if self.verificar_victoria():
                print(f"🎊 ¡Ganaste! La palabra era: {self.palabra_secreta}")
                break

            print(f" Intentos restantes: {intentos_restantes}")

        else:
            print(f" Game Over. La palabra era: {self.palabra_secreta}")

        print(f" Intentos totales: {self.intentos}")

if __name__ == "__main__":
    juego = JuegoAdivinanza()
    juego.jugar()