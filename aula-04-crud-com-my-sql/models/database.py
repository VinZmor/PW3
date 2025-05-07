from flask_sqlalchemy import SQLAlchemy

# Carregando o SQLAlchemy na variável db
db = SQLAlchemy()

# Criando o Model (classe),  parenteses é a herança
class Game (db.Model):
    # Atributos seão as colunas do Banco de Dados
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column (db.String(150))
    plataforma = db.column (db.String(150))
    preco = db.column (db.Float)
    quantidade = db.Column (db.Integer)
    
    # Método contrutor da classe
    def _init_(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano - ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade