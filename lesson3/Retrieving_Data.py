from __future__ import print_function

import pandas as pd
import mysql.connector as mdb

if __name__ == "__main__":

    def retrieve_symbol():
        db_host = 'localhost'
        db_user = 'root'
        db_password = 'M1@crowill'
        db_name = 'securities_master'

        con = mdb.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            db = db_name
        )

    sql = "SELECT dp.price_date, dp.adj_close_price FROM symbol AS sym INNER JOIN daily_price AS dp ON dp.symbol_id = sym.id WHERE sym.ticker = 'GOOG' ORDER BY  dp.price_date ASC;"
    goog = pd.read_sql_query(sql, con=con, index_col='price_date')

    print(goog.tail())