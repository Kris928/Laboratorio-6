# Laboratorio-6
Laboratorio 6 (Callbacks y Funciones Lambda en Python) 
1. Callbacks
## Descripción del Código
El siguiente código implementa una simulación de actualización de datos en tiempo real utilizando números aleatorios para representar la temperatura y la humedad. El objetivo principal es demostrar el uso de una clase `RealTimeDataManager` que utiliza un temporizador para notificar eventos periódicos de actualización de datos a través de un `EventManager`.

## Funcionalidad Destacada

### Simulación de Datos en Tiempo Real:

La clase `RealTimeDataManager` simula la actualización periódica de datos utilizando números aleatorios para la temperatura y la humedad.

### EventManager para Notificaciones:

Se utiliza un `EventManager` para gestionar la suscripción, cancelación y notificación de eventos. En este caso, notifica a los suscriptores cada vez que se actualizan los datos.

### Callback de Notificación:

Se proporciona un callback simple que imprime los datos actualizados en tiempo real al `stdout`.

## Uso del Código

Para ejecutar el código, se crea una instancia de `RealTimeDataManager`, se suscribe un callback al `EventManager`, y luego se inicia la actualización periódica de datos.

## Resultado 
![Resultado del ejercicio 1, aquí se ve donde se imprimen los valores de la temperatura y la humedad con pocos decimales correctamente](imagen/Ejercicio1.PNG)

2. Código de Calculadora con Callbacks y Lambda

## Descripción General:

El siguiente código implementa una calculadora interactiva en Python, permitiendo al usuario realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. La calculadora utiliza funciones de devolución de llamada (callbacks) y funciones lambda para ejecutar las operaciones seleccionadas por el usuario.

## Estructura del Código:

El código se divide en tres funciones principales: `get_user_input`, `ejecutar_operacion`, y `main`.

- **`get_user_input:`** Esta función solicita al usuario que ingrese dos números y la operación deseada. Maneja posibles errores, como la introducción de valores no numéricos, mediante un bloque try-except.

- **`ejecutar_operacion:`** Esta función toma la entrada del usuario y una función de devolución de llamada correspondiente a la operación seleccionada. Utiliza funciones lambda para representar cada operación matemática y ejecuta la operación con los dos números proporcionados. Se manejan excepciones, como la división por cero.

- **`main:`** La función principal del programa. Utiliza un bucle while para mantener la calculadora en funcionamiento hasta que el usuario decida salir. Dentro del bucle, obtiene la entrada del usuario, realiza la operación seleccionada utilizando la función `ejecutar_operacion`, y maneja casos de salida.
## Resultado
![Resultado del ejercicio 2, aquí se ve donde se solicita dos numeros y el operador para luego calcular su valor](imagen/Ejercicio2.PNG)

## Uso de Funciones Lambda:

En lugar de definir funciones separadas para cada operación matemática, se han utilizado funciones lambda en el diccionario `operations`. Cada función lambda toma dos argumentos (números a operar) y devuelve el resultado de la operación correspondiente. Esto simplifica el código y lo hace más conciso.

```python
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else None
}




