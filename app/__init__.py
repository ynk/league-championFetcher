import os

from flask import Flask, Blueprint, jsonify, render_template, request
from flask_api import status

from app.riot import Riot


def create_app(*args):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "App_secret_key!"
    # ensure the instance folder exists
    try:
        if not os.path.exists(app.instance_path):
            os.makedirs(app.instance_path)
    except OSError as _:
        print(str(_))

    index = Blueprint('lookup', __name__, url_prefix='/')

    @index.route('/', methods=['GET', 'POST'])
    def riot():
        server_to_riot_name = {
            'North America': 'na1',
            'Europe West': 'euw1',
            'Brazil': 'br1',
            'Euripe Nordic & East': 'eun1',
            'Latin America North': 'la1',
            'Latin America South': 'la2',
            'Ocenia': 'oc1',
            'Turkey': 'tr1',
            'Japan': 'jp1',
            'Korean': 'kr',
            'Russia': 'ru'
        }
        valid_servers = [
            'North America',
            'Europe West',
            'Brazil',
            'Euripe Nordic & East',
            'Latin America North',
            'Latin America South',
            'Ocenia',
            'Russia',
            'Turkey',
            'Japan',
            'Korean',
        ]

        if request.method == 'GET':
            return render_template("app/root.html", server=valid_servers)
        elif request.method == "POST":
            info = request.form
            riot_api = info['riot_api'] if 'riot_api' in info else None
            account_name = info['account_name'] if 'account_name' in info else None
            server = info['servers'] if 'servers' in info else None

            if server is None:
                return {
                    "message": "server cannot be None. It's required!",
                    "status": 404,
                }
            else:
                # Empty String. Won't break
                server = server_to_riot_name[server] if server in server_to_riot_name else ""
                if server == "":
                    return {
                        "message": "Server not found!",
                        "status": 404,
                    }

            riot = Riot(account_name, server, riot_api)
            result = riot.master_controller()
            return render_template("app/root.html",
                                   result=result,
                                   server=valid_servers)

    app.register_blueprint(index)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
