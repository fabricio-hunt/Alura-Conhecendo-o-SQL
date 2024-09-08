import sqlite3

# Criar uma conexão com o banco de dados
conexao = sqlite3.connect('curso_sql.db')


#cursos para comandos SQL
cursor = conexao.cursor()

#Execução dos Comandos SQL 

cursor.execute('CREATE TABLE Pedidos(ID INTEGER PRIMARY KEY AUTOINCREMENT, Data_do_Pedido TEXT NOT NULL,Status TEXT NOT NULL,Total_do_Pedido REAL NOT NULL,Cliente TEXT NOT NULL,Data_de_Envio_Estimada TEXT)')

cursor.execute('CREATE TABLE Fornecedores (ID INTEGER PRIMARY KEY AUTOINCREMENT,Nome_do_Fornecedor TEXT NOT NULL,Pais_de_Origem TEXT NOT NULL,Informacoes_de_Contato TEXT NOT NULL,Data_de_Inicio TEXT NOT NULL)')


