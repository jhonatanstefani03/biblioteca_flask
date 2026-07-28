from  flask import Flask
from  config import Config
from extensions import  db,migrate
from models.livro import Livro
from  models.usuario import Usuario
from models.emprestimo import Emprestimo
from routes import init_routes

app =  Flask(__name__)

print(db.Model.metadata.tables.keys())

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
init_routes(app)


@app.route('/')
def home():
   return 'em processo  de criação',200

if __name__ == '__main__':
    app.run(debug=True)