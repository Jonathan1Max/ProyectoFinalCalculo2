# README: Calculadora de Integrales Impropias y Regla de L'Hopital

## Introducción
Esta aplicación permite calcular integrales impropias y aplicar la Regla de L'Hopital usando la biblioteca **SymPy** de Python. La interfaz es sencilla y permite al usuario interactuar a través de la terminal.

## Requisitos
- Python 3.x
- SymPy (instalar con `pip install sympy`)

## Cómo Ejecutar el Programa en la terminal de Windows 
1. **Clona o descarga el repositorio** en tu máquina local.
2. **Navega a la carpeta del proyecto** en la terminal de Windows (cmd) usando el comando `cd`. Por ejemplo:
   ```bash
   cd C:\ruta\al\directorio\del\proyecto
   python nombre_del_archivo.py

## Interfaz del usuario
Al ejecutar el programa, verás un menú en la terminal con las siguientes opciones:

¡Bienvenido al calculador de Integrales Impropias y Regla de L'Hopital!
Selecciona una opción:
1. Calcular Integral Impropia
2. Calcular Límite usando Regla de L'Hopital
3. Salir

## EJEMPLO OPCION 1
Selecciona la opción: 1
Ingresa la función: x**2 + 2*x + 1
Ingresa el límite inferior: 0
Ingresa el límite superior: oo

Ingresa la función: 1/x
Ingresa el límite inferior: 1
Ingresa el límite superior: oo

## EJEMPLO OPCION 2
Selecciona la opción: 2
Ingresa el numerador: x**2
Ingresa el denominador: x - 1
Ingresa el punto donde calcular el límite: 1

Ingresa el numerador: sin(x)
Ingresa el denominador: x
Ingresa el punto donde calcular el límite: 0

## Notas adicionales
Asegúrate de ingresar las funciones en el formato correcto usando la sintaxis de Python para operaciones matemáticas.
Para funciones complejas, consulta la documentación de SymPy para obtener detalles sobre cómo ingresar expresiones más complicadas.
