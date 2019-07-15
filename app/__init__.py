import os

from flask import Flask, Blueprint, render_template, request

from app.riot import Riot

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
        riot_api = info['riot_api'] if 'riot_api' in info else None
        account_name = info['account_name'] if 'account_name' in info else None
        server = info['servers'] if 'servers' in info else None

        riot = Riot(account_name, server, riot_api)
        result = riot.master_controller()
        return render_template("app/root.html",
                               result=result,
                               server=valid_servers)


app.register_blueprint(index)
