import datetime

from database import Database

class CheckInput:

    def test_car_number(car_number):
        car_number_arr = list(car_number)
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if car_number_arr[0] not in letters:
            return False
        elif car_number_arr[1] not in letters:
            return False
        elif car_number_arr[6] not in letters:
            return False
        elif car_number_arr[7] not in letters:
            return False
        for x in range(0, 4):
            if not car_number_arr[2 + x].isnumeric():
                return False

        return True

    def test_price(price):
        try:
            price_num = float(price)
            if price_num >= 0:
                return True
            return False
        except ValueError:
            return False

    def test_driver_license(d_l):
        driver_license_arr = list(d_l)
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if driver_license_arr[0] not in letters:
            return False
        elif driver_license_arr[1] not in letters:
            return False
        elif driver_license_arr[2] not in letters:
            return False
        for x in range(0, 6):
            if not driver_license_arr[3 + x].isnumeric():
                return False
        return True

    def test_date(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def check_car_existence(car_number):
        db = Database()
        if(db.get_car(car_number) == None):
            return False
        return True


    def check_renter_existence(driver_license):
        db = Database()
        if(db.get_renter(driver_license) == None):
            return False
        return True

    def check_renting_list_entity_existence(car_number, date):
        db = Database()
        if(db.get_renting_list_entity(car_number, date) == None):
            return False
        return True