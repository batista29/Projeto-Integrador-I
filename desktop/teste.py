import oracledb

connection = oracledb.connect(
    user = "system",
    password = 'PorFavorzinho24@',
    dsn = "localhost/xe"
)

cursor = connection.cursor()

opcao = int(input("Digite 1 (Cadastrar produto), 2 (Alterar cadastro), 3 (Apagar produto), 4 (Listar produto), 5 (Sair do programa): "))
#falta 2(Alterar cadastro); 5(sair do programa)

def alterar_produto_descricao():
    desc_prod=input("Digite uma nova descriçâo: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   
    #cursor.execute("UPDATE Estoque SET desc_prod=", descricao," WHERE id_prod=",id)

    alterar = "UPDATE Estoque SET desc_prod=:desc_prod where id_prod=:id"
    cursor.execute(alterar, {'desc_prod': desc_prod, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()

def alterar_produto_valor():
    custo_prod=input("Digite um novo custo: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   
    alterar = "UPDATE Estoque SET custo_prod=:custo_prod where id_prod=:id"
    cursor.execute(alterar, {'custo_prod':custo_prod, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()
   
def alterar_produto_custo():
    custo_fixo=input("Digite um novo custo fixo: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   

    alterar = "UPDATE Estoque SET custo_fixo=:custo_fixo where id_prod=:id"
    cursor.execute(alterar, {'custo_fixo':custo_fixo, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()

def alterar_produto_comissao():
    comissao=input("Digite um novo valor para a comissâo: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   

    alterar = "UPDATE Estoque SET comissao=:comissao where id_prod=:id"
    cursor.execute(alterar, {'comissao':comissao, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()
   
def alterar_produto_imposto():
    imposto=input("Digite um novo valor para o imposto: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   

    alterar = "UPDATE Estoque SET imposto=:imposto where id_prod=:id"
    cursor.execute(alterar, {'imposto':imposto, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()

def alterar_produto_rentabilidade():
    rentabilidade=input("Digite um novo valor para a rentabilidade ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   

    alterar = "UPDATE Estoque SET rentabilidade=:rentabilidade where id_prod=:id"
    cursor.execute(alterar, {'rentabilidade':imposto, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()

def alterar_produto_nome():
    nome_prod=input("Digite um novo nome: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   

    alterar = "UPDATE Estoque SET nome=:nome where id_prod=:id"
    cursor.execute(alterar, {'rentabilidade':imposto, 'id': id})

    print("nome alterado com sucesso")
    connection.commit()  

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
    cursor.execute("INSERT INTO Estoque  VALUES (:id_prod, :nome_prod, :desc_prod, :custo_prod, :custo_fixo, :comissao, :imposto, :rentabilidade)", {'id_prod' : id_prod, 'nome_prod': nome_prod , 'desc_prod' : desc_prod , 'custo_prod': custo_prod , 'custo_fixo': custo_fixo, 'comissao' : comissao, 'imposto' : imposto, 'rentabilidade' : rentabilidade} )
    connection.commit()
    connection.close()


elif opcao == 4:

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
        print("\t"*7 +f"H. Rentabilidade"+"\t"*3+f"R$ {valor_rentabilidade:.2f}"+"\t"*3+f"{round(valor_rentabilidade/pv*100):.2f}%\n")
        

        if rentabilidade > 20:
            print("\t"*7+"Lucro:\tLucro alto")
        elif rentabilidade > 10:
            print("\t"*7+"Lucro:\tLucro médio")
        elif rentabilidade > 0:
            print("\t"*7+"Lucro:\tLucro baixo")
        elif rentabilidade == 0:
            print("\t"*7+"Lucro:\tEquilíbrio")
        else:
            print("\t"*7+"Lucro:\tPrejuízo")
        print("\n")

    cursor.close()
    connection.close()


elif opcao == 3:

    print("Apagar produto")
    
    id=int(input("Digite o id do produto que deseja excluir: "))

    connection.commit()
    cursor.execute("SELECT * FROM Estoque where id_prod = :id", {'id': id})

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
        print("\t"*7 +f"H. Rentabilidade"+"\t"*3+f"R$ {valor_rentabilidade:.2f}"+"\t"*3+f"{round(valor_rentabilidade/pv*100):.2f}%\n")

    escolha=input("Tem certeza que deseja excluir o id {id}? (S/N)")
    escolha=escolha.upper()
        
    if escolha=='S':
            try:
                cursor.execute("DELETE FROM Estoque WHERE id_prod= :id", {'id': id})
                print("Item excluido com sucesso")
                connection.commit() 
            except oracledb.Error as erro:
                print(erro)
    else:
            print("Seu item não foi excluido")


    connection.commit()
    cursor.close()   
    connection.close()

elif (opcao==6):
    desc_prod=input("Digite uma nova descriçâo: ")
    id=int(input("Digite o id do produto que deseja alterar: "))
   
    #cursor.execute("UPDATE Estoque SET desc_prod=", descricao," WHERE id_prod=",id)

    alterar = "UPDATE Estoque SET desc_prod=:desc_prod where id_prod=:id"
    cursor.execute(alterar, {'desc_prod': desc_prod, 'id': id})

    print("Item alterado com sucesso")
    connection.commit()