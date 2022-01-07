import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    register = SubmitField("Register")
    authenticate = SubmitField("Authenticate")

