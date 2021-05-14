from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import rospkg

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    #print(os.path.dirname(os.path.realpath(__file__)))
    rospack = rospkg.RosPack()
    pkg_dir = rospack.get_path("image_stream_server")
    module_dir = os.path.join(pkg_dir, "src", "webapp")
    app = Flask(__name__, template_folder=os.path.join(module_dir, "templates"))
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(module_dir, "db.sqlite"))
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    # blueprint for auth routes in our app
    from .webcam import webcam as webcam_blueprint
    app.register_blueprint(webcam_blueprint)

    return app
