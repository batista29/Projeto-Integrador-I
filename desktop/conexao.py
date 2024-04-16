
import oracledb
#import getpass 
#pw = getpass.getpass("Entre com sua sneha: ")

connection = oracledb.connect(
    user = "system", 
    password = 'PorFavorzinho24@', 
    dsn = "localhost:1521/XE"  
)
print ("Conectado")

cursor = connection.cursor()

cursor.execute("INSERT INTO Estoque (id_prod, nome_prod,desc_prod ,custo_prod,custo_fixo ,comissao ,imposto ,rentabilidade) VALUES (20,'geladeira','geladeira grande branca',5000,200,10,300,20)")

#Para ler as informações:
cursor.execute("SELECT * FROM Estoque")

for row in cursor: 
    print(row)
cursor.close()
connection.close()

#Depoisde tudo, entra no sqlDeveloper e da um select: select * from test;
