import pandas as pd
import sqlite3
import os

pathToDb = 'db'

with sqlite3.connect(os.path.join(pathToDb, 'clientes.db')) as conn:
    dfClientes = pd.read_sql('Select * from CLIENTES', conn)
    dfVentas = pd.read_sql('Select * from VENTAS', conn)

# read_sql da error con sólo el nombre de la tabla.

dfProvinciaImporte = pd.merge(dfClientes[['id_cliente', 'provincia']],
                 dfVentas[['id_cliente', 'importe']],
                 on='id_cliente')

# dfProvinciaImporte.head()

dfResult = dfProvinciaImporte.groupby(['provincia'], group_keys=['importe']).sum()
