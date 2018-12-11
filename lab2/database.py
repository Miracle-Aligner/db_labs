import random

from db_schemes import CarScheme
from db_schemes import RenterScheme
from db_schemes import RentingListScheme

from db_schemes import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Database():

    _engine_ = create_engine('postgresql://max:100103@localhost:5432/db_lab1')
    _Session_ = sessionmaker(bind=_engine_)

    def __init__(self, host="localhost", database="db_lab1", user="max", password="100103"):
        _engine_ = create_engine('postgresql://max:100103@localhost:5432/db_lab1')
        _Session_ = sessionmaker(bind=_engine_)
        Base.metadata.create_all(_engine_)
        self._session_ = _Session_()

    def close(self):
        self._session_.close()

    #def insert_renting_info(vendor_name):

    def get_car(self, car_number):
        return self._session_.query(CarScheme).get(car_number)

    def insert_car(self, car_scheme: CarScheme):
        self._session_.add(car_scheme)
        self._session_.commit()

    def insert_cars_list(self, car_scheme_list):
        for car_sheme in car_scheme_list:
            self.insert_car(car_sheme)

    def update_car(self, car_scheme: CarScheme):
        self.insert_car(car_scheme)

    def delete_car(self, car_number):
        self._session_.query(CarScheme).filter_by(car_number = car_number).delete()
        self._session_.commit()

    def get_renter(self, driver_license):
        return self._session_.query(RenterScheme).get(driver_license)

    def insert_renter(self, renter_scheme: RenterScheme):
        self._session_.add(renter_scheme)
        self._session_.commit()

    def update_renter(self, renter_scheme: RenterScheme):
        self.insert_department(renter_scheme)

    def delete_renter(self, driver_license):
        self._session_.query(RenterScheme).filter_by(driver_license = driver_license).delete()
        self._session_.commit()

    def insert_renting_list_entity(self, renting_list_scheme: RentingListScheme):
        self._session_.add(renting_list_scheme)
        self._session_.commit()

    def update_renting_list_entity(self, renting_list_scheme: RentingListScheme):
        self.insert_worker_card(renting_list_scheme)

    def delete_renting_list_entity(self, car_number, date):
        self._session_.query(RentingListScheme).filter(car_number == car_number, date == date).delete()
        self._session_.commit()

    def get_renting_list_entity(self, car_number, date):
        return self._session_.query(RentingListScheme).get((car_number, date))

    def get_table_string(self, table_name):
        return self._session_.query(Base.metadata.tables[table_name]).all()

    def search_by_transmission(self, has_automatic_transmission):
        res = self._session_.query(RentingListScheme) \
            .filter(RentingListScheme.has_automatic_transmission == has_automatic_transmission) \
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def search_by_date_range(self, left_boundary, right_boundary):
        res = self._session_.query(RentingListScheme) \
            .filter(RentingListScheme.date >= left_boundary.date(),
                    RentingListScheme.date < right_boundary.date()) \
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def search_by_transmission_and_date_range(self, has_automatic_transmission, left_boundary, right_boundary):
        res = self._session_.query(RentingListScheme) \
            .filter(RentingListScheme.car_number == CarScheme.car_number,
                    RentingListScheme.driver_license == RenterScheme.driver_license) \
            .filter(CarScheme.has_automatic_transmission == has_automatic_transmission,
                    RentingListScheme.data >= left_boundary.date(),
                    RentingListScheme.data < right_boundary.date()) \
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def search_by_word_not_belong(self, word):
        sql = f"""SELECT car_number, name, model FROM cars WHERE to_tsvector(name) @@ to_tsquery('!{word}');"""
        res = self._session_.execute(sql).fetchall()

        strings = ""
        for row in res:
            strings += str(dict(row.items())) + "\n"
        return strings

    def search_by_phrase(self, phrase):
        sql = f"""SELECT * FROM renting_list 
                  JOIN renters USING(driver_license) 
                  JOIN cars USING (car_number) 
                  WHERE to_tsvector(model) @@ phraseto_tsquery('{phrase}');"""
        res = self._engine_.execute(sql).fetchall()

        strings = ""
        for row in res:
            strings += str(dict(row.items())) + "\n"
        return strings

    #def get_random_car_number(self):

    def get_random_driver_license(self):
        rand_index = random.randint(0, self._session_.query(RenterScheme).count())
        return self._session_.query(RenterScheme)[rand_index]

    def get_random_car_number(self):
        rand_index = random.randint(0, self._session_.query(CarScheme).count())
        return self._session_.query(CarScheme)[rand_index]

