import oracledb

connection = oracledb.connect(
    user = "seu user", 
    password = 'sua senha', 
    dsn = "172.16.12.14:1521/XE"  
)

cursor = connection.cursor()

option = int(input("Digite 1 (Cadastrar produto) ou 2 (Listar produto): "))

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


if option == 1:
    # Casos: 
    #def case1():
    print("Cadastro")

    # cadastro de produtos
    print("\t"*5 + "-"*100)
    print("\t"*10 +" CADASTRO DE PRODUTOS \n")
    # código do produto
    id_prod = input("\t"*7 +"Digite o código do produto: ")
    # nome do produto
    nome_prod = input("\t"*7 +"Nome do produto: ")
    # descrição do produto
    desc_prod = input("\t"*7 +"Digite uma breve descrição do produto: ")
    # custo produto
    custo_prod = float(input("\t"*7 +"Custo do produto: "))
    # custo fixo do produto
    custo_fixo = float(input("\t"*7 +"Custo fixo do produto (%): "))

    # comissão vendas
    comissao = float(input("\t"*7 +"Comissão de venda (%): "))

    imposto = float(input("\t"*7 +"Imposto sobre a venda (%): "))
    # rentabilidade
    rentabilidade = float(input("\t"*7 +"Rentabilidade (%): "))

    #formula para calcular o preco de venda
    pv = custo_prod/(1 -((custo_fixo + comissao + imposto + rentabilidade)/100))

    # calcular porcentagem e valores da tabela
    porcentcusto_prod = (custo_prod/pv)*100
    receitaBruta = pv - custo_prod
    porcentReceitaBruta = (receitaBruta/pv)*100
    porcentOutroCusto = custo_fixo + comissao +imposto
    valor_custoFixo = (custo_fixo*pv)/100
    valor_comissao = (comissao*pv)/100
    valor_imposto = (imposto*pv)/100
    valor_outroCusto = valor_custoFixo + valor_comissao + valor_imposto
    valor_rentabilidade = receitaBruta - valor_outroCusto
    porcentRentab = (valor_rentabilidade/pv)*100
    
    # avaliar lucro
    if(rentabilidade > 20):
        print("\t"*12 + "Lucro Alto")
    elif(rentabilidade>10 and porcentRentab<=20):
        print("\t"*12 + "Lucro Médio")
    elif(rentabilidade>0 and porcentRentab<=10):
        print("\t"*12 + "Lucro Baixo")
    elif(rentabilidade == 0):
        print("\t"*12 + "Equilíbrio")
    elif(rentabilidade <0):
        print("\t"*12 + "Prejuízo")

    #Inserir no banco: 
    cursor.execute("INSERT INTO Estoque (id_prod, nome_prod,desc_prod ,custo_prod,custo_fixo ,comissao ,imposto ,rentabilidade) VALUES ({id_prod}, '{nome_prod}', '{desc_prod}', {custo_prod}, {custo_fixo}, {comissao}, {imposto}, {rentabilidade})")
    cursor.execute("TRUNCATE TABLE ESTOQUE")
    connection.commit()
    connection.close()


elif option == 2:

    print("Listagem")

    connection.commit()
    cursor.execute("SELECT * FROM Estoque")

    for row in cursor: 
        #Para imprimir dados tal como foram inseridos no SQL:
        # print(row)

        id_prod, nome_prod, desc_prod, custo_prod, custo_fixo, comissao, imposto, rentabilidade = row
         
        # Chamando a função para calcular os valores
        pv, receitaBruta, porcentcusto_prod, porcentReceitaBruta, porcentOutroCusto, valor_custoFixo, valor_comissao, valor_imposto, valor_outroCusto, valor_rentabilidade, porcentRentab = calcular_valores(
            custo_prod, custo_fixo, comissao, imposto, rentabilidade)
         
        
        print(f"{id_prod} {nome_prod} {desc_prod}")
        print("Descrição\tValor\t%")
        print(f"A. Preço de venda\tR$ {pv:.2f}\t100%")
        print(f"B. Custo de Aquisição (Fornecedor)\tR$ {custo_prod:.2f}\t{porcentcusto_prod:.2f}%")
        print(f"C. Receita Bruta (A-B)\tR$ {receitaBruta:.2f}\t{porcentReceitaBruta:.2f}%")
        print(f"D.Custo Fixo/Administrativo\tR$ {valor_custoFixo:.2f}\t{(valor_custoFixo/pv*100):.2f}%")
        print(f"E.Comissão de Vendas\tR$ {valor_comissao:.2f}\t{(valor_comissao/pv*100):.2f}%")
        print(f"F.Impostos\tR$ {valor_imposto:.2f}\t{(valor_imposto/pv*100):.2f}%")
        print(f"G. Outros Custos (D+E+F)\tR$ {valor_outroCusto:.2f}\t{(valor_outroCusto/pv*100):.2f}%")
        print(f"H. Rentabilidade\tR$ {valor_rentabilidade:.2f}\t{(valor_rentabilidade/pv*100):.2f}%")
        

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