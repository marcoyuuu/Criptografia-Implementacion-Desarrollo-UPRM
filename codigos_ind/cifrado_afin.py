def inverso_modulo(a, m):
    """
    Función para calcular el inverso multiplicativo de 'a' bajo el módulo 'm' utilizando el algoritmo extendido de Euclides, o sea un número x tal que (a * x) % m = 1.
    
    :param a: Entero, el número del cual se busca el inverso multiplicativo.
    :param b: Entero, el módulo bajo el cual se busca el inverso multiplicativo.
    :return: inverso multiplicativo de a bajo el módulo m si existe. Si a y m no son coprimos, retorna una cadena de texto indicando que no hay inverso porque gcd(a, m) > 1.
    """
    # Inicializa variables para el algoritmo extendido de Euclides
    d0, d1 = a, m
    x0, x1 = 1, 0  # x0 es el coeficiente para 'a' en la combinación lineal, x1 para 'm'

    # Itera mientras el resto de la división no sea cero
    while d1 != 0:
        q = d0 // d1  # Calcula el cociente de la división
        d2 = d0 - q * d1  # Actualiza d0 a d1, y d1 a d2, que es el nuevo resto
        x2 = x0 - q * x1  # Actualiza x0 a x1, y x1 a x2, que es el nuevo coeficiente de 'a'

        # Prepara la siguiente iteración
        x0, x1 = x1, x2
        d0, d1 = d1, d2

    # Verifica si el último resto no nulo es 1, lo que significa que 'a' y 'm' son coprimos
    if d0 == 1:
        return x0 % m  # Retorna el coeficiente de 'a' como el inverso, asegurándose de que sea positivo
    else:
        # Si gcd(a, m) > 1, entonces no hay inverso
        return 'gcd(a, m) > 1'  # Retorna un mensaje de error

def cifrar_afin(texto, a, b, m=26):
    """
    Función para cifrar un texto usando el cifrado afín, aplicando una transformación lineal a cada carácter alfabético basada en coeficientes específicos, dejando los caracteres no alfabéticos intactos.
    
    :param texto: Cadena de texto a cifrar
    :param a: Entero, el coeficiente multiplicativo en el cifrado afín.
    :param b: Entero, el término constante en el cifrado afín.
    :param m: Entero, representa el tamaño del alfabeto (por defecto 26 para el alfabeto inglés).
    :return: El texto cifrado según el cifrado afín. Las letras alfabéticas son transformadas según la fórmula (a * x + b) % m, donde x es la posición de la letra en el alfabeto (0 a 25). Los caracteres no alfabéticos son dejados intactos.
    """
    resultado = ''
    for char in texto:
        if char.isalpha():  # Verificar si el carácter es una letra del alfabeto
            # Convertir char a su posición en el alfabeto [0-25]
            x = ord(char.lower()) - ord('a')
            # Aplicar la fórmula de cifrado
            cifrado = (a * x + b) % m
            # Convertir de nuevo a un carácter y añadir al resultado
            resultado += chr(cifrado + ord('a'))
        else:
            # Para caracteres no alfabéticos, añadirlos tal cual
            resultado += char
    return resultado

def descifrar_afin(texto, a, b, m=26):
    """
    Función para descrifrar un texto cifrado usando cifrado afín, aplicando la operación inversa, solo si existe un inverso modular para el coeficiente multiplicativo.
    Devuelve el texto original o un mensaje de error si el inverso no existe.
    
    :param texto: Cadena de texto a descifrar
    :param a: Entero, el coeficiente multiplicativo en el cifrado afín.
    :param b: Entero, el término constante en el cifrado afín.
    :param m: Entero, representa el tamaño del alfabeto (por defecto 26 para el alfabeto inglés).
    :return: El texto descifrado según el cifrado afín.
    """
    resultado = ''
    a_inv = inverso_modulo(a, m)  # Encontrar el inverso multiplicativo modular de a módulo m
    if isinstance(a_inv, str):  # Verificar si inverso_modulo devolvió un mensaje de error
        return a_inv  # Devolver el mensaje de error si mcd(a, m) > 1
    for char in texto:
        if char.isalpha():  # Verificar si el carácter es una letra del alfabeto
            # Convertir char a su posición en el alfabeto [0-25]
            x = ord(char.lower()) - ord('a')
            # Aplicar la fórmula de descifrado
            descifrado = a_inv * (x - b) % m
            # Convertir de nuevo a un carácter y añadir al resultado
            resultado += chr(descifrado + ord('a'))
        else:
            # Para caracteres no alfabéticos, añadirlos tal cual
            resultado += char
    return resultado

def test_cifrar_afin():
    """
    Test cases para verificar la funcionalidad de cifrar_afin
    """
    print("Iniciando pruebas de cifrado...")
    # Test 1
    assert cifrar_afin('abc', 3, 5) == 'fil', "Test 1 falló"
    print("Test 1 (cifrar 'abc' con a=3, b=5): PASÓ")
    # Test 2
    assert cifrar_afin('hello', 7, 3) == 'afccx', "Test 2 falló"
    print("Test 2 (cifrar 'hello' con a=7, b=3): PASÓ")
    print("Todas las pruebas de cifrado se aprobaron exitosamente.")

def test_descifrar_afin():
    """
    Test cases para verificar la funcionalidad de descifrar_afin
    """
    print("\nIniciando pruebas de descifrado...")
    # Test 1
    assert descifrar_afin('fil', 3, 5) == 'abc', "Test 1 falló"
    print("Test 1 (descifrar 'fil' con a=3, b=5): PASÓ")    # Test 2
    # Test 2
    assert descifrar_afin('afccx', 7, 3) == 'hello', "Test 2 falló"
    print("Test 2 (descifrar 'afccx' con a=7, b=3): PASÓ")
    print("¡Todas las pruebas de descifrado se aprobaron exitosamente!")

# Llamar a las funciones de prueba
test_cifrar_afin()
test_descifrar_afin()
