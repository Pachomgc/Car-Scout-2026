
from database import Car, get_session


def get_all_cars() -> list[Car]:
 
    with get_session() as session:
        cars = session.query(Car).order_by(Car.brand, Car.model).all()
        session.expunge_all()   
        return cars


def add_car(brand: str, model: str, year: int, km: int,
            trans: str, price: float) -> Car:
 
    with get_session() as session:
        car = Car(brand=brand, model=model, year=year,
                  km=km, trans=trans, price=price)
        session.add(car)
        session.commit()
        session.refresh(car)
        session.expunge(car)
        return car


def delete_car(car_id: int) -> None:

    with get_session() as session:
        car = session.get(Car, car_id)
        if car:
            session.delete(car)
            session.commit()


def update_car(car_id: int, brand: str, model: str, year: int,
               km: int, trans: str, price: float) -> Car | None:
  
    with get_session() as session:
        car = session.get(Car, car_id)
        if not car:
            return None
        car.brand = brand
        car.model = model
        car.year  = year
        car.km    = km
        car.trans = trans
        car.price = price
        session.commit()
        session.refresh(car)
        session.expunge(car)
        return car