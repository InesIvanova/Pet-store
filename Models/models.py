from abc import ABC, abstractmethod
from dateutil.parser import parse

class User:
    def __init__(self, first_name, last_name, password, match_pass, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.match_pass = match_pass
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        print(len(phone))
        if not len(phone) == 14:
            raise Exception('Phone must have 14 characters')

        if not (phone[0:4] == '+359'):
            raise Exception('Phone must start with +359')

        self.__phone = phone

    @property
    def match_pass(self):
        return self.__password

    @match_pass.setter
    def match_pass(self, match_pass):
        if not match_pass == self.password:
            raise Exception('Passwords must match')
        self.__match_pass = match_pass


    def check_if_number(self, password):
        return any(i.isdigit() for i in password)

    @property
    def password(self):
        return self.__password


    @password.setter
    def password(self, password):
        length = len(password)

        if length < 6 or length > 15:
            raise Exception('Password should be between 6-15 digits')

        if self.check_if_number(password):
            self.__password = password
        else:
            raise Exception('Password should contains at least one number')



    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        length = len(first_name)

        if length < 3 or length > 20:
            raise Exception('Name should be between 3-20 characters long')
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        length = len(last_name)

        if length < 3 or length > 20:
            raise Exception('Last name should be between 3-20 characters long')
        self.__last_name = last_name


class BasicItem(ABC):
    kinds_list = ['dog', 'cat']
    @abstractmethod
    def __init__(self, id, price, kind):
        self.id = id
        self.price = float(price)
        self.kind = kind

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price must be positive")
        self.__price = price

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        if not kind in self.kinds_list:
            raise Exception('Kind must be valid animal')
        self.__kind = kind


class Cage(BasicItem):
    def __init__(self, id, volume, price, kind):
        BasicItem.__init__(self, id=id, price=price, kind=kind)
        self.volume = float(volume)

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if volume <= 0:
            raise Exception('Volume must be positive')
        self.__volume = volume


class Food(BasicItem):
    def __init__(self, id, price, kind, date_of_validity, kilograms):
        BasicItem.__init__(self, id=id, price=price, kind=kind)
        self.date_of_validity = date_of_validity
        self.kilograms = float(kilograms)

    @property
    def kilograms(self):
        return self.__kilograms

    @kilograms.setter
    def kilograms(self, kilograms):
        if kilograms <= 0:
            raise Exception('Food must be valid kilograms')
        self.__kilograms = kilograms


    @property
    def date_of_validity(self):
        return self.__date_of_validity


    @date_of_validity.setter
    def date_of_validity(self, date_of_validity):
        try:
            datetime_object = datetime = parse(f'{date_of_validity} 22:21:41')
            self.__date_of_validity = datetime_object
        except:
            raise Exception('Data formatting failed')


class Toy(BasicItem):
    def __init__(self, id, price, kind):
        BasicItem.__init__(self, id=id, price=price, kind=kind)


class Animal(ABC):
    @abstractmethod
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = int(age)

    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        if age <= 0:
            raise Exception('Animal age should be valid number')
        self.__age = age


class Dog(Animal):
    def __init__(self, id, name, age, playfulness):
        Animal.__init__(self,id, name, age)
        self.playfulness = float(playfulness)


    @property
    def playfulness(self):
        return self.__playfulness

    @playfulness.setter
    def playfulness(self, playfulness):
        if playfulness <= 0:
            raise Exception("Dog's playfulness should be valid number")


class Cat(Animal):
    def __init__(self, id,  name, age, laziness):
        Animal.__init__(self, id, name, age)
        self.laziness = float(laziness)

    @property
    def laziness(self):
        return self.__laziness

    @laziness.setter
    def laziness(self, laziness):
        if laziness <= 0:
            raise Exception("Cat's laziness should be valid number")
        self.__laziness = laziness


