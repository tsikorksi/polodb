from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
# matchid.chukka_num.venue.season_state.conditions.chukka_max.pony.player.result


class InputForm(FlaskForm):
    venue = StringField("Venue name", validators=[DataRequired()])
    pony = StringField("Pony name", validators=[DataRequired()])
    submit = SubmitField()
