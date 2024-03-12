from . import app
from flask import Flask, render_template, request
from forms import LoginForm


@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        return f"Username: {form.username.data}, <br> Password: {form.password.data}"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
