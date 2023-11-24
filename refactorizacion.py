def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2  

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"
    
def calcular(operacion, num1, num2):
    operaciones = {
        'suma': suma,
        'resta': resta,
        'multiplicacion': multiplicacion,
        'division': division
    }

    if operacion in operaciones:
        return operaciones[operacion](num1, num2)
    else:
        raise ValueError("Operación no soportada.")
    
def main():
    operacion = input("¿Qué operación quieres realizar? (suma, resta, multiplicacion, division): ")
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    try:
        resultado = calcular(operacion, num1, num2)
        print("El resultado de la operación es: {}".format(resultado))
    except ValueError as e:
        print(e)
        
main()