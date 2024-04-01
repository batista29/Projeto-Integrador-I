# cadastro de produtos

print("\t"*5 + "-"*100)
print("\t"*10 +" CADASTRO DE PRODUTOS \n")
# código do produto
codprod = input("\t"*7 +"Digite o código do produto: ")
# nome do produto
nomep = input("\t"*7 +"Nome do produto: ")
# descrição do produto
descp = input("\t"*7 +"Digite uma breve descrição do produto:")
# custo produto
custop = float(input("\t"*7 +"Custo do produto: "))
# custo fixo do produto
custofixop = float(input("\t"*7 +"Custo fixo do produto (%): "))

# comissão vendas
cv = float(input("\t"*7 +"Comissão de venda (%): "))

imposto = float(input("\t"*7 +"Imposto sobre a venda (%): "))
# rentabilidade
rentab = float(input("\t"*7 +"Rentabilidade (%): "))

pv = custop/(1 -((custofixop + cv + imposto + rentab)/100))
pv = round(pv,2)
print("\t"*11 + "-"*9)
print("\t"*11 + f"|R$ {pv}|")
print("\t"*11 + "-"*9)

pv = custop/(1 -((custofixop + cv + imposto + rentab)/100))
print(pv)
