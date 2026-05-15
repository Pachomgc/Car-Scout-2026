from domain.car import Car
from data_access.database import get_session


class CarDAO:

    @staticmethod
    def get_all():
        with get_session() as session:
            return session.query(Car).all()

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