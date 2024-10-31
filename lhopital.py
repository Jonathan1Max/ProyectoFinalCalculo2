import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class ReglaLhopital:
    def __init__(self, funcion_num, funcion_den, punto):
        self.funcion_num = sp.sympify(funcion_num)
        self.funcion_den = sp.sympify(funcion_den)
        self.punto = sp.sympify(punto)
        self.variable = sp.symbols('x')

    def aplicar(self):
        limite_original = sp.limit(self.funcion_num / self.funcion_den, self.variable, self.punto)
        derivada_num = sp.diff(self.funcion_num, self.variable)
        derivada_den = sp.diff(self.funcion_den, self.variable)
        limite_lhopital = sp.limit(derivada_num / derivada_den, self.variable, self.punto)
        return limite_original, limite_lhopital

    def graficar(self):
        x = self.variable
        numerador = self.funcion_num
        denominador = self.funcion_den

        # Valores de x alrededor del punto de interés para graficar
        x_vals = np.linspace(float(self.punto) - 2, float(self.punto) + 2, 1000)
        y_vals = [
            numerador.evalf(subs={x: val}) / denominador.evalf(subs={x: val})
            if denominador.evalf(subs={x: val}) != 0 else np.nan
            for val in x_vals
        ]

        plt.figure(figsize=(12, 8))
        plt.plot(x_vals, y_vals, label=f"f(x)={numerador}/{denominador}", color='blue')

        # Calcular el límite en el punto de interés y marcarlo en la gráfica
        try:
            interseccion_y = sp.limit(numerador / denominador, x, self.punto)
            plt.scatter([float(self.punto)], [float(interseccion_y)], color='red', zorder=5)
            plt.text(float(self.punto), float(interseccion_y), f"({float(self.punto):.2f}, {float(interseccion_y):.2f})",
                     color="red", fontsize=12, ha='right')
        except (ZeroDivisionError, ValueError):
            pass  # Manejar casos en los que no se pueda calcular el límite

        plt.axvline(x=float(self.punto), color='green', linestyle='--', label=f'x = {float(self.punto)}')
        plt.title("Gráfica del Límite usando Regla de L'Hôpital")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.xlim(float(self.punto) - 2, float(self.punto) + 2)
        plt.grid()
        plt.legend()

        graph_path = "static/lhopital_graph.png"
        plt.savefig(graph_path)
        plt.close()
        return graph_path