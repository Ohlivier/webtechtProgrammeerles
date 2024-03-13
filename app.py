from . import app
from flask import render_template, request
from .forms import LoginForm, RegisterForm


@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        return f"Username: {form.username.data}, <br> Password: {form.password.data}"
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and request.method == 'POST':
        return f"E-mail: {form.email.data} <br> Username: {form.username.data}, <br> Password: {form.password.data}"
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
