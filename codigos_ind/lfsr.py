import random

def lfsr_generate_initial_state(degree):
    """
    Genera un estado inicial aleatorio para un LFSR según el grado del polinomio.
    
    :param degree: Entero que representa el grado más alto del polimonio usado para el LFSR
    :return: Lista de bits aleatorios (0 o 1) de longitud igual al grado del polinomio. Esta lista representa el estado inicial del LFSR.
    """

    return [random.randint(0, 1) for _ in range(degree)]

def lfsr(estado_inicial, taps):
    """
    Ejecuta el LFSR. Calcula un nuevo bit usando XOR en las posiciones especificadas por los taps, 
    desplaza todos los bits en el registro un lugar hacia adelante, y coloca el nuevo bit al final del registro.
    
    :param estado_inicial: Una lista de enteros de bits (0 o 1) que representa el estado actual del LFSR al inicio de la función. Generado por función lfsr_generate_initial_state(degree).
    :param taps: Una lista de enteros que especifica las posiciones en el registro estado_inicial que se utilizarán para calcular el nuevo bit mediante operaciones XOR.
    :return: bit_salida: un entero que representa el bit que es "expulsado" del registro como resultado del desplazamiento.
    """
    nuevo_bit = 0
    for pos in taps:
        nuevo_bit ^= estado_inicial[pos]  # Usando 0-indexado

    # Capturar el bit que será "expulsado" del registro
    bit_salida = estado_inicial[0]

    # Desplazar los bits hacia adelante y añadir el nuevo bit al final
    for i in range(len(estado_inicial) - 1):
        estado_inicial[i] = estado_inicial[i + 1]
    estado_inicial[-1] = nuevo_bit

    return bit_salida

# Test case
degree = 8  # Grado del polinomio máximo, que corresponde al número de bits en el estado inicial
estado_inicial = lfsr_generate_initial_state(degree)  # Genera estado inicial automáticamente
taps = [0, 1, 2, 3, 7]  # Taps con polinomio 1 + x + x^3 + x^4 + x^8

print("Estado inicial del LFSR:", estado_inicial, "Auto-generado")
print("\nTaps utilizados (0-indexado):", taps)

# Generar 16 bits de salida del LFSR para simular los dos primeros bytes de salida
salida_bytes = []
for _ in range(16):
    bit_salida = lfsr(estado_inicial, taps)
    salida_bytes.append(bit_salida)

print("\nLos primeros 16 bits generados por el LFSR son:", salida_bytes)
print("\nRepresentación hexadecimal de los primeros dos bytes:", ''.join(str(bit) for bit in salida_bytes[:8]), ''.join(str(bit) for bit in salida_bytes[8:]))

# Calculando el valor en hexadecimal como se muestra en la imagen
primer_byte = int(''.join(str(bit) for bit in salida_bytes[:8]), 2)
segundo_byte = int(''.join(str(bit) for bit in salida_bytes[8:]), 2)
print(f"En hexadecimal, los dos primeros bytes son: {primer_byte:02X} {segundo_byte:02X}")

