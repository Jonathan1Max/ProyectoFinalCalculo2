import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class IntegralImpropia:
    def __init__(self, funcion, limite_inferior, limite_superior):
        self.funcion = sp.sympify(funcion)
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.variable = sp.symbols('x')

    def calcular(self):
            # Calcula la integral impropia
            integral = sp.integrate(self.funcion, (self.variable, self.limite_inferior, self.limite_superior))
            return integral
            
    def graficar(self):
        # Asignar valores finitos para graficar si los límites son infinitos
        lim_inf_grafica = -10 if self.limite_inferior == '-oo' else float(self.limite_inferior) - 1
        lim_sup_grafica = 10 if self.limite_superior == 'oo' else float(self.limite_superior) + 1

        x_vals = np.linspace(lim_inf_grafica, lim_sup_grafica, 1000)
        y_vals = []

        for val in x_vals:
            try:
                y = float(self.funcion.evalf(subs={self.variable: val}))
                y_vals.append(y if np.isfinite(y) else np.nan)
            except (ZeroDivisionError, ValueError):
                y_vals.append(np.nan)

        plt.figure(figsize=(16, 12))
        plt.plot(x_vals, y_vals, label=f"f(x)={self.funcion}", color='blue')
        plt.axvline(x=lim_inf_grafica, color='green', linestyle='--', label='Límite Inferior')
        plt.axvline(x=lim_sup_grafica, color='red', linestyle='--', label='Límite Superior')

        plt.title('Gráfica de la Integral Impropia')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim(-10, 10)
        plt.xlim(lim_inf_grafica, lim_sup_grafica)
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.legend()

        graph_path = "static/integral_graph.png"
        plt.savefig(graph_path)
        plt.close()
        return graph_path