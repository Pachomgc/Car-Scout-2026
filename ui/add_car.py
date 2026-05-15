from datetime import datetime
from nicegui import ui
from services.car_service import *
 
 
def add_car_page() -> None:
 
    with ui.column().classes("w-full max-w-xl mx-auto mt-8 px-4 gap-4"):
        ui.label("Add a Car").classes("text-2xl font-bold")
 
        brand = ui.input("Brand").classes("w-full")
        model = ui.input("Model").classes("w-full")
 
        current_year = datetime.now().year
        year = ui.number("Year", min=1886, max=current_year,
                         precision=0).classes("w-full")
        km   = ui.number("Kilometres", min=0,
                         precision=0).classes("w-full")
 
        trans = ui.select(
            ["manual", "automatic"],
            label="Transmission",
            value="automatic",
        ).classes("w-full")
 
        price = ui.number("Price (CHF)", min=0).classes("w-full")
 
        def submit() -> None:

            errors = []
            if not brand.value:
                errors.append("Brand is required.")
            if not model.value:
                errors.append("Model is required.")
            if not year.value:
                errors.append("Year is required.")
            if km.value is None:
                errors.append("Kilometres is required.")
            if price.value is None or price.value <= 0:
                errors.append("Price must be greater than 0.")
 
            if errors:
                ui.notify(" | ".join(errors), color="negative")
                return
 
            add_car(
                brand=brand.value.strip(),
                model=model.value.strip(),
                year=int(year.value),
                km=int(km.value),
                trans=trans.value,
                price=float(price.value),
            )
            ui.notify(f"{brand.value} {model.value} added!", color="positive")
 

            brand.value = ""
            model.value = ""
            year.value  = None
            km.value    = None
            price.value = None
 
        ui.button("Add Car", on_click=submit).props("color=primary").classes("mt-2")