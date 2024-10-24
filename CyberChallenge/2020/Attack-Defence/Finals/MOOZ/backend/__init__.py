import os
from contextlib import suppress


from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.exc
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='cKAlgR32BfhnpzuF',
        SQLALCHEMY_DATABASE_URI=('sqlite:///' + os.path.join(app.instance_path, 'db.sqlite')),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # ensure the instance folder exists
    with suppress(OSError):
        os.makedirs(app.instance_path)

    # init db
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({"status":"fail","message":"page not found"}), 404

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({"status":"fail","message":"forbidden"}), 403

    # @app.after_request
    # def disable_cors(response):
    #     response.headers['Access-Control-Allow-Origin'] = "http://testip:8080"
    #     response.headers['Access-Control-Allow-Credentials'] = "true"
    #     response.headers['Access-Control-Allow-Headers'] ="Content-Type"
    #     return response

    from . import auth
    app.register_blueprint(auth.bp)
    auth.login_manager.init_app(app)

    from . import messages
    app.register_blueprint(messages.bp)

    from . import application
    app.register_blueprint(application.bp)

    from . import crypto_func
    app.register_blueprint(crypto_func.bp)

    with app.app_context():
        try:
            db.create_all()
        except sqlalchemy.exc.OperationalError as e:
            print(e)

    # admin = Admin(app, name='Admin', template_mode='bootstrap3')
    # admin.add_view(ModelView(auth.User, db.session))
    # admin.add_view(ModelView(messages.Message, db.session))

    return app

