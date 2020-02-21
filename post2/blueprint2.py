from flask import Blueprint
from flask import render_template

posts2=Blueprint('posts2', __name__, template_folder='hohhoh')
@posts2.route('/')
@posts2.route('/<page>')
def index(page=10):
    return render_template('index_v.html',page=page)

@posts2.route('/1')
def index2():
    return render_template('index.html')