from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    pony = StringField("Pony name", validators=[DataRequired()])
    submit = SubmitField()
