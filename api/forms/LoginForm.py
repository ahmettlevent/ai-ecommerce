from wtforms import Form, BooleanField, StringField, PasswordField, validators


class LoginForm(Form):

    email = StringField(
        'Email Address', [validators.DataRequired(), validators.Email()])

    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
