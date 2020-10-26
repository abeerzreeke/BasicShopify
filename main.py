from flask import Flask, jsonify, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Macbook Pro",
        "price": 1000.99,
        "stock_quantity": 3,
        "category": "technology"
    },
    {
        "id": 2,
        "name": "Dell Laptop",
        "price": 899.99,
        "stock_quantity": 5,
        "category": "technology"
    },
    {
        "id": 3,
        "name": "Brita Water filter",
        "price": 39.00,
        "stock_quantity": 2,
        "category": "kitchen"
    }
]


@app.route('/search/by-category/<category_name>')
def check(category_name):
    result = list(filter(lambda product: (product["category"] == category_name), products))
    return jsonify(result)


@app.route('/product/<product_name>')
def details(product_name):
    result = list(filter(lambda product: (product["name"] == product_name), products))
    return jsonify(result)


@app.route('/')
def index():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
