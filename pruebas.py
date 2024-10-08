from sympy import symbols, diff, solve

# Definir la variable simbólica
x = symbols('x')

# Definir los valores de a, b, c
a = 9
b = 3
c = 5

# Definir la función f(x)
f = (x - a) * (x - b) * (x - c)

# Calcular los puntos críticos
Val_criticos = [i.n(4) for i in solve(diff(f, x))]

# Calcular los valores de f en los puntos críticos
maximo_relativo = f.subs(x, Val_criticos[0])
minimo_relativo = f.subs(x, Val_criticos[1])

# Imprimir los resultados
print(f"Coordenada x del máximo relativo: {Val_criticos[0]}")
print(f"Máximo relativo de f: {maximo_relativo}")
print(f"Coordenada x del mínimo relativo: {Val_criticos[1]}")
print(f"Mínimo relativo de f: {minimo_relativo}")
