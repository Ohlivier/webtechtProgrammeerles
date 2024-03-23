from . import app, db
from .forms import LoginForm, RegisterForm
from .models import User
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user



@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            # flash('Succesvol ingelogd.')
            redir = request.args.get('next')

            if redir is None or not redir[0] == '/':
                redir = url_for('index')
                return redirect(redir)
            return redirect(url_for('index'))
    elif current_user.is_authenticated:
        flash("Je bent al ingelogd")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and request.method == 'POST':
        if form.validate_on_submit():
            print(form.password.data)
            user = User(form.email.data,
                        form.username.data,
                        form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Dank voor de registratie. Er kan nu ingelogd worden! ')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('index'))

@app.route('/welkom')
@login_required
def welkom():
    return render_template('welkom.html')


if __name__ == '__main__':
    app.run(debug=True)
