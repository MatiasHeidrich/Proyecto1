# Inicio del juego
from random import randint
import time
print("""------------------------------------""")
print("--- Inciando juego 'El ahorcado' ---")
print("""------------------------------------
      """)
time.sleep(1)

#Seleccion de palabras e intentos
palabras = ["babuino", "sinfonia", "integral", "xilofono", "nariz", "bicicleta"]
indice_palabras_max = len(palabras) - 1
indice_aleatorio = randint(0, indice_palabras_max)
intentos = 6

palabra_aleatoria = palabras[indice_aleatorio] # palabra aleatoria

# Debe mostrar las letras adivinadas y las letras incorrectas.
correctas = []
incorrectas = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
palabra_secreta = ['__'] * len(palabra_aleatoria)

print(palabra_secreta)

# El juego debe verificar si la letra ingresada por el jugador está en la
# palabra secreta y actualizar el estado del juego en consecuencia.

juego_termino = False

while juego_termino == False:
    print(f"Tienes: ", intentos, " intentos")
    if intentos == 0:
        break
    letra_ingresada = str(input("Por favor ingrese una letra: "))

    ind = 0
    existe_letra = False
    for letra in palabra_aleatoria:
        if letra == letra_ingresada:
            existe_letra = True
            palabra_secreta[ind] = letra_ingresada
            print("Muy bien!")
            print("""
                  """)
            print(palabra_secreta)
        ind += 1
    if palabra_secreta == ['b', 'a', 'b', 'u', 'i', 'n', 'o']: 
        juego_termino = True
        print("Felicidades, has ganado! La palabra era *Babuino*")
    elif palabra_secreta == ['s', 'i', 'n', 'f', 'o', 'n', 'i', 'a']: 
        juego_termino = True
        print("Felicidades, has ganado! La palabra era *Sinfonia*")
    elif palabra_secreta == ['i', 'n', 't', 'e', 'g', 'r', 'a', 'l']: 
        juego_termino = True
        print("Felicidades, has ganado! La palabra era *Integral*")
    elif palabra_secreta == ['x', 'i', 'l', 'o', 'f', 'o', 'n', 'o']: 
        juego_termino = True
        print("Felicidades, has ganado! La palabra era *Xilofono*")
    elif palabra_secreta == ['n', 'a', 'r', 'i', 'z']: 
        juego_termino = True
        print("Felicidades, has ganado! La palabra era *Nariz*")
    elif palabra_secreta == ['b', 'i', 'c', 'i', 'c', 'l', 'e', 't', 'a']: 
        juego_termino = True
        print("Felicidades, has ganado! La palabra era *Bicicleta*")        
    elif existe_letra == False:
        print("""Incorrecto, prueba otra letra
              """)
        intentos = intentos - 1
    if intentos <= 0:
        print("""Has perdido x_x
              no te quedan mas intentos""")
        
    if existe_letra:
        correctas.append(letra_ingresada)
    else:
        incorrectas.append(letra_ingresada)
    letras.remove(letra_ingresada)
    print("""
          """)
    print("""------------------------------------""")
    print("Letras correctas: ", correctas)
    print("Letras incorrectas: ", incorrectas)
    print("""------------------------------------
      """)
    time.sleep(1)
#Fin del programa