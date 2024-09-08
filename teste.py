import sqlite3

# Criar uma conexão com o banco de dados
conexao = sqlite3.connect('curso_sql.db')

cursor = conexao.cursor()

#execução de comando SQL
#cursor.execute("CREATE TABLE Fornecedores (ID INTEGER PRIMARY KEY AUTOINCREMENT,Nome_do_Fornecedor TEXT NOT NULL,Pais_de_Origem TEXT NOT NULL,Informacoes_de_Contato TEXT NOT NULL,Data_de_Inicio TEXT NOT NULL)")

#conexao.commit()


cursor.execute("SELECT * FROM Fornecedores")
print(cursor.fetchall())
