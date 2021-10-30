import pandas as pd
import sqlite3
import os

save_path = '.\exports'


def fileOps(cur_date):

    file_name = 'data'+cur_date+'.csv'
    value = os.path.join(save_path, file_name)

    conn = sqlite3.connect('database.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    data = pd.read_sql_query('select * from posts', conn)
    data.to_csv(value, index=False)


