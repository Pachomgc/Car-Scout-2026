from nicegui import ui
from services.car_service import get_car_by_id


@ui.page("/cars/{car_id}")
def car_detail_page(car_id: int):

    car = get_car_by_id(car_id)

    if not car:
        ui.label("Car not found")
        return

    with ui.column().classes("m-8 gap-4"):

        ui.label(f"{car.brand} {car.model}") \
            .classes("text-4xl font-bold")

        ui.separator()

        ui.label(f"Year: {car.year}")
        ui.label(f"Kilometres: {car.km:,} km")
        ui.label(f"Transmission: {car.trans}")
        ui.label(f"Price: CHF {car.price:,.0f}") \
            .classes("text-2xl text-green")

        ui.button(
            "Back to Cars",
            on_click=lambda: ui.navigate.to("/cars")
        )