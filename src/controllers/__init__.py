from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.controllers.home_controller import home_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.categories_controller import categories_bp
    from src.controllers.products_controller import products_bp
    from src.controllers.users_controller import users_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)

    return app