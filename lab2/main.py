#!/usr/bin/env python
# encoding: utf-8
import string

import datetime

from get_char import switch
from database import Database
from check_input import CheckInput
from user_input_getters import UserInput
from randomize import Randomize
from fill_db import RandomFillDB


db = Database()
user_input = UserInput()

def delete_entity(db_name):
    if db_name == "cars":
        car_number = user_input.get_car_number_input()

        if not CheckInput.check_car_existence(car_number):
            print("There is no such car in db!\n")
        else:
            db.delete_car(car_number)

    elif db_name == "renters":
        driver_license = input("enter renter driver license: ")
        while not CheckInput.test_driver_license(driver_license):
            driver_license = input("Wrong input!\nTry again: ")

        if not CheckInput.check_renter_existence(driver_license):
            print("There is no such renter in db!\n")
        else:
            db.delete_renter(driver_license)

    elif db_name == "renting_list":
        car_number = user_input.get_car_number_input()
        date = input("enter renting date(format: year-mm-dd): ")
        while not CheckInput.test_date(date):
            date = input("Wrong input!\nTry again: ")

        if not CheckInput.check_renting_list_entity_existence(car_number, date) :
            print("There is no such renting list entity in db!\n")

        else:
            db.delete_renting_list_entity(car_number, date)

def update_entity(db_name):
    if db_name == "cars":
        car_entity = user_input.read_car_update_input()
        if (car_entity != None):
            db.update_car(car_entity)
            return True

    elif db_name == "renters":
        renter_entity = user_input.read_renter_update_input()
        if (renter_entity != None):
            db.update_renter(renter_entity)
            return True

    elif db_name == "renting_list":
        renting_list_entity = user_input.read_renter_list_entity_update_input()
        if (renting_list_entity != None):
            db.update_renting_list_entity(renting_list_entity)
            return True

    return False

def add_entity(db_name):
    if db_name == "cars":
        db.insert_car(user_input.read_car_input())

    elif db_name == "renters":
        db.insert_renter(user_input.read_renter_input())

    elif db_name == "renting_list":
        db.insert_renting_list_entity(user_input.read_renter_list_entity_input())

def fill_rand(db_name):
    input_str = input("INPUT INTEGER NUMBER OF ENTITIES TO MAKE: ")
    random_fill = RandomFillDB()
    if db_name == "cars":
        random_fill.add_n_cars(int(input_str))

    elif db_name == "renters":
        random_fill.add_n_renters(int(input_str))

    elif db_name == "renting_list":
        random_fill.add_n_renting_list_entities(int(input_str))

def get_db_name():
    while 1:
        switchVariable = input("CHOOSE DB BY ITS NUMBER\npossible are: \n\t1 - cars, \n\t2 - renters, \n\t3 - renting_list, "
                               "\n\tb - go to main menu\nType here and press enter: ")
        for case in switch(switchVariable):
            if case('1'):
                return "cars"
            if case('2'):
                return "renters"
            if case('3'):
                return "renting_list"
            if case('b'):
                break
            else:
                print("____________________")
                print("no such option, try again!")

def search_in_db(criteria):
    if criteria == "by_date_range":
        date1 = user_input.get_date()
        date2 = user_input.get_date()
        print(db.search_by_date_range(date1, date2))

    elif criteria == "by_transmission":
        transmission = user_input.get_boolean()
        print("\nSearch result:")
        print(db.search_by_transmission(transmission))

    elif criteria == "by_date_range_and_transmission":
        date1 = user_input.get_date()
        date2 = user_input.get_date()
        transmission = user_input.get_boolean()
        print(db.search_by_transmission_and_date_range(transmission, date1, date2))


    elif criteria == "by_word_not_belong":
        name = input("enter car name: ")
        print(db.search_by_word_not_belong(name))

    elif criteria == "by_whole_sentence":
        name = input("enter car model: ")
        print(db.search_by_phrase(name))

def get_criteria():
    while 1:
        switchVariable = input("CHOOSE SEARCH CRITERIA BY ITS NUMBER\npossible are: \n\t1 - by_date_range, \n\t2 - "
                               "by_transmission, \n\t3 - by_date_range_and_transmission, "
                               "\n\t4 - by_word_not_belong (car's name), \n\t5 - by_whole_sentence (car's model)\n\tb - go to main menu\nType here and press enter: ")
        for case in switch(switchVariable):
            if case('1'):
                return "by_date_range"
            if case('2'):
                return "by_transmission"
            if case('3'):
                return "by_date_range_and_transmission"
            if case('4'):
                return "by_word_not_belong"
            if case('5'):
                return "by_whole_sentence"
            if case('b'):
                break
            else:
                print("____________________")
                print("no such option, try again!")

while 1:
    switchVariable = input("CHOOSE COMMAND BY ITS NUMBER\npossible are: \n\t1 - add_entity, \n\t2 - fill_rand, \n\t3 "
                           "- update_entity\n\t4 - delete_entity,\n\t5 - search_in_db, \n\tq - quit\nType here and press enter: ")
    for case in switch(switchVariable):
        if case('1'):
            db_name = get_db_name()
            print("Table before insertion:\n",  db.get_table_string(db_name))
            add_entity(db_name)
            print("Table after insertion:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('2'):
            db_name = get_db_name()
            print("Table before insertion:\n", db.get_table_string(db_name))
            fill_rand(db_name)
            print("Table after insertion:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('3'):
            db_name = get_db_name()
            print("Table before editing:\n", db.get_table_string(db_name))
            if update_entity(db_name):
                print("Table after editing:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('4'):
            db_name = get_db_name()
            print("Table before delete:\n", db.get_table_string(db_name))
            delete_entity(db_name)
            print("Table after delete:\n", db.get_table_string(db_name))
            print("____________________")
            break
        if case('5'):
            criteria = get_criteria()
            search_in_db(criteria)
            print("____________________")
            break
        if case('q'):
            break
        else:
            print("____________________")
            print("no such option, try again!")
        
    if switchVariable == 'q':
        break
