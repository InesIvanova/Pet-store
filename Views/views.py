from Models import models
import pickle
from flask import render_template

ABSOLUTE_PATH = 'C://Users/Ines/PycharmProjects/Mini-Lab-Pet_store_site'

FOOD_PATH = f'{ABSOLUTE_PATH}/DB/Food_db/food.txt'
USERS_PATH = f'{ABSOLUTE_PATH}/DB/Users_db/users.txt'
ANIMALS_PATH = f'{ABSOLUTE_PATH}/DB/Animals_db/animals.txt'
TOYS_PATH = f'{ABSOLUTE_PATH}/DB/Toys_db/toys.txt'
CAGES_PATH = f'{ABSOLUTE_PATH}/DB/Cages_db/cages.txt'

def index():
    return render_template('index.html')

def show_login():
    return render_template('login.html')

def login(form):
    first_name = form['first_name']
    last_name = form['last_name']
    password = form['password']

    users = get_users_Queryset()
    print(users[0].first_name)

    is_user = list(filter(lambda user: user.first_name == first_name and user.last_name == last_name and user.password == password, users))

    if is_user:
        return render_template('index.html', user=is_user[0])
    return render_template('error.html')




def save_users(users):
    with open(USERS_PATH, 'wb') as file:
        pickle.dump(users, file)

def create_user(user_data):
    try:
        user = models.User(first_name=user_data[0], last_name=user_data[1], password=user_data[2], match_pass=user_data[3], phone=user_data[4])
        return user
    except Exception as exception:
        print(exception)

def get_users_Queryset():
    with open(USERS_PATH, 'rb') as file:
        users = pickle.load(file)
    return users

def show_users():
    users = get_users_Queryset()
    return render_template('users.html', users=users)


def create_food(food_data):
    try:
        food = models.Food(id=food_data[0], kilograms=food_data[1], price=food_data[2], kind=food_data[3], date_of_validity=food_data[4])
        return food
    except Exception as exception:
        print(exception)

def save_food(food_list):
    with open(FOOD_PATH, 'wb') as file:
        pickle.dump(food_list, file)


def get_food_queryset():
    with open(FOOD_PATH, 'rb') as file:
        food_list = pickle.load(file)
    return render_template('items.html', items=food_list, is_toy=False)


def create_toy(toy_data):
    try:
        toy = models.Toy(id=toy_data[0], price=toy_data[1], kind=toy_data[2])
        return toy
    except Exception as exception:
        print(exception)


def save_toys(toys_list):
    with open(TOYS_PATH, 'wb') as file:
        pickle.dump(toys_list, file)

def get_toys_queryset():
    with open(TOYS_PATH, 'rb') as file:
        toys = pickle.load(file)
    return render_template('items.html', items=toys, is_toy=True)


def create_cage(cage_data):
    try:
        cage = models.Cage(id=cage_data[0], price=cage_data[1], kind=cage_data[2], volume=cage_data[3])
        return cage
    except Exception as exception:
        print(exception)


def save_cages(cages_list):
    with open(CAGES_PATH, 'wb') as file:
        pickle.dump(cages_list, file)

def get_cages_queryset():
    with open(CAGES_PATH, 'rb') as file:
        cages = pickle.load(file)
        return cages

def create_animal(animal_data):
    try:
        cls = animal_data[0]
        upper_letter = cls[0].upper()
        class_ = list(upper_letter) + list(cls[1:])
        class_ = class_[0] + class_[1] + class_[2]
        string = f'models.{class_}({animal_data[1]}, "{animal_data[2]}", {animal_data[3]}, {animal_data[4]})'
        animal = eval(string)
        return animal
    except Exception as exception:
        print(exception)


def save_animals(animals_list):
    with open(ANIMALS_PATH, 'wb') as file:
        pickle.dump(animals_list, file)

def get_animals_queryset():
    with open(ANIMALS_PATH, 'rb') as file:
        animals = pickle.load(file)
        return animals


