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

# Test cases para verificar la funcionalidad del algoritmo Square-and-Multiply
def test_square_and_multiply():
    assert square_and_multiply(2, 10, 1000) == 24, "Test case 1 failed"
    print("Test Case 1: 2^10 % 1000", "=", square_and_multiply(2, 10, 1000))

    assert square_and_multiply(3, 7, 13) == 3, "Test case 2 failed"
    print("\nTest Case 2: 3^7 % 13", "=", square_and_multiply(3, 7, 13))
    
    assert square_and_multiply(5, 117, 19) == 1, "Test case 3 failed"
    print("\nTest Case 3: 5^117 % 19", "=", square_and_multiply(5, 117, 19))
    
    assert square_and_multiply(10, 1000, 991) == 353, "Test case 4 failed"
    print("\nTest Case 4: 10^1000 % 991", "=", square_and_multiply(10, 1000, 991))

    print("\n¡Todas las pruebas del algoritmo Square-and-Multiply se aprobaron exitosamente!")

# Ejecutar los tests para validar la implementación
test_square_and_multiply()
