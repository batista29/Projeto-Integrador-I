import oracledb

connection = oracledb.connect(
    user = "system", 
    password = 'PorFavorzinho24@', 
    dsn = "localhost:1521/XE"  
)
print ("Conectado")

cursor = connection.cursor()

# Casos: 
def case1():
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


    # tabela com o print
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'Descrição':^30}"+ f"|{'Valor':^8}" + f"|{'%':^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'A. Preço de venda':<30}"+ f"|{round(pv,2):^8}"+ f"|{'100':^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'B. Custo de aquisição':<30}"+ f"|{custo_prod:^8}"+ f"|{porcentcusto_prod:^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'C. Receira Bruta':<30}"+ f"|{receitaBruta:^8}"+ f"|{porcentReceitaBruta:^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'D. Custo Fixo/Administrativo':<30}"+ f"|{valor_custoFixo:^8}"+ f"|{custo_fixo:^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'E. Comissão de Vendas':<30}"+ f"|{valor_comissao:^8}"+ f"|{comissao:^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'F. Impostos':<30}"+ f"|{valor_imposto:^8}"+ f"|{imposto:^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'G. Outros Custos':<30}"+ f"|{valor_outroCusto:^8}"+ f"|{porcentOutroCusto:^4}|")
    print("\t"*7+ "-"*46)
    print("\t"*7 + f"|{'H. Rentabilidade':<30}"+ f"|{valor_rentabilidade:^8}"+ f"|{rentabilidade:^4}|")
    print("\t"*7+ "-"*46)

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
    connection.close()

def case2():
    print("Listagem")

    cursor.execute("SELECT * FROM Estoque")

    for row in cursor: 
        print(row)
    cursor.close()
    connection.close()

def default_case():
    print("Executando caso padrão")

def switch_case(argument):
    switcher = {
        1: case1,
        2: case2,
    }
    # Obtém a função correspondente ao argumento fornecido
    func = switcher.get(argument, default_case)
    # Chama a função
    func()

# Captura a entrada do usuário
option = int(input("Digite 1 (Cadastrar produto) ou 2 (Listar produto): "))

# Chama a função switch_case com base na entrada do usuário
switch_case(option)



