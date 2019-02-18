from flask import Flask, request
from Views import views


app = Flask(__name__, template_folder='Templates')

@app.route('/')
def hello_world():
    return views.index()

@app.route('/items/food/')
def show_food():
    return views.get_food_queryset()

@app.route('/items/toys/')
def show_toys():
    return  views.get_toys_queryset()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return views.login(request.form)
    return views.show_login()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return views.register(request.form)
    return views.show_register()


@app.route('/users/<username>')
def get_user(username):
    return views.show_user(username)


@app.route('/users/')
def show_users():
    return views.show_users()


if __name__ == '__main__':
    app.run()