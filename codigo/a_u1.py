import random

def elegir_palabra():
    palabras = ['python', 'programacion', 'ahorcado', 'desarrollo', 'openai', 'inteligencia']
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    resultado = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += '_'
        resultado += ' '
    return resultado

def dibujar_ahorcado(intentos):
    etapas = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |   / \\
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |   / 
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |    
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    |
           |    
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    |
           |    
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           |    
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           |    
        '''
    ]
    return etapas[6 - intentos]  # Mostrar según intentos restantes

def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos_restantes = 6
    letras_incorrectas = []
    
    print("¡Bienvenido al juego del ahorcado!")
    
    while True:
        print("\n" + dibujar_ahorcado(intentos_restantes))
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        
        if intentos_restantes == 0:
            print(f"\n¡Perdiste! La palabra era: {palabra_secreta}")
            break
            
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"\n¡Felicidades! ¡Adivinaste la palabra: {palabra_secreta}!")
            break
        
        letra = input("Ingresa una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa solo una letra válida.")
            continue
            
        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya has intentado con esa letra.")
            continue
            
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto! La letra está en la palabra.")
        else:
            letras_incorrectas.append(letra)
            intentos_restantes -= 1
            print("Incorrecto. Pierdes un intento.")
    
    jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        jugar_ahorcado()
    else:
        print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_ahorcado()
