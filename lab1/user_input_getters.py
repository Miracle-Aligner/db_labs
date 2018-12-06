from database import Database
from get_char import switch
from check_input import CheckInput
from db_schemes import CarScheme
from db_schemes import RenterScheme
from db_schemes import RentingListScheme

db = Database()
class UserInput:
    def read_car_input(self):
        carEntity = CarScheme()
        carEntity.name = input("enter car name: ")
        carEntity.color = input("enter car color: ")
        carEntity.model = input("enter car model: ")
        carEntity.car_number = input("enter car number: ")
        while not CheckInput.test_car_number(carEntity.car_number):
            carEntity.car_number = input("Wrong input!\nTry again: ")

        carEntity.price_per_day = input("enter car's price per day: ")
        while not CheckInput.test_price(carEntity.price_per_day):
            carEntity.price_per_day = input("Wrong input!\nTry again: ")

        carEntity.has_automatic_transmission = input("enter car if car has automatic transmision (True/False): ")
        while carEntity.has_automatic_transmission != "True" and carEntity.has_automatic_transmission != "False":
            carEntity.has_automatic_transmission = input("Wrong input!\nTry again: ")

        return carEntity

    def read_renter_input(self):
        renterEntity = RenterScheme()
        renterEntity.first_name = input("enter renter first name: ")
        renterEntity.last_name = input("enter renter last name: ")
        renterEntity.driver_license = input("enter renter driver license: ")
        while not CheckInput.test_driver_license(renterEntity.driver_license):
            renterEntity.driver_license = input("Wrong input!\nTry again: ")

        return renterEntity

    def read_renter_list_entity_input(self):
        renterListEntity = RentingListScheme()
        renterListEntity.car_number = input("enter car number: ")
        while not CheckInput.test_car_number(renterListEntity.car_number):
            renterListEntity.car_number = input("Wrong input!\nTry again: ")

        while not CheckInput.check_car_existence(renterListEntity.car_number):
            car_entity = CarScheme()
            input_str = ""
            input_str = input("There is no such car!\nWanna add?\n(y/n): ")
            for case in switch(input_str):
                if case('y'):
                    car_entity = self.read_car_input()
                    renterListEntity.car_number = car_entity.car_number
                    db.insert_car(car_entity)
                    break
                if case('n'):
                    print("can't insert renting list entity")
                    return
                else:
                    print("____________________")
                    print("no such option, try again!")

        renterListEntity.driver_license = input("enter renter driver license: ")
        while not CheckInput.test_driver_license(renterListEntity.driver_license):
            renterListEntity.driver_license = input("Wrong input!\nTry again: ")

        while not CheckInput.check_renter_existence(renterListEntity.driver_license):
            renter_entity = RenterScheme()
            input_str = ""
            input_str = input("There is no such renter!\nWanna add?\n(y/n): ")
            for case in switch(input_str):
                if case('y'):
                    renter_entity = self.read_renter_input()
                    renterListEntity.driver_license = renter_entity.driver_license
                    db.insert_renter(renter_entity)
                    break
                if case('n'):
                    print("can't insert renting list entity")
                    return
                else:
                    print("____________________")
                    print("no such option, try again!")

        renterListEntity.date = input("enter renting date(format: year-mm-dd): ")
        while not CheckInput.test_date(renterListEntity.date):
            renterListEntity.date = input("Wrong input!\nTry again: ")

        return renterListEntity

    def get_car_number_input(self):
        car_number = input("enter car number to delete: ")
        while not CheckInput.test_car_number(car_number):
            car_number = input("Wrong input!\nTry again: ")
        return car_number

    def get_boolean(self):
        has_automatic_transmission = input("enter car if car has automatic transmision (True/False): ")
        while has_automatic_transmission != "True" and has_automatic_transmission != "False":
            has_automatic_transmission = input("Wrong input!\nTry again: ")

        return has_automatic_transmission

    def get_date(self):
        date = input("enter date(format: year-mm-dd): ")
        while not CheckInput.test_date(date):
            date = input("Wrong input!\nTry again: ")
        return date


    def read_car_update_input(self):
        carEntity = CarScheme()
        carEntity.car_number = input("enter car number: ")
        while not CheckInput.test_car_number(carEntity.car_number):
            carEntity.car_number = input("Wrong input!\nTry again: ")
        if CheckInput.check_car_existence(carEntity.car_number):
            carEntity.name = input("enter new car name: ")
            carEntity.color = input("enter new car color: ")
            carEntity.model = input("enter new car model: ")
            carEntity.price_per_day = input("enter new car's price per day: ")
            while not CheckInput.test_price(carEntity.price_per_day):
                carEntity.price_per_day = input("Wrong input!\nTry again: ")

            carEntity.has_automatic_transmission = input("enter if new car has automatic transmision (True/False): ")
            while carEntity.has_automatic_transmission != "True" and carEntity.has_automatic_transmission != "False":
                carEntity.has_automatic_transmission = input("Wrong input!\nTry again: ")

            return carEntity
        else:
            print("There is no such car in db!")
            return None


    def read_renter_update_input(self):
        renterEntity = RenterScheme()
        renterEntity.driver_license = input("enter renter driver license: ")
        while not CheckInput.test_driver_license(renterEntity.driver_license):
            renterEntity.driver_license = input("Wrong input!\nTry again: ")
        if CheckInput.check_renter_existence(renterEntity.driver_license):
            renterEntity.first_name = input("enter new renter first name: ")
            renterEntity.last_name = input("enter new renter last name: ")
            return renterEntity
        else:
            print("There is no such renter in db!")
            return None


    def read_renter_list_entity_update_input(self):
        renterListEntity = RentingListScheme()
        renterListEntity.car_number = input("enter car number: ")
        while not CheckInput.test_car_number(renterListEntity.car_number):
            renterListEntity.car_number = input("Wrong input!\nTry again: ")

        renterListEntity.date = input("enter renting date(format: year-mm-dd): ")
        while not CheckInput.test_date(renterListEntity.date):
            renterListEntity.date = input("Wrong input!\nTry again: ")
        if CheckInput.check_renting_list_entity_existence(renterListEntity.car_number, renterListEntity.date):
            renterListEntity.driver_license = input("enter renter driver license: ")
            while not CheckInput.test_driver_license(renterListEntity.driver_license):
                renterListEntity.driver_license = input("Wrong input!\nTry again: ")

            while not CheckInput.check_renter_existence(renterListEntity.driver_license):
                renter_entity = RenterScheme()
                input_str = ""
                input_str = input("There is no such renter!\nWanna add?\n(y/n): ")
                for case in switch(input_str):
                    if case('y'):
                        renter_entity = self.read_renter_input()
                        renterListEntity.driver_license = renter_entity.driver_license
                        db.insert_renter(renter_entity)
                        break
                    if case('n'):
                        print("can't insert renting list entity")
                        return
                    else:
                        print("____________________")
                        print("no such option, try again!")
        else:
            print("There's no such renting list entity")
            return None

        return renterListEntity
