from math import gcd
import random

def extended_euclidean(a, b):
    """
    Calcula el máximo común divisor de a y b junto con los coeficientes de Bézout,
    que son los enteros x e y tales que ax + by = gcd(a, b).

    :param a: Entero, uno de los números para calcular el máximo común divisor (GCD).
    :param b: Entero, el otro número para calcular el GCD.
    :return: Una tupla (g, x, y) donde g es el gcd y x, y son los coeficientes de Bézout que satisfacen la ecuación ax + by = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_euclidean(b % a, a)
        return g, y - (b // a) * x, x

def square_and_multiply(base, exponent, modulo):
    """
    Realiza la exponenciación modular usando el método Square-and-Multiply,
    que es eficiente para calcular grandes potencias bajo módulos grandes.

    :param base: Entero, la base de la exponenciación.
    :param exponent: Entero, el exponente al que se eleva la base.
    :param modulo: Entero, el módulo bajo el cual se realiza la operación.
    :return: Entero, el resultado de (base^exponent) % modulo.
    """
    resultado = 1  # Inicializa el resultado a 1.
    base = base % modulo  # Reduce la base bajo el módulo para simplificar los cálculos.

    # Itera mientras haya bits en el exponente.
    while exponent > 0:
        if exponent & 1:  # Si el bit menos significativo es 1.
            resultado = (resultado * base) % modulo  # Multiplica la base actual al resultado.
        
        base = (base * base) % modulo  # Cuadrado de la base.
        exponent = exponent >> 1  # Desplaza el exponente un bit a la derecha.

    return resultado


def prueba_de_primalidad_miller_rabin(n, k):
    """
    Realiza la prueba de primalidad de Miller-Rabin en un número n, repitiendo la prueba k veces.

    :param n: Entero, el número a testear para primalidad.
    :param k: Entero, el número de veces que se realizará la prueba para aumentar la certeza de la primalidad.
    :return: True si n es probablemente primo, False si n es compuesto.
    """
    if n < 2:
        return False
    if n in {2, 3}:
        return True
    if n % 2 == 0:
        return False

    # Descomponer n-1 como 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(k):
        a = random.randint(2, n - 2)
        x = square_and_multiply(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for r in range(s - 1):
            x = square_and_multiply(x, 2, n)
            if x == n - 1:
                break
        else:
            print(f"a = {a}, falló con x = {x}, {n} es definitivamente compuesto.")
            return False

    print(f"Todos los tests pasaron: {n} es probablemente primo.")
    return True

def generar_primo(bits, k):
    """
    Genera un número primo de 'bits' bits de longitud utilizando la prueba de primalidad de Miller-Rabin.
    
    :param bits: Entero, la cantidad de bits del número primo deseado.
    :param k: Entero, el número de rondas de la prueba de Miller-Rabin para asegurar la primalidad.
    :return: Un número primo de 'bits' bits.
    """
    while True:
        # Generar un número aleatorio impar de 'bits' bits
        primo = random.getrandbits(bits)
        primo |= (1 << bits - 1) | 1  # Asegurar el bit más significativo y el menos significativo
        
        if prueba_de_primalidad_miller_rabin(primo, k):
            return primo

def generar_claves_rsa(bits):
    """
    Genera una clave pública y una clave privada para el cifrado RSA utilizando números primos generados con especificación de bits.
    
    :param bits: Entero, la cantidad de bits para cada número primo.
    :return: Una tupla con la clave pública (e, n) y la clave privada (d, n).
    """
    k = 20  # Número de pruebas para Miller-Rabin
    p = generar_primo(bits // 2, k)
    q = generar_primo(bits // 2, k)
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi_n) > 1:
        e += 1

    _, d, _ = extended_euclidean(e, phi_n)
    d = d % phi_n
    if d < 0:
        d += phi_n

    return (e, n), (d, n)


def cifrar(mensaje, clave_publica):
    """
    Cifra un mensaje usando la clave pública RSA.

    :param mensaje: Cadena, el mensaje a cifrar, representado como un entero.
    :param clave_publica: La clave pública RSA, una tupla (e, n)
    :return: El mensaje cifrado como un entero, calculado como mensaje^e mod n.
    """
    e, n = clave_publica
    return pow(mensaje, e, n)

def descifrar(cifrado, clave_privada):
    """
    Descifra un mensaje cifrado usando la clave privada RSA.

    :param cifrado: El mensaje cifrado, representado como un entero.
    :param clave_privada: La clave privada RSA, una tupla (d, n)
    :return: El mensaje descifrado como un entero, calculado como cifrado^d mod n.
    """
    d, n = clave_privada
    return pow(cifrado, d, n)

# Test Cases para verificar la funcionalidad del algoritmo RSA
def test_rsa():
    print("Iniciando prueba del algoritmo RSA...")
    bits = 512  # Tamaño del primo en bits
    mensaje_original = 65  # Mensaje a cifrar y descifrar

    print("Generando claves pública y privada...")
    clave_publica, clave_privada = generar_claves_rsa(bits)

    print(f"Clave pública (e, n): {clave_publica}")
    print(f"Clave privada (d, n): {clave_privada}")

    print("Cifrando el mensaje...")
    mensaje_cifrado = cifrar(mensaje_original, clave_publica)
    print(f"Mensaje Cifrado: {mensaje_cifrado}")

    print("Descifrando el mensaje...")
    mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada)
    print(f"Mensaje Descifrado: {mensaje_descifrado}")

    assert mensaje_original == mensaje_descifrado, "El mensaje descifrado debe ser igual al mensaje original"

    print("\n¡Todas las pruebas del algoritmo RSA se aprobaron exitosamente!")

test_rsa()
