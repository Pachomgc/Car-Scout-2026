from nicegui import ui

from services.car_service import (
    get_car_by_id,
    update_car,
)


@ui.page("/cars/edit/{car_id}")
def edit_car_page(car_id: int):

    car = get_car_by_id(car_id)

    if not car:
        with ui.column().classes("w-1/2 mx-auto m-8 gap-4"):
            ui.label("Car not found").classes("text-3xl font-bold text-red-600")
            ui.button("Back to Cars", on_click=lambda: ui.navigate.to("/cars")).props("outline")
        return

    with ui.column().classes("w-1/2 mx-auto m-8 gap-4"):

        ui.label("Edit Car").classes("text-4xl font-bold text-orange-600")

        brand = ui.input("Brand", value=car.brand).classes("w-full")
        model = ui.input("Model", value=car.model).classes("w-full")
        year = ui.number("Year", value=car.year).classes("w-full")
        km = ui.number("Kilometres", value=car.km).classes("w-full")
        trans = ui.input("Transmission", value=car.trans).classes("w-full")
        price = ui.number("Price", value=car.price).classes("w-full")

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

            ui.notify("Car updated successfully")
            ui.navigate.to("/cars")

        with ui.row().classes("gap-4 mt-4"):
            ui.button("Save Changes", on_click=save).props("color=orange")
            ui.button("Back", on_click=lambda: ui.navigate.to("/cars")).props("outline")