import oracledb

connection = oracledb.connect(
    user = "seu user",
    password = 'sua senha',
    dsn = "172.16.12.14/xe"  
)

cursor = connection.cursor()

opcao = 1 # int(input("Digite 1 (Cadastrar produto) ou 2 (Listar produto): "))

#FUNÇÃO QUE FAZ OS CALCULOS
def calcular_valores(custo_prod, custo_fixo, comissao, imposto, rentabilidade):
    pv = custo_prod / (1 - ((custo_fixo + comissao + imposto + rentabilidade) / 100))
    porcentcusto_prod = (custo_prod / pv) * 100
    receitaBruta = pv - custo_prod
    porcentReceitaBruta = (receitaBruta / pv) * 100
    porcentOutroCusto = custo_fixo + comissao + imposto
    valor_custoFixo = (custo_fixo * pv) / 100
    valor_comissao = (comissao * pv) / 100
    valor_imposto = (imposto * pv) / 100
    valor_outroCusto = valor_custoFixo + valor_comissao + valor_imposto
    valor_rentabilidade = receitaBruta - valor_outroCusto
    porcentRentab = (valor_rentabilidade / pv) * 100
    return pv, receitaBruta, porcentcusto_prod, porcentReceitaBruta, porcentOutroCusto, valor_custoFixo, valor_comissao, valor_imposto, valor_outroCusto, valor_rentabilidade, porcentRentab

if opcao == 1:

    print("Listagem")

    connection.commit()
    cursor.execute("SELECT * FROM Estoque")

    for row in cursor: 
        #Para imprimir dados tal como foram inseridos no SQL:

        id_prod = row[0] 
        nome_prod = row[1]
        desc_prod = row[2]
        custo_prod = row[3] 
        custo_fixo = row[4]
        comissao = row[5]
        imposto = row[6] 
        rentabilidade = row[7]
         
        # # Chamando a função para calcular os valores
        pv, receitaBruta, porcentcusto_prod, porcentReceitaBruta, porcentOutroCusto, valor_custoFixo, valor_comissao, valor_imposto, valor_outroCusto, valor_rentabilidade, porcentRentab = calcular_valores(
            custo_prod, custo_fixo, comissao, imposto, rentabilidade)
         
        
        print("\t"*7 + f"{id_prod}:\t {nome_prod}\t {desc_prod}")
        print("\t"*7 +"Descrição"+"\t"*4+"Valor"+"\t"*3+"%")
        print("\t"*7 +f"A. Preço de venda"+"\t"*3+f"R$ {pv:.2f}"+"\t"*3+"100%")
        print("\t"*7 +f"B. Custo de Aquisição (Fornecedor)\tR$ {custo_prod:.2f}"+"\t"*2+f"{round(porcentcusto_prod):.2f}%")
        print("\t"*7 +f"C. Receita Bruta (A-B)"+"\t"*3+f"R$ {receitaBruta:.2f}"+"\t"*2+f"{round(porcentReceitaBruta):.2f}%")
        print("\t"*7 +f"D.Custo Fixo/Administrativo"+"\t"*2+f"R$ {valor_custoFixo:.2f}"+"\t"*2+f"{round(valor_custoFixo/pv*100):.2f}%")
        print("\t"*7 +f"E.Comissão de Vendas"+"\t"*3+f"R$ {valor_comissao:.2f}"+"\t"*3+f"{round(valor_comissao/pv*100):.2f}%")
        print("\t"*7 +f"F.Impostos"+"\t"*4+f"R$ {valor_imposto:.2f}"+"\t"*3+f"{round(valor_imposto/pv*100):.2f}%")
        print("\t"*7 +f"G. Outros Custos (D+E+F)"+"\t"*2+f"R$ {valor_outroCusto:.2f}"+"\t"*3+f"{round(valor_outroCusto/pv*100):.2f}%")
        print("\t"*7 +f"H. Rentabilidade"+"\t"*3+f"R$ {valor_rentabilidade:.2f}"+"\t"*3+f"{round(valor_rentabilidade/pv*100):.2f}%")
        

        if rentabilidade > 20:
            print("Lucro\tLucro alto")
        elif rentabilidade > 10:
            print("Lucro\tLucro médio")
        elif rentabilidade > 0:
            print("Lucro\tLucro baixo")
        elif rentabilidade == 0:
            print("Lucro\tEquilíbrio")
        else:
            print("Lucro\tPrejuízo")
        print("\n")

    cursor.close()
    connection.close()