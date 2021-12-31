from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length


class UpdateAccountForm(FlaskForm):
	email 	= StringField("Update Email",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=10, max=40, message="email must be between 10 and 40 characters long")
								])
	username = TextAreaField("Update Description",
								validators=[
									InputRequired("Input is required!"),
									DataRequired("Data is required!"),
									Length(min=4, max=20, message="Username must be between 4 and 20 characters long")
								])
	submit  	= SubmitField("Update")
