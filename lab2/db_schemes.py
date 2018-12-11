import datetime

from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CarScheme(Base):
    __tablename__ = "cars"

    name = Column(String)
    color = Column(String)
    model = Column(String)
    car_number = Column(String, primary_key=True)
    price_per_day = Column(Integer)
    has_automatic_transmission = Column(Boolean)

    def __init__ (self,
                  car_number = 'AA0123AA',
                  model = 'sample model',
                  price_per_day = '1000',
                  has_automatic_transmission = False,
                  color = 'transparent',
                  name = 'sample car'):
        self.name = name
        self.color = color
        self.model = model
        self.car_number = car_number
        self.price_per_day = price_per_day
        self.has_automatic_transmission = has_automatic_transmission

class RenterScheme(Base):
    __tablename__ = "renters"
    first_name = Column(String)
    last_name = Column(String)
    driver_license = Column(String, primary_key=True)

    def __init__ (self, first_name = 'Joe', last_name = "Doe", driver_license = 'ABC012345'):
        self.first_name = first_name
        self.last_name = last_name
        self.driver_license = driver_license

class RentingListScheme(Base):
    __tablename__ = "renting_list"
    driver_license = Column(String)
    car_number = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)

    def __init__ (self,
                  driver_license = 'ABC012345',
                  car_number = 'AA0123AA',
                  date = datetime.datetime.now()):
        self.driver_license = driver_license
        self.car_number = car_number
        self.date = date