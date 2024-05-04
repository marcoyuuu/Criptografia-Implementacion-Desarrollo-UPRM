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

def prueba_de_primalidad_fermat(n, k):
    """
    Realiza la prueba de primalidad de Fermat en un número n, repitiendo la prueba k veces.

    :param n: Entero, el número a testear para primalidad.
    :param k: Entero, el número de veces que se realizará la prueba para aumentar la certeza de la primalidad.
    :return: True si n es probablemente primo, False si n es compuesto.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(2, n - 2)
        resultado = square_and_multiply(a, n - 1, n)        
        if resultado != 1:
            return False
    return True

# Test cases para verificar la funcionalidad de la prueba de primalidad de Fermat
def test_fermat_primality():
    # Este número es un número de Carmichael, puede pasar la prueba pero no debe considerarse definitivamente como primo.
    assert not prueba_de_primalidad_fermat(561, 10)
    print("Prueba de primalidad para n = 561 (un número de Carmichael)")
    prueba_de_primalidad_fermat(561, 10)  # Número de Carmichael

    # Este número es primo, debería pasar siempre.
    assert prueba_de_primalidad_fermat(13, 10)
    print("\nPrueba de primalidad para n = 13")
    prueba_de_primalidad_fermat(13, 10)  # Número primo

    # Este número es compuesto, debería fallar.
    assert not prueba_de_primalidad_fermat(15, 10)
    print("\nPrueba de primalidad para n = 15")
    prueba_de_primalidad_fermat(15, 10)  # Número compuesto

    print("\n¡Todas las pruebas de la prueba de primalidad de Fermat se aprobaron exitosamente!")

test_fermat_primality()
