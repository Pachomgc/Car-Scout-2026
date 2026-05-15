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