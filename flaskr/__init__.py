import os
from flask import Flask
from .views import views

def create_app(test_config=None):

    UPLOAD_FOLDER = os.path.join(os.getcwd(),'flaskr','static','media')
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    app = Flask(__name__, instance_relative_config=True)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.register_blueprint(views)
    return app