import os
from campaign_requests import app as campaign_app
from flask_migrate import upgrade

basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    app = campaign_app.create_app()
    with app.app_context():
        upgrade('./campaign_requests/migrations')
    app.run(host='0.0.0.0', port=8000)
