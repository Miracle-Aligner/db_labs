import names
import string
import random
import datetime
import xml.etree.ElementTree as ET

class Car():
    name = ""
    model = []

    def __init__ (self, name = "default name", model="default model"):
        self.name = name
        self.model.append(model)

    def addName(self, name):
        self.name = name

    def addModel(self, model):
        self.model.append(model)

class Randomize():
    cars_array = []

    def __init__(self):
        Randomize.parseCarsXml()

    @classmethod
    def parseCarsXml(cls):
        tree = ET.parse('cars.xml')

        carlist = tree.getroot()

        i = -1
        for car in carlist:
            for subelem in car:
                if subelem.tag == 'carname':
                    i += 1
                    cls.cars_array.append(Car(subelem.text))

                elif subelem.tag == 'carmodellist':
                    for models in subelem:
                        cls.cars_array[i].addModel(models.text)
    def car(self):
        randIndex = random.randint(0, len(Randomize.cars_array))
        return Randomize.cars_array[randIndex]

    def carModel(self, car):
        randIndex = random.randint(0, len(car.model))
        return car.model[randIndex]

    def carNumber(self):
        number = ""
        string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number += random.choice(string.letters)
        number += random.choice(string.letters)
        for x in range(0, 4):
            number += str(random.randint(0, 9))
        number += random.choice(string.letters)
        number += random.choice(string.letters)
        return number

    def driverLicense(self):
        number = ""
        string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for x in range(0, 3):
            number += random.choice(string.letters)
        for x in range(0, 6):
            number += str(random.randint(0, 9))
        return number

    def transmission(self):
        return bool(random.getrandbits(1))

    def price(self):
        return random.randint(1000, 50000)

    def color(self):
        colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
        return random.choice(colors)

    def firstname(self):
        return names.get_first_name()

    def lastname(self):
        return names.get_last_name()

    def date(self):
        return datetime.datetime(random.randint(2000, 2018), random.randint(1, 12), random.randint(1, 30))