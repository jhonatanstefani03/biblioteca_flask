from models.emprestimo import Emprestimo
from flask import request
from models.usuario import Usuario
from models.livro import Livro
from extensions import db

def criar_emprestimo(data):


    usuario = Usuario.query.get_or_404(data['usuario_id'])
    livro = Livro.query.get_or_404(data['livro_id'])

    if livro.quantidade <= 0:
        return{'mensagem':'livro indisponivel'}

    emprestimo = Emprestimo(usuario_id=usuario.id,livro_id=livro.id)

    livro.quantidade -= 1

    db.session.add(emprestimo)
    db.session.commit()
    return{
        'id':emprestimo.id,
        'livro':emprestimo.livro.titulo,
        'usuario':emprestimo.usuario.nome
    },201

def devolver_emprestimo(emprestimo_id):
   
    emprestimo = Emprestimo.query.get_or_404(emprestimo_id)
    livro = emprestimo.livro

    livro.quantidade += 1



    db.session.delete(emprestimo)
    db.session.commit()

    return{"mensagem":'livro devolvido'}
        