"""
2- Elabore o programa que selecione o maior valor de três valores fornecidos pelo usuário. Resolva
sem usar operador lógico (e, ou, não).
"""
valor_1 = float(input("Digite o primeiro número: "))
valor_2 = float(input("Digite o segundo número: "))
valor_3 = float(input("Digite o terceiro número: "))

if   valor_1 > valor_2:
   print("O primeiro valor digitado é o maior.")
elif valor_1 > valor_3:
   print("O primeiro valor digitado é o maior.")
elif valor_2 > valor_1:
   print("O segundo valor digitado é o maior.")
elif valor_2 > valor_3:
   print("O segundo valor digitado é o maior.")
elif valor_3 > valor_1:
   print("O terceiro valor digitado é o maior.")
elif valor_3 > valor_2:
   print("O terceiro valor digitado é o maior.")
else:
   print("Os valores são iguais.")