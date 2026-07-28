from  extensions import db

class Usuario(db.Model):
     
    __tablename__ = "usuarios"

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    
    emprestimos = db.relationship("Emprestimo",back_populates="usuario")