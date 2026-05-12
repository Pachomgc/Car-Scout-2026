from nicegui import ui
from car_service import get_all_cars, delete_car
 
 
def cars_page() -> None:
    with ui.column().classes("w-full max-w-5xl mx-auto mt-8 px-4 gap-4"):
        ui.label("All Cars").classes("text-2xl font-bold")
 
        table_container = ui.column().classes("w-full")
 
        def render_table() -> None:
            table_container.clear()
            with table_container:
                cars = get_all_cars()
                if not cars:
                    ui.label("No cars listed yet.").classes("text-gray-500")
                    return
 
                columns = [
                    {"name": "brand",  "label": "Brand",        "field": "brand",  "sortable": True},
                    {"name": "model",  "label": "Model",        "field": "model",  "sortable": True},
                    {"name": "year",   "label": "Year",         "field": "year",   "sortable": True},
                    {"name": "km",     "label": "Kilometres",   "field": "km",     "sortable": True},
                    {"name": "trans",  "label": "Transmission", "field": "trans",  "sortable": True},
                    {"name": "price",  "label": "Price (CHF)",  "field": "price",  "sortable": True},
                    {"name": "action", "label": "",             "field": "action"},
                ]
                rows = [
                    {
                        "id":    c.id,
                        "brand": c.brand,
                        "model": c.model,
                        "year":  c.year,
                        "km":    f"{c.km:,}",
                        "trans": c.trans.capitalize(),
                        "price": f"CHF {c.price:,.0f}",
                    }
                    for c in cars
                ]
 
                table = ui.table(columns=columns, rows=rows, row_key="id").classes("w-full")
 
                table.add_slot(
                    "body-cell-action",
                    """
                    <q-td :props="props">
                      <q-btn flat dense color="negative" icon="delete"
                             @click="$parent.$emit('delete', props.row)" />
                    </q-td>
                    """,
                )
 
                def handle_delete(e) -> None:
                    delete_car(e.args["id"])
                    ui.notify("Car deleted.", color="negative")
                    render_table()
 
                table.on("delete", handle_delete)
 
        render_table()