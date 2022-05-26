from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(max=30), Email()])
    password = PasswordField('Password', [DataRequired(), Length(min=8, max=30)])
    submit = SubmitField('Submit')
