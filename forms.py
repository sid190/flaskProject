from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, SubmitField

class Signupform(FlaskForm):
    username=StringField("username")
    password=PasswordField("password")
    submit=SubmitField("Sign Up")