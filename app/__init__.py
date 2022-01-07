"""
Example demo server to use a supported web browser to call the WebAuthn APIs
to register and use a credential.

See the file README.adoc in this directory for details.

Navigate to https://localhost:5000 in a supported web browser.
"""
from __future__ import absolute_import, print_function, unicode_literals

import os

from fido2.server import Fido2Server
from fido2.webauthn import PublicKeyCredentialRpEntity
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app():

    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__, static_url_path="")
    app.debug = True
    app.secret_key = os.urandom(32)  # Used for session.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
        os.path.join(basedir, "app.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app


