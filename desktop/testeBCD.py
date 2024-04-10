import cx_Oracle

# Informações de conexão
username = ''
password = ''
host = ''  # Endereço do servidor
port = 1521        # Número da porta padrão do Oracle
service_name = 'XE'  # Ou substitua por SID, caso esteja usando

# String de conexão
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Conectar ao banco de dados
connection = cx_Oracle.connect(username, password, dsn)

# Criar um cursor
cursor = connection.cursor()

# Consulta SQL
sql = 'select nome_prod from Estoque'

# Executar a consulta
cursor.execute(sql)

# Recuperar os resultados
for nome_prod in cursor:
    print(f'{nome_prod}')

# Fechar o cursor
cursor.close()
