import os
import sympy as sp
from flask import Flask, render_template, request
from IntegralImpropia import IntegralImpropia
from lhopital import ReglaLhopital
import matplotlib
matplotlib.use('Agg')  # Usar backend sin GUI
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_integral', methods=['POST'])
def calcular_integral():
    funcion = request.form['funcion']
    limite_inferior = float(request.form['limite_inferior'])
    limite_superior = request.form['limite_superior']
    if limite_superior == 'oo':
        limite_superior = sp.oo
    else:
        limite_superior = float(limite_superior)

    integral = IntegralImpropia(funcion, limite_inferior, limite_superior)
    resultado = integral.calcular()

    # Graficar la función
    x = sp.symbols('x')
    expr = sp.sympify(funcion)
    x_vals = np.linspace(limite_inferior, limite_superior, 100)
    y_vals = [expr.subs(x, val) for val in x_vals]

    # Filtrar solo la parte real en caso de valores complejos
    y_vals = [sp.re(val) if val.is_real else sp.re(val.evalf()) for val in y_vals]
    y_vals = [float(y) for y in y_vals]  # Convertimos a float para Matplotlib

    plt.plot(x_vals, y_vals, label=f"f(x)={funcion}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfica de la función")
    plt.legend()

    # Guardar la gráfica de la integral
    graph_path = "static/graphs/integral_graph.png"
    plt.savefig(graph_path)
    plt.clf()  # Limpiar la gráfica para evitar conflictos en solicitudes futuras

    return render_template('index.html', resultado_integral=resultado, graph_url=graph_path)

@app.route('/calcular_lhopital', methods=['POST'])
def calcular_lhopital():
    numerador = request.form['numerador']
    denominador = request.form['denominador']
    punto = float(request.form['punto'])

    lhopital = ReglaLhopital(numerador, denominador, punto)
    limite_original, limite_lhopital = lhopital.aplicar()

    # Graficar el numerador y el denominador
    x = sp.symbols('x')
    num_expr = sp.sympify(numerador)
    den_expr = sp.sympify(denominador)

    # Crear un rango de valores x alrededor del punto de interés
    x_vals = np.linspace(punto - 1, punto + 1, 100)
    num_vals = [num_expr.subs(x, val) for val in x_vals]
    den_vals = [den_expr.subs(x, val) for val in x_vals]

    # Filtrar solo la parte real en caso de valores complejos
    num_vals = [sp.re(val) if val.is_real else sp.re(val.evalf()) for val in num_vals]
    den_vals = [sp.re(val) if val.is_real else sp.re(val.evalf()) for val in den_vals]
    num_vals = [float(y) for y in num_vals]  # Convertimos a float para Matplotlib
    den_vals = [float(y) for y in den_vals]  # Convertimos a float para Matplotlib

    # Graficar
    plt.plot(x_vals, num_vals, label=f"Numerador: {numerador}", color='blue')
    plt.plot(x_vals, den_vals, label=f"Denominador: {denominador}", color='red')
    plt.axvline(x=punto, color='green', linestyle='--', label=f"Límite en x={punto}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfica de L'Hôpital")
    plt.legend()

    # Guardar la gráfica de L'Hôpital
    lhopital_graph_path = "static/graphs/lhopital_graph.png"
    plt.savefig(lhopital_graph_path)
    plt.clf()  # Limpiar la gráfica para evitar conflictos en solicitudes futuras

    return render_template('index.html', resultado_lhopital=(limite_original, limite_lhopital), lhopital_graph_url=lhopital_graph_path)

if __name__ == '__main__':
    app.run(debug=True)