import os

#  view_name: (width, height)
WIND_SIZE = {
    'LIWind': (400, 225),
    'SUWind': (800, 500),
    'PHWind': (800, 500),
    'WHWind': (800, 500),
    'OHWind': (800, 500)
}

# App's mini logo img.
APP_MINI_LOGO = os.path.abspath("src/assets/imgs/icon.png")

#Apps's font color
WHITE = "#000000"
RED = "#D10606"

# User account types.
ACC_TYPE = {
    'Seleccione una opcion': 0,
    'Almacen': 1,
    'Planeacion': 2,
    'Propietario': 3
}


MATERIALS = {
    'Cable' : 0,
    'Fierro' : 1,
    'Pan' : 2
}

TRANSACTION = {
    'Egreso'  : 0,
    'Ingreso' : 1
}

#   (Column_id, Column_text) 
PROYECT_COLUMNS = (
    ("prj_name", "Nombre"),
    ("recipient", "Cliente"),
    ("begin_date", "Fecha inicio"),
    ("finish_date", "Fecha fin"),
    ("curr_state", "Estado")
)

