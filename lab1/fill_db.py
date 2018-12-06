from database import Database
from randomize import Randomize
from db_schemes import CarScheme
from db_schemes import RenterScheme
from db_schemes import RentingListScheme


class RandomFillDB:

    db = Database()

    def add_n_cars(self, n):
        for x in range(0, n):
            self.add_car()

    def add_car(self):
        rand_vals = Randomize()
        car = rand_vals.car()
        self.db.insert_car(
            CarScheme(
                rand_vals.carNumber(),
                rand_vals.carModel(car),
                str(rand_vals.price()),
                str(rand_vals.transmission()),
                rand_vals.color(),
                car.name))
    def add_n_renters(self, n):
        for x in range(0, n):
            self.add_renter()

    def add_renter(self):
        rand_vals = Randomize()
        car = rand_vals.car()
        self.db.insert_renter(
            RenterScheme(
                rand_vals.firstname(),
                rand_vals.lastname(),
                rand_vals.driverLicense()))

    def add_n_renting_list_entities(self, n):
        for x in range(0, n):
            self.add_renting_list_entity()

    def add_renting_list_entity(self):
        rand_vals = Randomize()
        car = rand_vals.car()
        self.db.insert_renting_list_entity(
            RentingListScheme(
                self.db.get_random_driver_license().pop(0),
                self.db.get_random_car_number().pop(0),
                rand_vals.date()))