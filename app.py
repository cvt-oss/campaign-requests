import os
from flask import render_template
from config import connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

@connex_app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    connex_app.run(debug=False)
