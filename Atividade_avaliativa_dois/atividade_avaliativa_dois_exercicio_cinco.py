"""5- Dado o comprimento das três retas a, b e c. Verifique se eles podem ser o comprimento dos lados
de um triângulo. Se forem, verifique se compõem um triângulo equilátero, isósceles ou escaleno.
Informe se não compuserem nenhum triângulo. Relembre as seguintes definições:
- No plano, triângulo (também aceito como trilátero) é a figura geométrica que ocupa o espaço
interno limitado por três linhas retas que concorrem, duas a duas, em três pontos diferentes
formando três lados e três ângulos internos. Para ser triângulo, qualquer lado tem medida menor que
a soma das medidas dos outros dois lados.
- Triângulo equilátero: possui três lados iguais;
- Triângulo isósceles: possui dois lados iguais;
- Triângulo escaleno: tem todos os lados diferentes.
Obs.: verifique primeiro se os lados formam um triângulo"""
reta_a = float(input("Digite o valor da reta a: "))
reta_b = float(input("Digite o valor da reta b: "))
reta_c = float(input("Digite o valor da reta c: "))


if reta_a < (reta_c + reta_b) and reta_b < (reta_a + reta_c) and reta_c < (reta_a + reta_b):
    print("A junção dessas retas forma um triângulo.")
    if reta_a == reta_b == reta_c:
        print(" É um triângulo equilátero.")
    elif  reta_a == reta_b or reta_a == reta_c or reta_b == reta_c:
        print("É um triângulo isóceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Essas retas não formam um triângulo.")





