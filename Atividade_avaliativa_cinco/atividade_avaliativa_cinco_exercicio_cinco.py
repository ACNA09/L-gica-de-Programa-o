"""5. Elabore o programa que imprima a tabuada de multiplicação do número
cinco de um até dez. Gere o seguinte layout:                           1  x  5  =    5
                             	.  .  .
10	x  5  =  50
"""

num = 5
for numero in range(1,11,1):
    print(f"{num} * {numero} = { num * numero}" )