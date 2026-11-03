try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
except ValueError:
    print("Error: Debes introducir un valor numérico válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")