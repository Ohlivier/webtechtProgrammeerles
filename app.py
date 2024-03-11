from flask import Flask, render_template
from config import Config
from forms import LoginForm
from . import app


@app.route('/')
def hello_world():  # put application's code here
    form = LoginForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
