from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run()