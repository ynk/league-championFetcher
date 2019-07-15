import os

from flask import Flask, Blueprint, jsonify, render_template, request
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

    @index.route('/', methods=['GET', 'POST'])
    def root():
        valid_servers = ['euw1', 'na1', 'eun1', 'br1', 'la1', 'la2', 'tr1', 'jp1', 'kr', 'ru', 'oc1']
        if request.method == 'GET':
            return render_template("app/root.html", server=valid_servers)
        elif request.method == "POST":
            info = request.form
            print(info)
            return render_template("app/root.html", result=info, server=valid_servers)

    app.register_blueprint(index)
    return app
