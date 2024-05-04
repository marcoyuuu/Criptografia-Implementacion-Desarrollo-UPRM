import random

def square_and_multiply(base, exponent, modulo):
    """
    Realiza la exponenciación modular usando el método Square-and-Multiply.

    :param base: Entero, la base de la exponenciación.
    :param exponent: Entero, el exponente al que se eleva la base.
    :param modulo: Entero, el módulo bajo el cual se realiza la operación.
    :return: Entero, el resultado de (base^exponent) % modulo.
    """
    resultado = 1
    base = base % modulo
    while exponent > 0:
        if exponent & 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        exponent = exponent >> 1
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

def intercambio_de_claves_elGamal(bits, g, a, b):
    """
    Simula el intercambio de claves usando el protocolo de ElGamal con un número primo generado de longitud de bits especificada.
    
    :param bits: Entero, número de bits para el primo que se usará como módulo.
    :param g: Entero, la base de las operaciones exponenciales.
    :param a: Entero, el secreto privado de Alice.
    :param b: Entero, el secreto privado de Bob.
    :return: Tupla de enteros, las claves compartidas calculadas por Alice y Bob.
    """
    k = 20  # Número de pruebas para Miller-Rabin
    p = generar_primo(bits, k)  # Generar un número primo de 'bits' bits

    # Generación de claves públicas
    A = square_and_multiply(g, a, p)
    B = square_and_multiply(g, b, p)

    print(f"Alice's public key: A = {A}")
    print(f"Bob's public key: B = {B}\n")

    # Cálculo de las claves compartidas
    clave_compartida_Alice = square_and_multiply(B, a, p)
    clave_compartida_Bob = square_and_multiply(A, b, p)

    print(f"Alice's shared key: {clave_compartida_Alice}")
    print(f"Bob's shared key: {clave_compartida_Bob}\n")

    # Verificación de las claves compartidas
    if clave_compartida_Alice == clave_compartida_Bob:
        print("El intercambio de claves fue exitoso.\n")
    else:
        print("Error en el intercambio de claves.\n")

    return clave_compartida_Alice, clave_compartida_Bob

# Test cases para verificar la funcionalidad del intercambio de claves ElGamal
def test_elGamal_key_exchange():
    print("Iniciando prueba de intercambio de claves ElGamal...")
    bits = 512  # Tamaño del primo en bits
    g = 2       # Una base comúnmente usada
    a = 123456  # Secreto privado de Alice
    b = 654321  # Secreto privado de Bob

    print("Generando número primo para el módulo...")
    clave_Alice, clave_Bob = intercambio_de_claves_elGamal(bits, g, a, b)

    print("Verificando que las claves compartidas sean iguales...")
    assert clave_Alice == clave_Bob, "Las claves compartidas deben ser iguales."

    print("¡Todas las pruebas del intercambio de claves ElGamal se aprobaron exitosamente!")

test_elGamal_key_exchange()
