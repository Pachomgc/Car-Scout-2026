from sqlalchemy import Column, Float, Integer, String
from data_access.database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    km = Column(Integer, nullable=False)
    trans = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)