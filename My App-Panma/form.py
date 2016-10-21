from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, PasswordField
from wtforms.validators import Required, Email


class loginform(Form):
	name = StringField('What is your name?', validators=[Required()])
	email = TextField('Email address', [Email(),
		Required(message='Email Required!')])
	password = PasswordField('Password',[Required(message='Input Password!')])
	submit = SubmitField('Submit')


	 
