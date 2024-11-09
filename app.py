from flask import Flask
from routes import main_routes

app = Flask(__name__)

# Configuraciones de la aplicación
app.config['SECRET_KEY'] = 'tu_clave_secreta'

# Registrar las rutas
app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)