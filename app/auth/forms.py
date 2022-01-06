from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, DataRequired, EqualTo, Length, ValidationError
from app.models import User

def user_exists_with_email(form, field):
    user = User.query.filter_by(email=field.data).first()
    if not user:
        raise ValidationError("There is no registered account with that email.")

class RegistrationForm(FlaskForm):
    email            = StringField("Email *",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=10, max=30, message="Email must be between 10 and 30 characters long")
                                ])
    username         = StringField("Username *",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=4, max=20, message="Username must be between 4 and 20 characters long")
                                ])
    password         = PasswordField("Password *",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=10, max=40, message="Password must be between 10 and 40 characters long"),
                                    EqualTo("password_confirm", message="Passwords must match")
                                ])
    password_confirm = PasswordField("Confirm Password *",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!")
                                ])
    age              = BooleanField(validators=[DataRequired()],false_values=None)
    submit           = SubmitField("Register")

    def validate_username(form, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("Username already exists.")

    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError("Email already exists.")

class LoginForm(FlaskForm):
    email        = StringField("Email",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=10, max=30, message="Email must be between 5 and 30 characters long"),
                                    user_exists_with_email
                                ])
    password     = PasswordField("Password",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=10, max=40, message="Password must be between 10 and 40 characters long")
                                ])
    remember_me  = BooleanField("Remember me")
    submit       = SubmitField("Login")
