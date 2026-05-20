from domain.car import Car
from data_access.car_dao import CarDAO


def add_car(brand, model, year, km, trans, price):
    car = Car(
        brand=brand,
        model=model,
        year=year,
        km=km,
        trans=trans,
        price=price,
    )

    CarDAO.add(car)


def get_cars():
    return CarDAO.get_all()


def remove_car(car_id):
    CarDAO.delete(car_id)


def get_all_cars():
    return CarDAO.get_all()


def delete_car(car_id):
    CarDAO.delete(car_id)

def search_cars(search_text):
    return CarDAO.search(search_text)

def get_car_by_id(car_id):
    return CarDAO.get_by_id(car_id)

def update_car(car_id, brand, model, year, km, trans, price):
    CarDAO.update(car_id, brand, model, year, km, trans, price)