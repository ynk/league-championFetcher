import os

from flask import Flask, Blueprint, jsonify
from flask_api import status


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "App_secret_key!"
    # ensure the instance folder exists
    try:
        if not os.path.exists(app.instance_path):
            os.makedirs(app.instance_path)
    except OSError as _:
        print(str(_))

    index = Blueprint('index', __name__, url_prefix='/')

    @index.route('/')
    def root():
        return jsonify(
            message='It works!',
            status_code=status.HTTP_200_OK,
        )

    app.register_blueprint(index)
    return app
