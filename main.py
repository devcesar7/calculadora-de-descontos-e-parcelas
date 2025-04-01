print("*****************************************")
print("** Calculadora de Descontos e Parcelas **")
print("*****************************************")

# Solicita um valor válido para o produto
valor_do_produto = float(input("Digite o valor do produto (R$): "))
while valor_do_produto <= 0:
    print("Erro!! O valor do produto deve ser maior que zero.")
    valor_do_produto = float(input("Digite o valor do produto (R$): "))

# Solicita um valor válido para o desconto
valor_do_desconto = int(input("Digite o percentual do desconto (%): "))
while valor_do_desconto < 0 or valor_do_desconto > 100:
    print("Erro!! O desconto deve estar entre 0% e 100%.")
    valor_do_desconto = int(input("Digite o percentual do desconto (%): "))

# Solicita um valor válido para as parcelas
parcelas = int(input("Digite quantas parcelas você quer pagar (X): "))
while parcelas < 1:
    print("Erro!! O número de parcelas deve ser pelo menos 1.")
    parcelas = int(input("Digite quantas parcelas você quer pagar (X): "))

# Calcula o valor com desconto
valor_com_desconto = valor_do_produto - (valor_do_produto * (valor_do_desconto / 100))

# Pergunta se há juros simples
tem_juros = input("Tem juros simples? (True/False): ").strip().lower()

if tem_juros == "true":
    taxa_juros = float(input("Digite a taxa de juros por parcela (%): "))
    while taxa_juros < 0:
        print("Erro!! A taxa de juros deve ser um valor positivo.")
        taxa_juros = float(input("Digite a taxa de juros por parcela (%): "))

    # Convertendo a taxa de juros para decimal
    taxa_juros = taxa_juros / 100

    # Calculando o juros simples
    juros_total = valor_com_desconto * taxa_juros * parcelas
    valor_final = valor_com_desconto + juros_total
else:
    valor_final = valor_com_desconto

# Calculando o valor de cada parcela
valor_de_cada_parcela = valor_final / parcelas

# Exibindo os resultados
print("\n=============== RESULTADO ===============")
print(f"O valor com desconto é: R${valor_com_desconto:.2f}")
if tem_juros == "true":
    print(f"Total com juros: R${valor_final:.2f}")
print(f"O valor de cada parcela ({parcelas}x) será: R${valor_de_cada_parcela:.2f}")
print("=========================================")
