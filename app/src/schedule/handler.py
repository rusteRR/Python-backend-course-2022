import sys

from database import db_flights


def get_possible_options(city_from: str, city_to: str, date: str):
    tokens = [x[0].split() for x in db_flights.values()]
    return [" ".join(line) for line in tokens if line[0] == date and    
            line[1] == city_from and line[2] == city_to]


def parse_query(date: str, city_from: str, city_to: str):
    possible_options = dict()
    counter = 1
    try:
        options = get_possible_options(city_from, city_to, date)
        for element in options:
            possible_options.update({counter: element})
            counter += 1

    except OSError:
        return  "Could not open database"
    return {"Possible options" : possible_options}
    