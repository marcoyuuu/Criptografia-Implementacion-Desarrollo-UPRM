import random
import string

def cifrar(texto_plano):
    """
    Función para cifrar un texto usando el cifrado de flujo con XOR. 
    Genera una clave aleatoria del mismo tamaño que el texto y aplica XOR entre el texto y la clave.
    
    :param texto_plano: cadena de texto que se desea cifrar.
    :return: Tupla de dos elementos: 
        Primer elemento: texto_cifrado es una cadena de texto resultante de aplicar la operación XOR entre cada carácter del texto plano y la clave aleatoria generada.
        Segundo elemento: clave, que es una cadena de texto generada aleatoriamente y que tiene la misma longitud que el texto plano.
    """
    clave = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(texto_plano)))
    texto_cifrado = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(texto_plano, clave))
    return texto_cifrado, clave

def descifrar(texto_cifrado, clave):
    """
    Función para descifrar un texto cifrado usando el mismo método de cifrado de flujo con XOR.
    Utiliza la clave proporcionada para aplicar XOR entre el texto cifrado y la clave y recuperar el texto original.
    
    :param texto_cifrado: cadena de texto que ha sido cifrado previamente.
    :param clave: cadena de texto utilizada para cifrar el texto original, necesaria para descifrar el texto.
    :return: texto_descifrado, que es una cadena de texto recuperada aplicando la operación XOR entre cada carácter del texto cifrado y el carácter correspondiente de la clave proporcionada.
    """
    texto_descifrado = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(texto_cifrado, clave))
    return texto_descifrado

def test_cifrado_descifrado():
    """
    Pruebas para verificar la funcionalidad de cifrado y descifrado. 
    Cifra un texto, luego lo descifra usando la misma clave y verifica si el texto descifrado es igual al texto original.
    """
    texto_plano = "Alci dame 100"
    print(f"Test: Texto plano = '{texto_plano}'")
    
    texto_cifrado, clave_generada = cifrar(texto_plano)
    print("Clave generada automáticamente:", clave_generada)
    print("Texto cifrado:", texto_cifrado)

    texto_descifrado = descifrar(texto_cifrado, clave_generada)
    assert texto_descifrado == texto_plano, "El texto descifrado debe ser igual al texto plano"
    print("Resultado del descifrado:", texto_descifrado, "=", texto_plano)
    print("Cifrado seguido de descifrado con la misma clave funciona correctamente.")

test_cifrado_descifrado()
