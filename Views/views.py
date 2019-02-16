from Models import models
import pickle

FOOD_PATH = '../DB/Food_db/food.txt'
USERS_PATH = '../DB/Users_db/users.txt'
ANIMALS_PATH = '../DB/Animals_db/animals.txt'
TOYS_PATH = '../DB/Toys_db/toys.txt'
CAGES_PATH = '../DB/Cages_db/cages.txt'

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
        food = pickle.load(file)
        return food

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
        return toys


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



if __name__ == '__main__':
    food_list = []
    for _ in range(3):
        toy = ['cat', f'{_}', 'jujo', 5, 5.5]
        toy = create_animal(toy)
        food_list.append(toy)

    save_animals(food_list)
    toys = get_animals_queryset()
    a=5
    animals = get_animals_queryset()
    a =5

    #call other functions to get data from files