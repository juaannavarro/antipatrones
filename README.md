# antipatrones


## Ejercicio práctico: Identificación y refactorización de antipatrón "Spaghetti Code" en Python:

Un antipatrón de programación es un patrón que puede ser considerado una mala práctica. "Spaghetti Code" es un antipatrón que se refiere a código con una estructura de control compleja, difícil de leer y seguir, generalmente debido a múltiples saltos de control, como instrucciones GOTO, ciclos y excepciones.

## Enunciado del ejercicio:

Dada una porción de código Python escrita en estilo "Spaghetti Code", se te pide que identifiques las principales características de este antipatrón y refactorices el código para mejorar su legibilidad y mantenibilidad.

Considera el siguiente fragmento de código:

``` 
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")

```
Las funciones deberían tener una sola responsabilidad, y esta función tiene muchas. También se pueden observar problemas como la falta de modularización, uso de cadenas de texto para la lógica de control, y falta de manejo de errores.

## Criterio de evaluación:

### 1.Identificación de características de "Spaghetti Code": Debes ser capaz de identificar las características de "Spaghetti Code" en el código proporcionado. (20%)
Como hemos dicho antes, el spaghetti code es un ejemplo de código lioso, difícil de leer y seguir. Al ser un ejemplo de código tan simple y breve no se aprecia bien directamente en el código pero sí respecto al que he remodelado a continuación. 

### 2.Refactorización de código: Debes ser capaz de refactorizar el código para mejorar su legibilidad y mantenibilidad. Esto podría incluir la eliminación de la lógica de control basada en cadenas de texto, la modularización del código, y la mejora del manejo de errores. (60%)
``` 
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
```

### 3.Justificación de cambios: Debes ser capaz de justificar los cambios que has hecho al código, explicando cómo estos cambios mejoran el código y cómo evitan las características de "Spaghetti Code". (20%)

En este caso he creado varios métodos y un método principal que incluye a todos los anteriores, que es el calcular, ya que en el código original, la función calcular maneja múltiples operaciones matemáticas y el control de errores.Después llamamos a un nuevo método que es el main donde ejecutaremos todo. Esto sí es un ejemplo de código fácil de seguir. 

Además el código original usa múltiples declaraciones if para determinar qué operación realizar. Esto puede volverse lioso y difícil de mantener a medida que agregamos más operaciones. En el código refactorizado, utilizamos un diccionario para mapear las cadenas de operación a sus respectivas funciones.
