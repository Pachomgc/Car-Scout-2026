#Car Scout 2026 APP

from nicegui import ui
from data_access.database import init_db, seed_from_csv
from ui.cars import cars_page
from ui.add_car import add_car_page
from ui.car_detail import car_detail_page
from ui.edit_car import edit_car_page

init_db()
seed_from_csv("cars_data.csv")
 
 
@ui.page("/")
def index():
    
    with ui.column().classes("items-center justify-center w-full mt-16 gap-4"):
        ui.label("CAR SCOUT").classes("text-2xl font-bold")
        ui.label("Find your perfect car").classes("text-lg text-gray-500")
        with ui.row().classes("gap-4 mt-6"):
            ui.button("Browse Cars", on_click=lambda: ui.navigate.to("/cars")).props("color=primary size=lg")
            ui.button("Add a Car", on_click=lambda: ui.navigate.to("/add")).props("outline size=lg")
 
 
@ui.page("/cars")
def cars():
    _nav_bar()
    cars_page()
 
 
@ui.page("/add")
def add():
    _nav_bar()
    add_car_page()
 
 
def _nav_bar():
   
    with ui.header().classes("bg-blue-700 text-white"):
        ui.label("CAR SCOUT").classes("text-xl font-bold cursor-pointer").on(
            "click", lambda: ui.navigate.to("/")
        )
        ui.space()
        ui.button("Browse", on_click=lambda: ui.navigate.to("/cars")).props("flat color=white")
        ui.button("Add Car", on_click=lambda: ui.navigate.to("/add")).props("flat color=white")
 
 
ui.run(title="Car Scout", port=8080)
