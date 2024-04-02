# cadastro de produtos

print("\t"*5 + "-"*100)
print("\t"*10 +" CADASTRO DE PRODUTOS \n")
# código do produto
codprod = input("\t"*7 +"Digite o código do produto: ")
# nome do produto
nomep = input("\t"*7 +"Nome do produto: ")
# descrição do produto
descp = input("\t"*7 +"Digite uma breve descrição do produto: ")
# custo produto
custop = float(input("\t"*7 +"Custo do produto: "))
# custo fixo do produto
custofixop = float(input("\t"*7 +"Custo fixo do produto (%): "))

# comissão vendas
cv = float(input("\t"*7 +"Comissão de venda (%): "))

imposto = float(input("\t"*7 +"Imposto sobre a venda (%): "))
# rentabilidade
rentab = float(input("\t"*7 +"Rentabilidade (%): "))

#formula para calcular o preco de venda
pv = custop/(1 -((custofixop + cv + imposto + rentab)/100))

# calcular porcentagem e valores da tabela
porcentCustop = (custop/pv)*100
receitaBruta = pv - custop
porcentReceitaBruta = (receitaBruta/pv)*100
porcentOutroCusto = custofixop + cv +imposto
valor_custoFixo = (custofixop*pv)/100
valor_cv = (cv*pv)/100
valor_imposto = (imposto*pv)/100
valor_outroCusto = valor_custoFixo + valor_cv + valor_imposto
valor_rentab = receitaBruta - valor_outroCusto
porcentRentab = (valor_rentab/pv)*100


# tabela com o print
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'Descrição':^30}"+ f"|{'Valor':^8}" + f"|{'%':^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'A. Preço de venda':<30}"+ f"|{round(pv,2):^8}"+ f"|{'100':^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'B. Custo de aquisição':<30}"+ f"|{custop:^8}"+ f"|{porcentCustop:^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'C. Receira Bruta':<30}"+ f"|{receitaBruta:^8}"+ f"|{porcentReceitaBruta:^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'D. Custo Fixo/Administrativo':<30}"+ f"|{valor_custoFixo:^8}"+ f"|{custofixop:^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'E. Comissão de Vendas':<30}"+ f"|{valor_cv:^8}"+ f"|{cv:^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'F. Impostos':<30}"+ f"|{valor_imposto:^8}"+ f"|{imposto:^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'G. Outros Custos':<30}"+ f"|{valor_outroCusto:^8}"+ f"|{porcentOutroCusto:^4}|")
print("\t"*7+ "-"*46)
print("\t"*7 + f"|{'H. Rentabilidade':<30}"+ f"|{valor_rentab:^8}"+ f"|{rentab:^4}|")
print("\t"*7+ "-"*46)

# avaliar lucro
if(rentab > 20):
    print("\t"*12 + "Lucro Alto")
elif(rentab>10 and porcentRentab<=20):
    print("\t"*12 + "Lucro Médio")
elif(rentab>0 and porcentRentab<=10):
    print("\t"*12 + "Lucro Baixo")
elif(rentab == 0):
    print("\t"*12 + "Equilíbrio")
elif(rentab <0):
    print("\t"*12 + "Prejuízo")
