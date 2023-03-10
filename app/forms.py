from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed



class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedrooms = IntegerField('No. of Bedrooms', validators=[InputRequired(), NumberRange(min=1, max=99, message='Number outside range')])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=1, max=99, message='Number outside range')])
    location = StringField('Location', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    type = SelectField('Type', choices=[('Apartment'), ('House')])
    description=TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])