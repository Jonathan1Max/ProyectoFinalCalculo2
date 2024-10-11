import sympy as sp

class IntegralImpropia:
    def __init__(self, funcion, limite_inferior, limite_superior):
        self.funcion = sp.sympify(funcion)
        self.limite_inferior = sp.sympify(limite_inferior)
        self.limite_superior = sp.sympify(limite_superior)
        self.variable = sp.symbols('x')  # Definimos la variable de integración

    def calcular(self):
        # Calcula la integral impropia
        integral = sp.integrate(self.funcion, (self.variable, self.limite_inferior, self.limite_superior))
        return integral