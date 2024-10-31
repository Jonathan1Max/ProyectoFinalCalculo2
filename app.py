from flask import Flask, render_template, request
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

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

    def graficar(self):
        x = sp.symbols('x')
        funcion = self.funcion

        # Establecer un rango más amplio y aumentar el número de puntos
        x_vals = np.linspace(float(self.limite_inferior) - 1, float(self.limite_superior) + 1, 1000)
        y_vals = [funcion.evalf(subs={x: val}) for val in x_vals]

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f"f(x)={funcion}", color='blue')

        # Resaltar el límite superior e inferior
        plt.axvline(x=float(self.limite_inferior), color='green', linestyle='--', label='Límite Inferior')
        plt.axvline(x=float(self.limite_superior), color='red', linestyle='--', label='Límite Superior')

        plt.title('Gráfica de la Integral Impropia')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.ylim(-10, 10)  # Ajusta según el rango esperado de la función
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.legend()

        # Guardar la gráfica
        graph_path = "static/integral_graph.png"
        plt.savefig(graph_path)
        plt.close()  # Cerrar la figura para evitar problemas
        return graph_path


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

    def graficar(self):
        x = sp.symbols('x')
        numerador = self.funcion_num
        denominador = self.funcion_den

        # Establecer un rango para la gráfica
        x_vals = np.linspace(float(self.punto) - 1, float(self.punto) + 1, 1000)
        y_vals = [numerador.evalf(subs={x: val}) / denominador.evalf(subs={x: val}) for val in x_vals]

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f"f(x)={numerador}/{denominador}", color='blue')

        # Resaltar el punto de interés
        plt.scatter([float(self.punto)], [numerador.subs(x, float(self.punto)) / denominador.subs(x, float(self.punto))], color='red', zorder=5)
        plt.axvline(x=float(self.punto), color='green', linestyle='--', label='Punto de Interés')

        plt.title("Gráfica de Límite usando Regla de L'Hôpital")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.legend()

        # Guardar la gráfica
        graph_path = "static/lhopital_graph.png"
        plt.savefig(graph_path)
        plt.close()  # Cerrar la figura para evitar problemas
        return graph_path


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_integral', methods=['POST'])
def calcular_integral():
    funcion = request.form['funcion']
    limite_inferior = request.form['limite_inferior']
    limite_superior = request.form['limite_superior']

    integral = IntegralImpropia(funcion, limite_inferior, limite_superior)
    resultado = integral.calcular()
    graph_url = integral.graficar()  # Graficar y obtener la URL

    return render_template('index.html', resultado_integral=resultado, graph_url=graph_url)


@app.route('/calcular_lhopital', methods=['POST'])
def calcular_lhopital():
    numerador = request.form['numerador']
    denominador = request.form['denominador']
    punto = request.form['punto']

    lhopital = ReglaLhopital(numerador, denominador, punto)
    resultado_original, resultado_lhopital = lhopital.aplicar()
    graph_url = lhopital.graficar()  # Graficar y obtener la URL

    return render_template('index.html', resultado_lhopital=(resultado_original, resultado_lhopital), graph_url=graph_url)


if __name__ == "__main__":
    app.run(debug=True)