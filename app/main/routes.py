import hashlib
import json
import random
import string

from app import db, login_manager
from app.forms import LoginForm
from app.main import bp
from flask import render_template


@bp.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return None


# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     return redirect('/login')
