print("*****************************************")
print("** Calculadora de Descontos e Parcelas **")
print("*****************************************")

valor_do_produto = float(input("Digite o valor do produto (R$): "))
valor_do_desconto = int(input("Digite o percentual do desconto (%): "))
parcelas = int(input("Digite quantas parcelas você quer pagar (X): "))

valor_com_desconto = valor_do_produto - (valor_do_produto * (valor_do_desconto/100))
print (f"O valor com desconto é {valor_com_desconto} R$")

valor_de_cada_parcela = valor_com_desconto / parcelas
print (f"O valor de cada parecela é {valor_de_cada_parcela} R$")