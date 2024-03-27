# cadastro de produtos

print("**************************************************")
print("Cadastro do produto \n")
# código do produto
codprod = input("Digite o código do produto: ")
# nome do produto
nomep = input("Nome do produto: ")
# descrição do produto
descp = input("Digite uma breve descrição do produto:")
# custo produto
custop = float(input("Custo do produto: "))
# custo fixo do produto
custofixop = float(input("Custo fixo do produto (%): "))

# comissão vendas
cv = float(input("Comissão de venda (%): "))

imposto = float(input("Imposto sobre a venda (%): "))
# rentabilidade
rentab = float(input("Rentabilidade (%): "))

pv = custop/(1 -((custofixop + cv + imposto + rentab)/100))
print(pv)