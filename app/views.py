from flask import jsonify, request
from app.models import Product

#Una función del módulo flask para convertir a formato json listas y diccionarios de python

def index():
    response = {'message':'Hola mundo API FLASK'}
    return jsonify(response)


"""Un crud de productos"""

#Función que busca todo el listado de productos

def get_all_products():
    products = Product.get_all()
    list_products = [product.serialize() for product in products]
    return jsonify(list_products)

def get_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(product.serialize())

def create_product():
    data = request.json
    #Falta agregar una lógica de validación de datos del lado del backend.
    new_product= Product(None, data['title'], data['price'], data['release_date'], data ['banner'])
    new_product.save()
    return jsonify({'message':'Producto creado con éxito.'}), 201

def update_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Producto no encontrado.'}), 404
    data = request.json
    product.title = data['title']
    product.price = data['price']
    product.release_date = data['release_date']
    product.banner = data['banner']
    product.save()
    return jsonify({'message': 'Producto actualizado.'})

def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Producto no encontrado.'}), 404
    product.delete()
    return jsonify({'message': 'Producto eliminado.'})


 