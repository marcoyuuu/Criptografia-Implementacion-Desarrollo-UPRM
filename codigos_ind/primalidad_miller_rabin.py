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

# Test cases para verificar la funcionalidad de la prueba de primalidad de Miller-Rabin
def test_miller_rabin_primality():
    # Número de Carmichael 561 fallará con Miller-Rabin
    print("Test 1: Número de Carmichael 561")
    resultado = prueba_de_primalidad_miller_rabin(561, 10)
    assert not resultado, "561 debería identificarse como compuesto debido a que es un número de Carmichael."
    print("561, un número de Carmichael, correctamente identificado como compuesto.\n")
    
    # Número primo 13 debería pasar
    print("Test 2: Número primo 13")
    resultado = prueba_de_primalidad_miller_rabin(13, 10)
    assert resultado, "13 debería identificarse como primo."
    print("13, un número primo, correctamente identificado como primo.\n")
    
    # Número compuesto 15 debería fallar
    print("Test 3: Número compuesto 15")
    resultado = prueba_de_primalidad_miller_rabin(15, 10)
    assert not resultado, "15 debería identificarse como compuesto."
    print("15, un número compuesto, correctamente identificado como compuesto.\n")

    print("¡Todas las pruebas de primalidad de Miller-Rabin se aprobaron exitosamente!")


test_miller_rabin_primality()
