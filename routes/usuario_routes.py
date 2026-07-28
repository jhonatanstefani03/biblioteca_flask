from  flask import Blueprint
from  models.usuario import Usuario
from flask import request
from  extensions import db

usuarios_bp =  Blueprint('usuarios',__name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios =  Usuario.query.all()
    if not usuarios:
        return {'mensagem':'não possui usuarios cadastrados'}

    resultado = []

    for usuario in usuarios:
        resultado.append({
            'id':usuario.id,
            'nome':usuario.nome,
            'email':usuario.email
        })
    return resultado

@usuarios_bp.route('/usuarios', methods=['POST'])
def cadastrar_usuarios():
    data = request.get_json()
   

    nome = data['nome']
    email = data['email']
    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return{'mensagem': 'usuario ja cadastrado'},400

    usuario =Usuario(email=email, nome=nome)
    
    db.session.add(usuario)
    db.session.commit()
    return {
        'id':usuario.id,
        'nome':usuario.nome,
        'email':usuario.email
    },201

@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuarios(id):

    usuario = Usuario.query.get_or_404(id)
    data =  request.get_json()
    usuario.nome =  data['nome']
    db.session.commit()
    return{'id':usuario.id,
           'nome':usuario.nome,
           'email':usuario.email}