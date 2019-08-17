import pandas as pd
import sqlite3
import os

def crearTablas():

    pathToDb = 'db'

    # Tabla clientes
    df = pd.DataFrame({'nombre': ['Carmen', 'María', 'Ovidio', 'Pedro'],
                       'provincia': ['Madrid', 'Madrid', 'Murcia', 'Albacete'],
                       'preferente': [True, True, True, False]})

    df.index.name = 'id_cliente'

    # Tabla ventas
    df2 = pd.DataFrame({'id_cliente': [0, 1, 2, 3],
                       'importe': [12, 15, 16, 18],
                       'producto': ['Ventilador', 'Ventilador', 'Ventilador', 'Ventilador']})

    df2.index.name = 'id_venta'

    with sqlite3.connect(os.path.join(pathToDb, 'clientes.db')) as conn:
        df.to_sql('CLIENTES', conn)
        df2.to_sql('VENTAS', conn)
