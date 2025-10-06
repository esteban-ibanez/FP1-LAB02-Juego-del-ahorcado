import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip()
    res = ""
    for c in cadena:
        if c =="á":
            res +="a"
        elif c =="ú" or c == "ü":
            res += "u"
        elif c =="í":
            res += "i"
        elif c =="ó":
             res += "o"
        elif c=="é":  
            res += "e"
        else:
           res += c 
    return res
            
    

def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    res=""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            res += letra
        else:
            res += "_"
    return res
    
    


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if "_" in palabra_enmascarada:
        return False
    else:
        return True

def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    print(f"Estado :{' '.join(palabra_enmascarada)}")
    if len(letras_usadas) == 0:
        print("Letras usadas: ninguna")
    else:
        print(f"Letras usadas: {letras_usadas}")

    print(f"Intentos restantes: {intentos_restantes}")
    

def pedir_letra(letras_usadas=""):

    while True:
        letra=input("Dígame una letra: ")
        if letra.isdigit():
            print("Debe introducir una letra") 
        elif len(letra) >1:
            print("Debes introducir una única letra")
        elif letra in letras_usadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            return letra.lower()
    
    
    
def jugar(palabra_secreta,intentos_restantes=6):
    
    palabra_secreta = normalizar(palabra_secreta)
    
    if palabra_secreta == "":
        return None
    
    palabra_enmascarada = ocultar(palabra_secreta)
    
    letras_usadas = ""
    
    while intentos_restantes>0 and not ha_ganado(palabra_secreta):
        mostrar_estado(palabra_enmascarada,letras_usadas,intentos_restantes)
        letra = pedir_letra(letras_usadas) 
        letras_usadas += letra
        
        if letra not in palabra_secreta:
            print("la letra no se encuentra en la palabra...")
            intentos_restantes -=  1
        else:
            print(f"Correcto {letra} pertenece a la palabra...")
            palabra_enmascarada = ocultar(palabra_secreta,letras_usadas)
    
    if ha_ganado(palabra_enmascarada):
         print(f"Felicidades, has ganado, la palabra secreta era: {palabra_secreta}")
    else:
        print(f"Lo siento, has perdido, la próxima vez será, la palabra secreta era: {palabra_secreta}")
            
            
    

