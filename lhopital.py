import sympy as sp

class ReglaLhopital:
    def __init__(self, funcion_num, funcion_den, punto):
        self.funcion_num = sp.sympify(funcion_num)
        self.funcion_den = sp.sympify(funcion_den)
        self.punto = sp.sympify(punto)
        self.variable = sp.symbols('x')  # Definimos la variable

    def aplicar(self):
        # Calcula el límite original y el límite usando la Regla de L'Hopital
        limite_original = sp.limit(self.funcion_num / self.funcion_den, self.variable, self.punto)
        derivada_num = sp.diff(self.funcion_num, self.variable)
        derivada_den = sp.diff(self.funcion_den, self.variable)
        limite_lhopital = sp.limit(derivada_num / derivada_den, self.variable, self.punto)
        return limite_original, limite_lhopital