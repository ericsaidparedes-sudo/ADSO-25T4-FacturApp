from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__)

@products_bp.route('/form_products')
def form_products():
    return render_template('products/form_products.html')

@products_bp.route('/list_products')
def list_products():
    return render_template('products/list_products.html')