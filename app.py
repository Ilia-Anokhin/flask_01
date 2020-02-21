from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
app.config.from_object(Configuration)
db=SQLAlchemy(app)


from posts.blueprint import posts
from post2.blueprint2 import posts2

from flask_admin import Admin
app.register_blueprint(posts, url_prefix='/blog')

app.register_blueprint(posts2, url_prefix='/vlog')


migrate=Migrate(app, db)
manager=Manager(app)
manager.add_command('db', MigrateCommand)

admin=Admin(app)