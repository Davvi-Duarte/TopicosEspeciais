from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def getAlunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_aluno;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Dados consultados com sucesso.", 200)

@app.route("/alunos/<int:id>", methods=["GET"])
def getAlunosByID(id):
    pass

@app.route("/cursos", methods=["GET"])
def getCursos():
    pass

@app.route("/cursos/<int:id>", methods=["GET"])
def getCursosByID():
    pass

@app.route("/turmas", methods=["GET"])
def getTurmas():
    pass

@app.route("/turmas/<int:id>", methods=["GET"])
def getTurmasByID():
    pass

@app.route("/")
def hello_world():
    return ("Olá Mundo! Estou aprendendo Flask", 200)
