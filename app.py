from flask import Flask, render_template, request, flash

from IntegralImpropia import IntegralImpropia
from lhopital import ReglaLhopital

app = Flask(__name__)
app.secret_key = 'max_wild'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_integral', methods=['POST'])
def calcular_integral():
    funcion = request.form['funcion']
    limite_inferior = request.form['limite_inferior']
    limite_superior = request.form['limite_superior']

    try:
        integral = IntegralImpropia(funcion, limite_inferior, limite_superior)
        resultado = integral.calcular()
        graph_url = integral.graficar()
        return render_template('index.html', resultado_integral=resultado, graph_url=graph_url)
    except Exception as e:
        flash(f"Error al calcular la integral: {str(e)}")
        return render_template('index.html')

@app.route('/calcular_lhopital', methods=['POST'])
def calcular_lhopital():
    numerador = request.form['numerador']
    denominador = request.form['denominador']
    punto = request.form['punto']

    try:
        lhopital = ReglaLhopital(numerador, denominador, punto)
        resultado_original, resultado_lhopital = lhopital.aplicar()
        graph_url = lhopital.graficar()
        return render_template('index.html', resultado_lhopital=(resultado_original, resultado_lhopital), graph_url=graph_url)
    except Exception as e:
        flash(f"Error al calcular el límite: {str(e)}")
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)