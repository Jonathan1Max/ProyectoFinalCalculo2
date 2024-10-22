import sympy as sp

# Definir variables globales
x = sp.Symbol('x')

# Semana 1: Función para calcular una integral impropia
def calcular_integral_impropia(funcion, limite_inferior, limite_superior):
    """
    Calcula la integral impropia de una función dada con límites.
    limite_inferior: límite inferior de la integral
    limite_superior: límite superior de la integral (puede ser infinito)
    """
    integral = sp.integrate(funcion, (x, limite_inferior, limite_superior))
    return integral

# Semana 1: AVANCE
def ejemplo_integral_impropia():
    """
    Ejemplo: Calcular la integral impropia de 1/x^2 desde 1 hasta infinito.
    """
    funcion = 1 / x**2
    limite_inferior = 1
    limite_superior = sp.oo  # Infinito
    resultado = calcular_integral_impropia(funcion, limite_inferior, limite_superior)
    print(f"Resultado de la integral impropia ∫1/𝑥² dx de 1 a ∞: {resultado}")

# Semana 2: AVANCE funcion para aplicar la Regla de L'Hopital
def regla_lhopital(funcion_numerador, funcion_denominador, valor_limite):
    """
    Aplica la Regla de L'Hopital a una función con numerador y denominador.
    valor_limite: valor hacia el que tiende x (puede ser infinito o un número).
    """
    limite_original = sp.limit(funcion_numerador / funcion_denominador, x, valor_limite)
    derivada_numerador = sp.diff(funcion_numerador, x)
    derivada_denominador = sp.diff(funcion_denominador, x)
    limite_lhopital = sp.limit(derivada_numerador / derivada_denominador, x, valor_limite)
    return limite_original, limite_lhopital

# Semana 3: AVANCE DE ex de Regla de L'Hopital
def ejemplo_lhopital():
    """
    Ejemplo: Resolver el límite de e^x / x^2 cuando x tiende a infinito usando la Regla de L'Hopital.
    """
    funcion_numerador = sp.exp(x)
    funcion_denominador = x**2
    valor_limite = sp.oo  # Infinito
    limite_original, limite_lhopital = regla_lhopital(funcion_numerador, funcion_denominador, valor_limite)
    print(f"Límite original de e^x / x^2 cuando x→∞: {limite_original}")
    print(f"Límite después de aplicar la Regla de L'Hopital: {limite_lhopital}")

# Semana 3: AVANCE FUNCION avanzada para trabajar con más integrales impropias
def calcular_integrales_varias(funciones, limites):
    """
    Calcula múltiples integrales impropias para un conjunto de funciones y límites.
    funciones: lista de funciones a integrar
    limites: lista de límites [limite_inferior, limite_superior] para cada función
    """
    resultados = []
    for i, funcion in enumerate(funciones):
        limite_inferior, limite_superior = limites[i]
        resultado = calcular_integral_impropia(funcion, limite_inferior, limite_superior)
        resultados.append(resultado)
    return resultados

# Semana 3: Avance Ejemplo con varias integrales
def ejemplo_varias_integrales():
    """
    Ejemplo: Calcular varias integrales impropias con diferentes funciones y límites.
    """
    funciones = [1 / x**2, sp.exp(-x)]
    limites = [(1, sp.oo), (0, sp.oo)]
    resultados = calcular_integrales_varias(funciones, limites)
    for i, resultado in enumerate(resultados):
        print(f"Resultado de la integral {i+1}: {resultado}")

# Semana 4: AVANCE funcion avanzada de Regla de L'Hopital con varias formas indeterminadas
def calcular_limites_varios(numeradores, denominadores, valor_limite):
    """
    Aplica la Regla de L'Hopital a varias funciones con diferentes numeradores y denominadores.
    numeradores: lista de funciones del numerador
    denominadores: lista de funciones del denominador
    valor_limite: valor hacia el que tiende x
    """
    resultados = []
    for i in range(len(numeradores)):
        limite_original, limite_lhopital = regla_lhopital(numeradores[i], denominadores[i], valor_limite)
        resultados.append((limite_original, limite_lhopital))
    return resultados

# Semana 4: Ejemplo avanzado de varios límites usando L'Hopital
def ejemplo_varios_lhopital():
    """
    Ejemplo: Resolver varios límites usando la Regla de L'Hopital con diferentes funciones.
    """
    numeradores = [sp.exp(x), x**3]
    denominadores = [x**2, sp.sin(x)]
    valor_limite = sp.oo  # Infinito para el primer, límite 0 para el segundo
    resultados = calcular_limites_varios(numeradores, denominadores, valor_limite)
    for i, (limite_original, limite_lhopital) in enumerate(resultados):
        print(f"Límite original {i+1}: {limite_original}")
        print(f"Límite L'Hopital {i+1}: {limite_lhopital}")

# Ejecución del proyecto completo
if __name__ == "__main__":
    print("Semana 1: Ejemplo de Integral Impropia")
    ejemplo_integral_impropia()
    
    print("\nSemana 2: Ejemplo de Regla de L'Hopital")
    ejemplo_lhopital()
    
    print("\nSemana 3: Ejemplo con Varias Integrales Impropias")
    ejemplo_varias_integrales()
    
    print("\nSemana 4: Ejemplo con Varios Límites usando Regla de L'Hopital")
    ejemplo_varios_lhopital()
