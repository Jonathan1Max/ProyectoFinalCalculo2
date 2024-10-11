import sympy as sp

from IntegralImpropia import IntegralImpropia
from lhopital import ReglaLhopital

class Calculadora:
    def __init__(self):
        self.variable = sp.symbols('x')  # Definimos la variable común para las operaciones

    @staticmethod
    def menu():
        print("¡Bienvenido al calculador de Integrales Impropias y Regla de L'Hopital!")
        print("Selecciona una opción:")
        print("1. Calcular Integral Impropia")
        print("2. Calcular Límite usando Regla de L'Hopital")
        print("3. Salir")
        
    def main(self):
        while True:
            self.menu()
            opcion = input("\nSelecciona una opción: ")

            if opcion == '1':
                funcion = input("Ingresa la función: ")
                limite_inferior = float(input("Ingresa el límite inferior: "))
                limite_superior = input("Ingresa el límite superior (escribe 'oo' para infinito): ")
                if limite_superior == 'oo':
                    limite_superior = sp.oo
                else:
                    limite_superior = float(limite_superior)

                integral = IntegralImpropia(funcion, limite_inferior, limite_superior)
                resultado = integral.calcular()
                print(f"El resultado de la integral impropia es: {resultado}")

            elif opcion == '2':
                numerador = input("Ingresa el numerador: ")
                denominador = input("Ingresa el denominador: ")
                punto = float(input("Ingresa el punto donde calcular el límite: "))

                lhopital = ReglaLhopital(numerador, denominador, punto)
                limite_original, limite_lhopital = lhopital.aplicar()  # Cambiar a aplicar()
                print(f"El límite original es: {limite_original}")
                print(f"El resultado de aplicar la Regla de L'Hopital es: {limite_lhopital}")

            elif opcion == '3':
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.main()