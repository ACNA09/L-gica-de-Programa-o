"""
5. Construa o programa que calcule o peso ideal de uma pessoa.
 Utilize as seguintes fórmulas:
- Se homem, o peso ideal é calculado assim: (72,7 x altura) - 58;
- Se mulher, o peso ideal é calculado assim: (62,1 x altura) - 44,7.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar)"""

mulher = 1
homem = 2
altura = float(input("Digite a sua altura: "))
escolha_do_genero = int(input("Digite 1 para mulher ou 2 para homem: "))
peso_ideal_mulher = (62.1 * altura) - 44.7
peso_ideal_homem = (72.7 * altura) - 58
if escolha_do_genero == mulher:
    print(f"O seu peso ideal é: {peso_ideal_mulher:.2f}")
else:
    print(f"O seu peso ideal é: {peso_ideal_homem:.2f}")





