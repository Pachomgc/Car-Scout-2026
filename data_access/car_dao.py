from domain.car import Car
from data_access.database import get_session


class CarDAO:

    @staticmethod
    def get_all():
        with get_session() as session:
            return session.query(Car).all()

    @staticmethod
    def search(search_text: str):
        with get_session() as session:
            return session.query(Car).filter(
                (Car.brand.ilike(f"%{search_text}%")) |
                (Car.model.ilike(f"%{search_text}%"))
            ).all()

    @staticmethod
    def get_by_id(car_id: int):
        with get_session() as session:
            return session.query(Car).filter(Car.id == car_id).first()
    
    @staticmethod
    def update(car_id, brand, model, year, km, trans, price):

        with get_session() as session:

            car = session.query(Car).filter(
                Car.id == car_id
            ).first()

            if car:
                car.brand = brand
                car.model = model
                car.year = year
                car.km = km
                car.trans = trans
                car.price = price

                session.commit()

    @staticmethod
    def add(car: Car):
        with get_session() as session:
            session.add(car)
            session.commit()

    @staticmethod
    def delete(car_id: int):
        with get_session() as session:
            car = session.query(Car).filter(Car.id == car_id).first()

            if car:
                session.delete(car)
                session.commit()