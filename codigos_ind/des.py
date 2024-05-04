import random

# Cajas S (Cajas de sustitución)
S_BOX = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Tabla de permutación inicial
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Tabla de permutación final
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Tabla de expansión (E)
E = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

# Permutación P (después de las S-Cajas S)
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Tabla de permutación PC1 para DES (elimina bits de paridad y reordena la clave)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# Tabla de permutación PC2 para DES (selecciona y reordena los bits para formar las subclaves)
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Calendario de rotaciones para las subclaves
ROTATION_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permutar(data, tabla):
    """
    Aplica una permutación definida por la tabla dada al data proporcionado.
    
    :param data: Lista de bits a permutar.
    :param tabla: Tabla de permutación que define el orden de los bits.
    :return: Lista de bits permutados.
    """
    return [data[i - 1] for i in tabla]

def dividir_bloque(data):
    """
    Divide el bloque de datos en dos mitades.
    
    :param data: Lista de bits.
    :return: Dos listas de bits, correspondientes a las mitades izquierda y derecha.
    """
    mitad = len(data) // 2
    return data[:mitad], data[mitad:]

def xor_bits(a, b):
    """
    Realiza una operación XOR entre dos listas de bits.
    
    :param a: Primer lista de bits.
    :param b: Segunda lista de bits.
    :return: Lista de bits resultante.
    """
    return [x ^ y for x, y in zip(a, b)]

# Tablas de conversión para S-Boxes
S_BOX_CONVERSION = [
    [
        [(x >> 4) & 0b11, x & 0b1111] for x in range(64)
    ] for _ in range(8)
]

def apply_s_box(block, sbox):
    """
    Aplica las S-Boxes a un bloque de bits expandidos.

    :param block: Bloque de bits expandidos de 48 bits.
    :param sbox: Cajas S definida.
    :return: Bloque de 32 bits después de aplicar las S-Boxes.
    """
    output = []
    for i in range(8):
        row, col = S_BOX_CONVERSION[i][((block[i*6] << 4) | (block[i*6 + 5]))]
        value = sbox[i][row][col]
        output += [int(x) for x in format(value, '04b')]
    return output

def function_f(right, subkey):
    """
    Función F usada en cada ronda de DES.
    
    :param right: La mitad derecha del texto (32 bits).
    :param subkey: Subclave para esta ronda (48 bits).
    :return: Salida de 32 bits de la función F.
    """
    expanded = permutar(right, E)
    mixed = xor_bits(expanded, subkey)
    substituted = apply_s_box(mixed, S_BOX)
    return permutar(substituted, P)

def rotar_izquierda(bits, n):
    """
    Rota una lista de bits hacia la izquierda n veces.
    
    :param bits: Lista de bits a rotar.
    :param n: Número de rotaciones a la izquierda.
    :return: Lista de bits rotada.
    """
    n = n % len(bits)  # Asegurar que n no excede la longitud de la lista
    return bits[n:] + bits[:n]

def generate_subkeys(key):
    """
    Genera las subclaves para las rondas de cifrado DES.

    :param key: Clave de 64 bits (56 + 8 bits de paridad).
    :return: Lista de 16 subclaves de 48 bits cada una.
    """
    # Permutación PC-1
    pc1_key = permutar(key, PC1)

    # División en mitades C0 y D0
    c, d = dividir_bloque(pc1_key)

    subkeys = []
    for i in range(16):
        # Rotación según la tabla de rotación
        c = rotar_izquierda(c, ROTATION_SCHEDULE[i])
        d = rotar_izquierda(d, ROTATION_SCHEDULE[i])

        # Combinación y permutación PC-2
        combined = c + d
        subkey = permutar(combined, PC2)
        subkeys.append(subkey)

    return subkeys

def cifrado_des(texto_plano, clave):
    """
    Cifra un bloque de texto plano utilizando la clave proporcionada según el estándar DES.
    
    :param texto_plano: Bloque de 64 bits de datos a cifrar.
    :param clave: Clave de 64 bits utilizada para cifrar.
    :return: Bloque de 64 bits de datos cifrados.
    """
    subclaves = generate_subkeys(clave)
    texto_permutado = permutar(texto_plano, IP)
    izquierda, derecha = dividir_bloque(texto_permutado)

    for i in range(16):
        temp_izquierda = derecha
        derecha = xor_bits(izquierda, function_f(derecha, subclaves[i]))
        izquierda = temp_izquierda

    texto_pre_cifrado = derecha + izquierda  # Nota el intercambio final de derecha e izquierda
    texto_cifrado = permutar(texto_pre_cifrado, FP)
    return texto_cifrado

def descifrado_des(texto_cifrado, clave):
    """
    Descifra un bloque de texto cifrado utilizando la clave proporcionada según el estándar DES.
    
    :param texto_cifrado: Bloque de 64 bits de datos cifrados.
    :param clave: Clave de 64 bits utilizada para descifrar.
    :return: Bloque de 64 bits de datos descifrados.
    """
    # Generar subclaves para las rondas de cifrado
    subclaves = generate_subkeys(clave)
    # Aplicar la permutación inicial
    texto_permutado = permutar(texto_cifrado, IP)
    izquierda, derecha = dividir_bloque(texto_permutado)

    # Realizar 16 rondas utilizando las subclaves en orden inverso
    for i in range(16):
        temp_izquierda = derecha
        # Usar la subclave desde la última hasta la primera
        derecha = xor_bits(izquierda, function_f(derecha, subclaves[15 - i]))
        izquierda = temp_izquierda

    # Nota el intercambio final de derecha e izquierda no se deshace aquí
    texto_pre_descifrado = derecha + izquierda  # Intercambio final hecho en cifrado, no se deshace en descifrado
    texto_descifrado = permutar(texto_pre_descifrado, FP)
    return texto_descifrado

# Test 
def test_des():
    print("Iniciando prueba del algoritmo DES...")

    # Generar datos de prueba
    texto_plano = [random.randint(0, 1) for _ in range(64)]  # Bloque de texto plano de ejemplo
    clave = [random.randint(0, 1) for _ in range(64)]  # Clave de 64 bits (incluyendo 8 bits de paridad)

    print("Texto plano original (fragmento):", texto_plano[:10])
    print("Clave (fragmento):", clave[:10])

    # Cifrar el texto plano
    texto_cifrado = cifrado_des(texto_plano, clave)
    print("Texto cifrado (fragmento):", texto_cifrado[:10])

    # Función de descifrado (ficticia, asumiendo que existe)
    texto_descifrado = descifrado_des(texto_cifrado, clave)
    print("Texto descifrado (fragmento):", texto_descifrado[:10])

    # Verificar que el texto descifrado coincide con el texto original
    assert texto_plano == texto_descifrado, "El texto descifrado debe ser igual al texto original"
    print("El texto descifrado coincide con el texto original.")

    print("\n¡Todas las pruebas del algoritmo DES se aprobaron exitosamente!")
    
test_des()
