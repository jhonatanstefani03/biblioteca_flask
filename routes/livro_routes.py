from flask import Blueprint
from models.livro import Livro
from flask import request
from extensions import db


livros_bp= Blueprint('livros',__name__)


@livros_bp.route('/livros',methods=['GET'])
def listar_livros():
    livros = Livro.query.all()

    if not livros:
        return {'mensagem':'nao possuem livros cadastrados'},401

    resultado = []

    for livro in livros:
        resultado.append({
            'id':livro.id,
            'titulo':livro.titulo,
            'autor':livro.autor,
            'quantidade':livro.quantidade
        })

    return resultado


@livros_bp.post('/livros')
def criar_livro():
    data =  request.get_json()

    titulo = data['titulo']
    autor =  data['autor']
    quantidade = data['quantidade']

    livro_existente =  Livro.query.filter_by(titulo=titulo).first()
    if livro_existente:
        return{'mensagem':'livro ja cadastrado'}

    livro = Livro(titulo=titulo,
                  autor=autor,
                  quantidade=quantidade)
    db.session.add(livro)
    db.session.commit()
    return {
        'id':livro.id,
        'titulo':livro.titulo,
        'autor':livro.autor,
        'quantidade':livro.quantidade
    }