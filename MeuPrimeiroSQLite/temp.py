import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_estudante(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    endereco TEXT NOT NULL,
    nascimento DATE NOT NULL,
    matricula VARCHAR(12) NOT NULL
    );
""")
print("Tabela criada com sucesso")
conn.close()

#despois

cursor.execute("""
INSERT INTO tb_estudante (nome, endereco, nascimento, matricula)
VALUES ("Davvi", "Alagoa Grande", '2001-11-30', 201613710005);
""")

conn.commit()

#despois

cursor.execute("""
    SELECT * FROM tb_estudante;
""")
for linha in cursor.fetchall():
    print(linha)
print ("Dados consultados com sucesso.")
