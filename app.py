from flask import Flask
from model import db
from routes import task_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'task_10_02_2024'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Registrar las rutas
app.register_blueprint(task_routes)

if __name__ == '__main__':
    app.run(debug=True)