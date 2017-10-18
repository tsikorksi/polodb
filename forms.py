from flask_wtf import Form
from wtforms import StringField, SubmitField


class InputForm(Form):
    pony = StringField("Pony name")