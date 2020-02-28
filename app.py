from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask import redirect, url_for, request

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

from posts.blueprint import posts
from post2.blueprint2 import posts2

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView



app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(posts2, url_prefix='/vlog')


migrate=Migrate(app, db)
manager=Manager(app)
manager.add_command('db', MigrateCommand)

from models import *

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')
    def inaccessible_callback(self,name,  **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
    def update_model( self, form, model ):
        print('updeit_model')
        super().update_model(form, model)

class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags', 'slug']
    can_create = False
    can_delete = False
    column_exclude_list = ['title']
    column_labels = dict(title='TIT')

class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']

admin=Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))

admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)