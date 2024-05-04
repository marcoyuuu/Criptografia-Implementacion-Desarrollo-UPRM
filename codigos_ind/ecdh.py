import random

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
    :param k: Entero, el número de veces que se realizará la prueba para asegurar la certeza de la primalidad.
    :return: Un número primo de 'bits' bits.
    """
    while True:
        primo = random.getrandbits(bits)
        primo |= (1 << bits - 1) | 1  # Asegurar el bit más significativo y el menos significativo
        if primo % 2 == 0:
            primo += 1  # Asegurarse de que sea impar
        
        if prueba_de_primalidad_miller_rabin(primo, k):
            return primo

def point_addition(P, Q, p, a):
    """
    Realiza la adición de dos puntos en una curva elíptica sobre un campo finito.
    
    :param P: Tupla que representa el primer punto (x1, y1).
    :param Q: Tupla que representa el segundo punto (x2, y2).
    :param p: Número primo que define el módulo para la aritmética.
    :param a: Coeficiente 'a' de la ecuación de la curva elíptica.
    :return: Tupla representando el punto resultante de la adición.
    """
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    if P[0] == Q[0] and P[1] != Q[1]:
        return (0, 0)  # Puntos son inversos
    if P == Q:
        lam = (3 * P[0]**2 + a) * pow(2 * P[1], p-2, p) % p
    else:
        lam = (Q[1] - P[1]) * pow(Q[0] - P[0], p-2, p) % p
    
    x3 = (lam**2 - P[0] - Q[0]) % p
    y3 = (lam * (P[0] - x3) - P[1]) % p
    return (x3, y3)

def scalar_multiplication(P, k, p, a):
    """
    Realiza la multiplicación de un punto por un escalar en una curva elíptica usando el método double-and-add.
    
    :param P: Tupla de enteros, punto inicial (x, y) en la curva.
    :param k: Entero, escalar por el que se multiplicará el punto.
    :param p: Entero, número primo que define el módulo para la aritmética.
    :param a: Entero, coeficiente 'a' de la ecuación de la curva elíptica.
    :return: Tupla de enteros representando el punto resultante de la multiplicación.
    """
    R = (0, 0)  # Punto en el infinito
    Q = P
    while k:
        if k & 1:
            R = point_addition(R, Q, p, a)
        Q = point_addition(Q, Q, p, a)
        k >>= 1
    return R

def intercambio_de_claves_ecdh(bits, G, a, a_priv, b_priv):
    """
    Realiza el intercambio de claves ECDH utilizando curvas elípticas.
    
    :param bits: Entero, número de bits para el primo que se usará como módulo.
    :param G: Tupla de enteros, punto generador de la curva.
    :param a: Entero, coeficiente 'a' de la ecuación de la curva.
    :param a_priv: Entero, secreto privado de Alice.
    :param b_priv: Entero, secreto privado de Bob.
    :return: Tupla de enteros representando las claves compartidas calculadas por Alice y Bob.
    """
    k = 20  # Número de pruebas para Miller-Rabin
    p = generar_primo(bits, k)  # Generar un número primo de 'bits' bits
    
    # Generación de puntos públicos
    A_pub = scalar_multiplication(G, a_priv, p, a)
    B_pub = scalar_multiplication(G, b_priv, p, a)

    # Cálculo de las claves compartidas
    clave_compartida_Alice = scalar_multiplication(B_pub, a_priv, p, a)
    clave_compartida_Bob = scalar_multiplication(A_pub, b_priv, p, a)

    return clave_compartida_Alice, clave_compartida_Bob

# Test
def test_ecdh():
    print("Iniciando la prueba ECDH...")
    bits = 512  # Tamaño del primo en bits
    G = (5, 1)  # Punto generador de la curva elíptica
    a = 1       # Coeficiente de la curva y^2 = x^3 + ax + b
    a_priv = 123456  # Secreto privado de Alice
    b_priv = 654321  # Secreto privado de Bob

    print("Generando claves públicas...")
    clave_Alice, clave_Bob = intercambio_de_claves_ecdh(bits, G, a, a_priv, b_priv)
    assert clave_Alice == clave_Bob, "Las claves compartidas deben ser iguales."

    print("Claves públicas generadas y verificadas.")
    print("Clave compartida de Alice y Bob: ", clave_Alice)
    print("\n¡Todas las pruebas del Intercambio de Claves ECDH con Curvas Elípticas se aprobaron exitosamente!")

test_ecdh()
