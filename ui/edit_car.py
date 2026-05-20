from nicegui import ui

from services.car_service import (
    get_car_by_id,
    update_car,
)


@ui.page("/cars/edit/{car_id}")
def edit_car_page(car_id: int):

    car = get_car_by_id(car_id)

    if not car:
        ui.label("Car not found")
        return

    brand = ui.input("Brand", value=car.brand)
    model = ui.input("Model", value=car.model)
    year = ui.number("Year", value=car.year)
    km = ui.number("Kilometres", value=car.km)
    trans = ui.input("Transmission", value=car.trans)
    price = ui.number("Price", value=car.price)

    def save():

        update_car(
            car_id,
            brand.value,
            model.value,
            int(year.value),
            int(km.value),
            trans.value,
            float(price.value),
        )

        ui.notify("Car updated")
        ui.navigate.to("/cars")

    ui.button("Save", on_click=save)