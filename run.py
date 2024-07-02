from flask import Flask
#Importo un objeto de la clase flask
from app.database import init_app
#Importo la función que inicializaba la aplicación con el manejo de la bd
from app.views import *
#Importo todas las funciones desde las vistas
from flask_cors import CORS

#Crear una instancia de Flask
app = Flask(__name__)

#Ejecuto la función para inicializar la app para el manejo de la bd
init_app(app)

#Que permita solicitudes desde cualquier origen
CORS(app) #CORS(app, ['Dominio desde el que quiero que se acceda a mi backend'])

#Asociación de las rutas con las vistas, el método correspondiente
app.route('/',methods=['GET'])(index)
app.route('/api/products/',methods=['GET'])(get_all_products)
app.route('/api/products/',methods=['POST'])(create_product)
app.route('/api/products/<int:product_id>', methods=['GET'])(get_product)
app.route('/api/products/<int:product_id>', methods=['PUT'])(update_product)
app.route('/api/products/<int:product_id>', methods=['DELETE'])(delete_product)

#Permite separar el código que se ejecuta cuando se corre el archivo.
if __name__=='__main__':
    #Levanta el servidor de desarrollo flask:
    app.run(debug=True)
