import pandas as pd
import sqlite3
import os

def crear(self):

    pathToDb = 'db'

    with sqlite3.connect(os.path.join(pathToDb, 'clientes.db')) as conn:
        self.dfResult.to_sql('IMPORTE_PROVINCIA', conn, if_exists='replace')

