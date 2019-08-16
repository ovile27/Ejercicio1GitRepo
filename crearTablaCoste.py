import pandas as pd
import sqlite3
import os
import numpy as np

pathToDb = 'db'

with sqlite3.connect(os.path.join(pathToDb, 'clientes.db')) as conn:
    dfResult.to_sql('IMPORTE_PROVINCIA', conn)

