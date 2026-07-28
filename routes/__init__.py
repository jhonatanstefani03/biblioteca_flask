from routes.livro_routes import livros_bp
from  routes.usuario_routes import usuarios_bp
from  routes.emprestimo_routes import emprestimos_bp

def init_routes(app):
    app.register_blueprint(livros_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(emprestimos_bp)
    