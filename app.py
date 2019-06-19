import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import connexion

# app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

if 'APP_SETTINGS' in os.environ:
    app.app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.app.config.from_object('config.DevelopmentConfig')

app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app.app)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()