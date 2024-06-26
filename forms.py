from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Regexp


class Registration(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=3, max=60)])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('password_confirm',
                                                                              message="Passwords have to be identical"),
                                                     Length(min=6, max=60),
                                                     Regexp(
                                                         regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,60}$",
                                                         message="Password should contain at least one letter, one number and one special sign")])
    password_confirm = PasswordField("Confirm password", validators=[InputRequired(),
                                                                     Length(min=6, max=60)])
    email = StringField("Email", validators=[InputRequired(), Email(message="Type correct email address")])
    submit = SubmitField('Sign Up!')


class Login(FlaskForm):
    username = StringField("Username",
                           validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=60)])
    submit = SubmitField('Sign In!')
