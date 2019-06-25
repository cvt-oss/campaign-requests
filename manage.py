# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from app import app, db

# if 'APP_SETTINGS' in os.environ:
#     app.app.config.from_object(os.environ['APP_SETTINGS'])
# else:
#     app.app.config.from_object('config.DevelopmentConfig')

# migrate = Migrate(app.app, db)

# manager = Manager(app.app)
# manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     manager.run()
