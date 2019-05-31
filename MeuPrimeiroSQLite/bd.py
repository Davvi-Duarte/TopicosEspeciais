import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM tb_estudante;
""")

for linha in cursor.fetchall():
    print("Fresco véi, eu sou", linha[1], "#TiraAMãoDoMeuIF")

print ("Dados consultados com sucesso.")

conn.commit()

conn.close()
