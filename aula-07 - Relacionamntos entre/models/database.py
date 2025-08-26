from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Console" com seus atributos.
class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    fabricante = db.Column(db.String(150))
    ano_lancamento = db.Column(db.Integer)

    def __init__(self, nome, fabricante, ano_lancamento):
        self.nome = nome
        self.fabricante = fabricante
        self.ano_lancamento = ano_lancamento
        

# Classe responsável por criar a entidade "Games" com seus atributos.
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    # Aqui está como relacionar as tabelas, usando a chave estrangeira
    console_id = db.Column(db.Integer, db.ForeignKey('console.id'))
    
    # Criando o relacionamento
    # lazy=True pega os dados que estão relacionados com as tabelas
    # backref são os bancos referentes
    console = db.relationship('Console', backref=db.backref('game', lazy=True))

    def __init__(self, titulo, ano, categoria, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade
