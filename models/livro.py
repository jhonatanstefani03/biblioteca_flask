from  extensions import db

class Livro(db.Model):
     
    __tablename__ = "livros"

    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(255), nullable=True)
    autor = db.Column(db.String(255), nullable=True)
    quantidade = db.Column(db.Integer,nullable=True)

    emprestimos = db.relationship("Emprestimo",back_populates="livro")