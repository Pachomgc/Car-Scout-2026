from nicegui import ui
from services.car_service import get_all_cars, delete_car, search_cars


@ui.page("/cars")
def cars_page():

    ui.label("All Cars").classes("text-3xl font-bold m-6")
    search_input = ui.input(
    label="Search by brand or model",
    placeholder="Example: BMW, Audi, M3..."
    ).classes("w-1/2 mx-6")

    with ui.row().classes("mx-6 mb-4 gap-3"):
        ui.button("Search", on_click=lambda: ui.navigate.to("/cars")).props("color=primary")
        ui.button("Reset", on_click=lambda: ui.navigate.to("/cars")).props("outline")

    search_text = search_input.value

    if search_text:
        cars = search_cars(search_text)
    else:
        cars = get_all_cars()

    columns = [
        {"name": "brand", "label": "Brand", "field": "brand"},
        {"name": "model", "label": "Model", "field": "model"},
        {"name": "year", "label": "Year", "field": "year"},
        {"name": "km", "label": "Kilometres", "field": "km"},
        {"name": "trans", "label": "Transmission", "field": "trans"},
        {"name": "price", "label": "Price (CHF)", "field": "price"},
        {"name": "actions", "label": "Actions", "field": "actions"},
    ]


    rows = []



    rows = []

    for car in cars:
        rows.append({
            "id": car.id,
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "km": f"{car.km:,}",
            "trans": car.trans,
            "price": f"CHF {car.price:,.0f}",
        })

    table = ui.table(
        columns=columns,
        rows=rows,
        row_key="id",
    ).classes("w-full m-6")

    table.add_slot(
        "body-cell-actions",
        """
        <q-td :props="props">
            <q-btn
                color="primary"
                label="View"
                dense
                class="q-mr-sm"
                @click="$parent.$emit('view', props.row.id)"
            />
            <q-btn
                color="orange"
                label="Edit"
                dense
                class="q-mr-sm"
                @click="$parent.$emit('edit', props.row.id)"
            />
            <q-btn
                color="red"
                icon="delete"
                dense
                round
                @click="$parent.$emit('delete', props.row.id)"
            />
        </q-td>
        """
    )

    table.on("view", lambda e: ui.navigate.to(f"/cars/{e.args}"))
    table.on("edit", lambda e: ui.navigate.to(f"/cars/edit/{e.args}"))

    def handle_delete(e):
        delete_car(e.args)
        ui.notify("Car deleted")
        ui.navigate.to("/cars")

    table.on("delete", handle_delete)