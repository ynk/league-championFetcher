import os

from decouple import config
from flask import Blueprint, Flask, jsonify, render_template, request
from flask_api import status
from requests.exceptions import ConnectionError

from app.riot import Riot


def create_app(*args):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = config("APP_SECRET_KEY", None)
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
            'Europe Nordic & East': 'eun1',
            'Latin America North': 'la1',
            'Latin America South': 'la2',
            'Oceania': 'oc1',
            'Turkey': 'tr1',
            'Japan': 'jp1',
            'Korean': 'kr',
            'Russia': 'ru'
        }
        valid_servers = [
            'North America',
            'Europe West',
            'Brazil',
            'Europe Nordic & East',
            'Latin America North',
            'Latin America South',
            'Oceania',
            'Russia',
            'Turkey',
            'Japan',
            'Korean',
        ]

        if request.method == 'GET':
            return render_template("app/root.html", server=valid_servers)
        elif request.method == "POST":
            info = request.form
            riot_api = config("RIOT_KEY", None)
            account_name = info['account_name'] if 'account_name' in info else None
            server = info['servers'] if 'servers' in info else None
            error = False

            if riot_api is None:
                error = True
                result = {
                    "message": "Damnn! There is something wrong on our side. Can you inform us in discord?",
                    "status": 404,
                }

            if account_name is None or server is None:
                error = True
                result = {
                    "message": "What are you hiding bro? You haven't given all the info!",
                    "status": 404,
                }

            if len(account_name) < 3 or len(account_name) > 16:
                error = True
                result = {
                    "message": "Dude! Your account name cannot be {}. Stop messing with us.".format(account_name),
                    "status": 404,
                }

            # if len(riot_api) != 42:
            #     return {
            #         "message": "Are you sure you have the right API key? This ({}) doesn't seem right.".format(riot_api),
            #         "status": 403,
            #     }

            # Empty String. Won't break
            server = server_to_riot_name[server] if server in server_to_riot_name else ""
            if server == "":
                error = True
                result = {
                    "message": "Dude! What the heck is your server? We couldn't find it anywhere. Damn!",
                    "status": 404,
                }

            if not error:
                # Only Riot if no error, homie 0_0
                try:
                    riot = Riot(account_name, server, riot_api)
                    result = riot.master_controller()
                except ConnectionError:
                    result = {
                        "message": "Sorry man! Riot is not sending us the data at this moment. Will you try a bit later?",
                        "status": 404,
                    }

            return render_template("app/root.html",
                                   result=result,
                                   server=valid_servers)

    app.register_blueprint(index)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
