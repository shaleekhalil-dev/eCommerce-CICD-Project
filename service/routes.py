from flask import jsonify, request, abort
from service.models import Product, Category
from service.common import status
from . import app

def check_content_type(content_type):
    if "Content-Type" not in request.headers or request.headers["Content-Type"] != content_type:
        app.logger.error("Invalid Content-Type: %s", request.headers.get("Content-Type"))
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f"Content-Type must be {content_type}")

@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")
    if name: products = Product.find_by_name(name)
    elif category: products = Product.find_by_category(getattr(Category, category.upper()))
    elif available: products = Product.find_by_availability(available.lower() in ["true", "1"])
    else: products = Product.all()
    return jsonify([p.serialize() for p in products]), status.HTTP_200_OK

@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' not found.")
    return jsonify(product.serialize()), status.HTTP_200_OK

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_products(product_id):
    check_content_type("application/json")
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' not found.")
    product.deserialize(request.get_json())
    product.update()
    return jsonify(product.serialize()), status.HTTP_200_OK

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_products(product_id):
    product = Product.find(product_id)
    if product: product.delete()
    return "", status.HTTP_204_NO_CONTENT
