from flask import Blueprint, render_template

users_bp = Blueprint('users', __name__)

@users_bp.route('/form_users')
def form_users():
    return render_template('users/form_users.html')

@users_bp.route('/list_users')
def list_users():
    return render_template('users/list_users.html')