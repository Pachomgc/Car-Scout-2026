import csv
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Session


DATABASE_URL = "sqlite:///cars.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase):
    pass




class Car(Base):
    

    __tablename__ = "cars"

    id       = Column(Integer, primary_key=True, autoincrement=True)
    brand    = Column(String(50),  nullable=False)
    model    = Column(String(50),  nullable=False)
    year     = Column(Integer,     nullable=False)
    km       = Column(Integer,     nullable=False)
    trans    = Column(String(20),  nullable=False)  
    price    = Column(Float,       nullable=False)

    def __repr__(self) -> str:
        return f"<Car {self.brand} {self.model} ({self.year}) CHF {self.price}>"




def get_session() -> Session:
   
    return Session(engine)


def init_db() -> None:
    
    Base.metadata.create_all(engine)
    print("Database initialised.")


def seed_from_csv(csv_path: str) -> None:
    
    with get_session() as session:
       
        if session.query(Car).count() > 0:
            return

        if not os.path.exists(csv_path):
            print(f"CSV file '{csv_path}' not found — skipping seed.")
            return

        inserted = 0
        with open(csv_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 6:
                    continue  
                b, m, y, km, t, p = parts
                car = Car(
                    brand=b.strip(),
                    model=m.strip(),
                    year=int(y.strip()),
                    km=int(km.strip()),
                    trans=t.strip().lower(),
                    price=float(p.strip()),
                )
                session.add(car)
                inserted += 1
            session.commit()

        print(f"Seeded {inserted} cars from '{csv_path}'.")