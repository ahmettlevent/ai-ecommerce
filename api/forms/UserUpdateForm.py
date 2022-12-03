from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField


class UserUpdateForm(Form):
    name = StringField(
        'Name', [validators.DataRequired(), validators.Length(min=4, max=30)])
    surname = StringField(
        'Surname', [validators.DataRequired(), validators.Length(min=4, max=25)])
    city = StringField(
        'City', [validators.DataRequired(), validators.Length(min=4, max=25)])
    state = StringField(
        'State', [validators.DataRequired(), validators.Length(min=4, max=25)])
    address = StringField(
        'Address', [validators.DataRequired(), validators.Length(min=10, max=200)])
    age = IntegerField(
        'Age', [validators.DataRequired(), validators.NumberRange(min=18, max=80)])
