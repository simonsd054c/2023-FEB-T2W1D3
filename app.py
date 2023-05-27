from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        'id': 0,
        'name': 'Product 0',
        'price': 110
    },
    {
        'id': 1,
        'name': 'Product 1',
        'price': 200
    },
    {
        'id': 2,
        'name': 'Product 2',
        'price': 330
    },
    {
        'id': 3,
        'name': 'Product 3',
        'price': 120
    }
]

@app.route("/")
def hello_word():
    return "<h1>Hello Hello World World</h1>"

@app.route("/another_route")
def another_route():
    return "This is another route, not the same as previous"

@app.route("/products")
def get_products():
    limit = request.args.get('limit')
    if(limit):
        products_to_return = products[0:int(limit)]
    else:
        products_to_return = products
    return jsonify(products_to_return)

@app.route("/products", methods=["POST"])
def create_product():
    product = request.get_json()
    products.append(product)
    return jsonify(products), 201

@app.route("/products/1", methods=["PUT"])
def update_product1_put():
    product = request.get_json() # only contain name and price
    product['id'] = products[1]['id'] # copy id from original to new
    products[1] = product # replace original with new
    return jsonify(products[1])

@app.route("/products/1", methods=["PATCH"])
def update_product1_patch():
    product = request.get_json()
    for (key, value) in product.items():
        products[1][key] = value
    return jsonify(products[1])

@app.route("/products/1", methods=["DELETE"])
def delete_produt1():
    del products[1]
    return jsonify(message="Product 1 Deleted")

@app.route("/products/0")
def product_0():
    product0 = products[0]
    return jsonify(product0)

@app.route("/products/1")
def product_1():
    product1 = products[1]
    return jsonify(product1)

@app.route("/products/10")
def product_10():
    return jsonify(message="No product with id 10"), 404
