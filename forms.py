
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL

species = ["Cat","Dog","Porcupine"]

class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[
                       InputRequired(message="pet name can't be blank")])
    species = SelectField('Species', choices=[(sp, sp) for sp in species])
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    notes = StringField("Notes")