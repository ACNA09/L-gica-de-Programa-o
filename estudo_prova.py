"""
valor_1 = float(input("Digite um número:"))
valor_2 = float(input("Digite um número:"))
soma = valor_1 + valor_2
print(f"A soma dos valores digitados é igual a: {soma}")"""

"""
#2) Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Média")
nota_1 = float(input("Digite a nota do primeiro bimestre: "))
nota_2 = float(input("Digite a nota do segundo bimestre: "))
nota_3 = float(input("Digite a nota do terceiro bimestre: "))
nota_4 = float(input("Digite a nota do quarto bimestre: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f"A média das notas desse aluno é: {media}")"""

"""
#3) Faça um Programa que converta metros para centímetros.
print("Conversor de unidades de comprimento")
valor_metros = float(input("Digite o comprimento de alguma coisa, em metros: "))
convertendo_cm = valor_metros * 100
print(f"O valor em centímetros é: {convertendo_cm} cm.")"""

"""Projete o programa para calcular a área de um triângulo. O usuário 
informará os dados necessários para o cálculo, ou seja, a base e a 
altura do triângulo.

- Fórmula:     área = base . altura
                            2   
print("Cálculo para a área do triângulo")
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))
area_triangulo = (base * altura) / 2
print(f"A área do triângulo é: {area_triangulo}")"""

"""
#4) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print("ÁREA DO CÍRCULO")
raio = float(input("Digite o raio do círculo: "))
area_circulo = 3.14 * raio**2
print("A área do cículo é: ", area_circulo)"""

"""
#5) Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta
#área para o usuário.
print("ÁREA DO QUADRADO")
lado = float(input("Digite o valor do lado do quadrado: "))
area_quadrado = lado**2
print("A área do quadrado é: ", area_quadrado)
dobro_area_quadrado = area_quadrado**2
print("O dobro da área do quadrado é: ", dobro_area_quadrado)"""
"""
ct = 0
while True:
    senha = int(input("Digite a senha: "))
    if senha != 1234:
        print("Senha incorreta. Tente Novamente.")
    else:
        print("Acesso permitido.")
        break
    ct = ct + 1
print("Tentativas: ", ct) """

"""
idade = int(input("Digite a sua idade: "))
if idade == 12:
    print("Criança")
elif idade >= 12 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso") """
"""
soma = 0
print("Digite [0] para sair.")
while True:
    numero = float(input("Digite um número: "))
    if numero == 0:
        break
    soma = soma + numero
print("A soma dos números digitados é: ", soma)
"""
"""
ct = 0
print("Digite um número negativo para sair.")
while True:
    numero = float(input("Digite um número: "))
    if numero < 0:
        break
    ct = ct + 1
print("A quantidade de números digitados é: ", ct)
"""

while True:
    senha = str(input("Digite a senha: "))
    if senha == "python123":
        print("Acesso liberado.")
        break
    else:
        print("Senha incorreta.")







