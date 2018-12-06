import random

import psycopg2
import pandas as pd
import psycopg2.extras

class Database():
    _db_connection = psycopg2.connect(host="localhost",database="db_lab1", user="max", password="100103")
    _db_cur = _db_connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

    def __init__(self, host="localhost", database="db_lab1", user="max", password="100103"):
        _db_connection = psycopg2.connect(host="localhost",database="db_lab1", user="max", password="100103")
        _db_cur = self._db_connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def close(self):
        self._db_connection.close()

    #def insert_renting_info(vendor_name):

    def get_car(self, car_number):
        Database._db_cur.execute(f"""SELECT * FROM cars WHERE car_number = '{car_number}'""")
        return Database._db_cur.fetchone()

    def insert_car(self, car_scheme):
        sql = "INSERT INTO cars(car_number, model, price_per_day, has_automatic_transmission, color, name) " \
              "VALUES(%s, %s, %s, %s, %s, %s);"
        Database._db_cur.execute(sql, (car_scheme.car_number, car_scheme.model, car_scheme.price_per_day,
                                       car_scheme.has_automatic_transmission, car_scheme.color, car_scheme.name))
        Database._db_connection.commit()

    def insert_cars_list(self, car_scheme_list):
        for car_sheme in car_scheme_list:
            self.insert_car(car_sheme)

    def update_car(self, car_scheme):
        sql = """ UPDATE cars
                    SET model = %s, 
                    price_per_day = %s, 
                    has_automatic_transmission = %s, 
                    color = %s, 
                    name = %s
                    WHERE car_number = %s"""
        Database._db_cur.execute(sql, (car_scheme.model, car_scheme.price_per_day, car_scheme.has_automatic_transmission,
                                       car_scheme.color, car_scheme.name, car_scheme.car_number))
        Database._db_connection.commit()

    def delete_car(self, car_number):
        Database._db_cur.execute(f"""DELETE FROM cars WHERE car_number = '{car_number}'""")
        Database._db_connection.commit()

    def get_renter(self, driver_license):
        Database._db_cur.execute(f"""SELECT * FROM renters WHERE driver_license = '{driver_license}'""")
        return Database._db_cur.fetchone()

    def insert_renter(self, renter_scheme):
        sql = "INSERT INTO renters(first_name, driver_license, last_name) " \
              "VALUES(%s, %s, %s);"
        Database._db_cur.execute(sql, (renter_scheme.first_name, renter_scheme.driver_license, renter_scheme.last_name))
        Database._db_connection.commit()

    def update_renter(self, renter_scheme):
        sql = """ UPDATE renters
                    SET first_name = %s, 
                    last_name = %s
                    WHERE driver_license = %s"""
        Database._db_cur.execute(sql, (renter_scheme.first_name, renter_scheme.last_name, renter_scheme.driver_license))
        Database._db_connection.commit()

    def delete_renter(self, driver_license):
        Database._db_cur.execute(f"""DELETE FROM renters WHERE driver_license = '{driver_license}'""")
        Database._db_connection.commit()

    def insert_renting_list_entity(self, renting_list_scheme):
        sql = "INSERT INTO renting_list(car_number, date, driver_license) " \
              "VALUES(%s, %s, %s);"
        Database._db_cur.execute(sql, (renting_list_scheme.car_number,
                                       renting_list_scheme.date,
                                       renting_list_scheme.driver_license))
        Database._db_connection.commit()

    def update_renting_list_entity(self, renting_list_scheme):
        sql = """ UPDATE renting_list
                    SET driver_license = %s, 
                    WHERE car_number = %s AND date = %s"""
        Database._db_cur.execute(sql, (renting_list_scheme.first_name, renting_list_scheme.last_name, renting_list_scheme.driver_license))
        Database._db_connection.commit()

    def delete_renting_list_entity(self, car_number, date):
        Database._db_cur.execute(f"""DELETE FROM renting_list WHERE car_number = '{car_number}' AND date = '{date}'""")
        Database._db_connection.commit()

    def get_renting_list_entity(self, car_number, date):
        Database._db_cur.execute(f"""SELECT * FROM renting_list WHERE car_number = '{car_number}' AND date = '{date}'""")
        return Database._db_cur.fetchone()

    def get_table_string(self, table_name):
        sql = "SELECT * FROM {0}".format(table_name)
        return pd.read_sql(sql, self._db_connection)

    def search_by_transmission(self, has_automatic_transmission):
        sql = f"""SELECT * FROM cars WHERE has_automatic_transmission = 
                                '{has_automatic_transmission}'"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_date_range(self, left_boundary, right_boundary):
        sql = f"""SELECT * FROM renting_list WHERE date >= 
                                '{left_boundary}' AND date < '{right_boundary}'"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_transmission_and_date_range(self, has_automatic_transmission, left_boundary, right_boundary):
        #"SELECT * FROM renting_list AS r_l JOIN cars AS ca ON r_l.car_number = ca.car_number JOIN renters AS r ON r.driver_license = r_l.driver_license"
        sql = f"""SELECT * FROM renting_list JOIN cars USING (car_number) JOIN renters USING(driver_license) 
        WHERE has_automatic_transmission = '{has_automatic_transmission}' AND date >= 
                                '{left_boundary}' AND date < '{right_boundary}'"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_word_not_belong(self, word):
        sql = f"""SELECT car_number, name, model FROM cars WHERE to_tsvector(name) @@ to_tsquery('!{word}');"""
        return pd.read_sql(sql, self._db_connection)

    def search_by_phrase(self, phrase):
        sql = f"""SELECT * FROM renting_list 
                  JOIN renters USING(driver_license) 
                  JOIN cars USING (car_number) 
                  WHERE to_tsvector(model) @@ phraseto_tsquery('{phrase}');"""
        return pd.read_sql(sql, self._db_connection)

    #def get_random_car_number(self):

    def get_random_driver_license(self):
        Database._db_cur.execute("SELECT driver_license FROM renters")
        driver_license_arr = Database._db_cur.fetchall()
        rand_index = random.randint(0, (len(driver_license_arr) - 1))
        return driver_license_arr[rand_index]

    def get_random_car_number(self):
        Database._db_cur.execute("SELECT car_number FROM cars")
        car_number_arr = Database._db_cur.fetchall()
        rand_index = random.randint(0, (len(car_number_arr) - 1))
        return car_number_arr[rand_index]


