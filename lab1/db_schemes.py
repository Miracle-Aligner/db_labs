import datetime

class CarScheme:
    name = "sample car"
    color = "transparent"
    model = "sample model"
    car_number = "AA0123AA"
    price_per_day = "1000"
    has_automatic_transmission = "False"

    def __init__ (self,
                  car_number = 'AA0123AA',
                  model = 'sample model',
                  price_per_day = '1000',
                  has_automatic_transmission = 'False',
                  color = 'transparent',
                  name = 'sample car'):
        self.name = name
        self.color = color
        self.model = model
        self.car_number = car_number
        self.price_per_day = price_per_day
        self.has_automatic_transmission = has_automatic_transmission

class RenterScheme:
    first_name = "Joe"
    last_name = "Doe"
    driver_license = "ABC012345"

    def __init__ (self, first_name = 'Joe', last_name = "Doe", driver_license = 'ABC012345'):
        self.first_name = first_name
        self.last_name = last_name
        self.driver_license = driver_license

class RentingListScheme:
    driver_license = "ABC012345"
    car_number = "AA0123AA"
    date = datetime.datetime.now()

    def __init__ (self, driver_license = 'ABC012345', car_number = 'AA0123AA', date = datetime.datetime.now()):
        self.driver_license = driver_license
        self.car_number = car_number
        self.date = date