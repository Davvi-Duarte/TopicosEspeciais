import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

lista=[('Davvi', 'PB', '2001-02-28', '201613710007'),('Davvila', 'RJ', '2004-02-28', '201613710014')]

cursor.executemany("""
    INSERT INTO tb_estudante (nome, endereco, nascimento, matricula) VALUES(?, ?, ?, ?);
""", lista)
conn.commit()

print ("Dados inseridos com sucesso.")
conn.close()
