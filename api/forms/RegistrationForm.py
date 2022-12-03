from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField


class RegistrationForm(Form):
    name = StringField(
        'Name', [validators.DataRequired(), validators.Length(min=4, max=30)])
    surname = StringField(
        'Surname', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField(
        'Email Address', [validators.DataRequired(), validators.Email()])
    city = StringField(
        'City', [validators.DataRequired(), validators.Length(min=4, max=25)])
    state = StringField(
        'State', [validators.DataRequired(), validators.Length(min=4, max=25)])
    address = StringField(
        'Address', [validators.DataRequired(), validators.Length(min=10, max=200)])

    age = IntegerField(
        'Age', [validators.DataRequired(), validators.NumberRange(min=18, max=80)])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('repeat_password', message='Passwords must match')
    ])
    repeat_password = PasswordField(
        'Repeat Password', [validators.DataRequired(), ])
