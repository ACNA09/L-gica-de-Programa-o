"""
3. Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano
cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles. """
x_um = float(input("Digite o x1: "))
y_um = float(input("Digite o y1: "))
p = (x_um,y_um)
print(p)
x_dois = float(input("Digite o x2: "))
y_dois = float(input("Digite o y2: "))
q = (x_dois,y_dois)
print(q)
primeiro_calculo = ((x_dois - x_um)**2)
segundo_calculo = ((y_dois - y_um)**2)
distancia_entre_dois_pontos_no_plano_cartesiano = (primeiro_calculo + segundo_calculo)**0.5
print(primeiro_calculo)
print(segundo_calculo)
print(f"A distância entre esses dois pontos é: {distancia_entre_dois_pontos_no_plano_cartesiano}")
