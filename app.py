from flask import Flask, g
import sqlite3

DATABASE = "blog.db"
secret_key = "spfc"

app = Flask(__name__)
app.config.from_object(__name__)


def conectar_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.db = conectar_db()

@app.teardown_request
def fim_requisicao(exc):
    g.db.close()


@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.db.execute(sql)
    entradas = []
    return str(entradas)


'''
@app.route('/home')
def home():
    return "O site será feito Aqui!!!" '''
