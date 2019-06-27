import os
import campaign_requests
from flask_migrate import upgrade

basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    app = campaign_requests.create_app()
    with app.app.app_context():
        upgrade('./campaign_requests/migrations')
    app.run()
