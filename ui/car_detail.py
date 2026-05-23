from nicegui import ui
from services.car_service import get_car_by_id


@ui.page("/cars/{car_id}")
def car_detail_page(car_id: int):

    car = get_car_by_id(car_id)

    if not car:
        with ui.card().classes(
            "w-1/2 mx-auto m-8 p-8 shadow-lg"
        ):

            ui.label("Car not found").classes(
                "text-3xl font-bold text-red-600"
            )

            ui.button(
                "Back to Cars",
                on_click=lambda:
                ui.navigate.to("/cars")
            ).props("outline")

        return

    with ui.card().classes(
        "w-1/2 mx-auto m-8 p-8 shadow-lg"
    ):

        ui.label(
            f"{car.brand} {car.model}"
        ).classes(
            "text-4xl font-bold text-blue-700"
        )

        ui.separator()

        ui.label(
            f"Year: {car.year}"
        ).classes("text-xl")

        ui.label(
            f"Kilometres: {car.km:,} km"
        ).classes("text-xl")

        ui.label(
            f"Transmission: {car.trans}"
        ).classes("text-xl")

        ui.label(
            f"Price: CHF {car.price:,.0f}"
        ).classes(
            "text-3xl font-bold text-green-700"
        )

        with ui.row().classes("gap-4 mt-6"):

            ui.button(
                "Back to Cars",
                on_click=lambda:
                ui.navigate.to("/cars")
            ).props("outline")

            ui.button(
                "Edit Car",
                on_click=lambda:
                ui.navigate.to(f"/cars/edit/{car.id}")
            ).props("color=orange")