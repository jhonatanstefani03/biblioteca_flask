from  flask import Blueprint
from  flask import request
from services.emprestimo_service import criar_emprestimo,devolver_emprestimo


emprestimos_bp = Blueprint('emprestimos',__name__)


@emprestimos_bp.post('/emprestimos')
def emprestimo():
    data = request.get_json()


    return criar_emprestimo(data)

@emprestimos_bp.delete('/emprestimos/<int:id>')
def deletar_emprestimo(id):
    return devolver_emprestimo(id)