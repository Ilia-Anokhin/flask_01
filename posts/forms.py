
from wtforms import Form, TextAreaField, StringField, IntegerField, ValidationError
from wtforms.validators import NumberRange

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')


class AgeForm(Form):
    age = IntegerField(u'Age', [NumberRange(min=20)])

    def validate_age(form, field) :
        if field.data < 13 :
            raise ValidationError("We're sorry, you must be 13 or older to register")