# README: Calculadora de Integrales Impropias y Regla de L'Hopital

## Introducción
Esta aplicación permite calcular integrales impropias y límites utilizando la Regla de L'Hôpital con Python, mostrando tanto el valor como una gráfica de la función. La aplicación emplea las bibliotecas SymPy para cálculo simbólico y Matplotlib para graficar resultados.

## Requisitos
- Python 3.x
- SymPy (instalar con `pip install sympy`)
- NumPy (instalar con pip install numpy)
- Matplotlib (instalar con pip install matplotlib)


## Cómo Ejecutar el Programa en la terminal de Windows 
1. **Clona o descarga el repositorio** en tu máquina local.
2. **Navega a la carpeta del proyecto** en la terminal de Windows (cmd) usando el comando `cd`. Por ejemplo:
   ```bash
   cd C:\ruta\al\directorio\del\proyecto
   python nombre_del_archivo.py

## Funcionamiento Web
Al ejecutar el programa, se inicia un servidor web que se puede acceder a través de un navegador. La aplicación proporciona dos secciones principales:

# Calcular Integral Impropia
Ingresa la función que deseas integrar, junto con los límites inferior y superior.
Por ejemplo, para la función 1/x, ingresa el límite inferior como 1 y el límite superior como oo para infinito.

# Calcular Límite usando Regla de L'Hôpital
Ingresa el numerador y el denominador de la función, así como el punto donde deseas calcular el límite.
Por ejemplo, para calcular el límite de (x**2)/(x - 1) cuando x se aproxima a 1, ingresa x**2 como numerador y x - 1 como denominador, con 1 como el punto.

## Notas adicionales
- Asegúrate de ingresar las funciones en el formato correcto utilizando la sintaxis de Python para operaciones matemáticas.
- Para funciones complejas, consulta la documentación de SymPy para obtener detalles sobre cómo ingresar expresiones más complicadas.
- Los límites en las integrales impropias pueden ser ingresados como oo para infinito.

## Contribuciones
Si deseas contribuir al proyecto, por favor crea un fork del repositorio y envía un pull request con tus mejoras. Se agradecerá bastante.