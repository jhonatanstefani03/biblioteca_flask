from extensions import db


class Emprestimo(db.Model):
    __tablename__='emprestimos'

    id = db.Column(db.Integer,primary_key=True)

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    livro_id = db.Column(
        db.Integer,
        db.ForeignKey("livros.id"),
        nullable=False
    )

    usuario = db.relationship("Usuario",back_populates="emprestimos")
    livro = db.relationship("Livro",back_populates="emprestimos")