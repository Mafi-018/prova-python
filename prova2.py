# Joao Pedro Mafi   O FILME

valor1 = float(input("Digite o valor do ingresso atual: "))
valor2 = float(input("Digite o valor do ingresso antigo: "))

# aqui eu calculei a porcentagem do meu valor2 então fiz ele valor1 e multipliquei por valor2 depois peguei o resultado e dividi por 100
porcentagem = ((valor1 - valor2) / valor2) * 100

print("A variação percentual entre o ingresso antigo e o atual é de {:.2f}%.".format(porcentagem))