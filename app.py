from . import app
from .forms import LoginForm, RegisterForm
from .models import User
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user


@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Succesvol ingelogd.')
            redir = request.args.get('next')

            if redir is None or not redir[0] == '/':
                redir = url_for('index')
                return redirect(redir)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and request.method == 'POST':
        return f"E-mail: {form.email.data} <br> Username: {form.username.data}, <br> Password: {form.password.data}"
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
