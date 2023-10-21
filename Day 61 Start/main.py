# Importing Libraries
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash



class UserForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.secret_key = "McLaren"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = UserForm()
    form.validate_on_submit()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit() and email == "admin@email.com" and password == "12345678":
        return render_template('success.html')
    elif form.validate_on_submit():
        return render_template('denied.html')
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
