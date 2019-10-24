import requests
import datetime
from bs4 import BeautifulSoup
import mysql.connector as mdb

def obtain_parse_wiki_snp500():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

    #print(result.headers);

    now = datetime.datetime.utcnow()

    soup = BeautifulSoup(response.text, 'lxml')

    list_symbol = soup.select('table')[0].select('tr')[1:]

    #print(list_symbol)

    symbols = []

    #print(list(enumerate(list_symbol)))

    for i, symbol in enumerate(list_symbol):
        list_tds = symbol.select('td')
        #print(list_tds)
        
        symbols.append(
            (
                '1',
                list_tds[0].select('a')[0].text,
                'stock',
                list_tds[1].select('a')[0].text,
                list_tds[3].text,
                'USD',
                now,
                now
            )
        )
    #print(symbols)
    return symbols

def insert_snp500_symbols(symbols):
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

    #print(con)
    column_str = "exchange_id, ticker, instrument, name, sector, currency, created_date, last_updated_date"
    insert_str = ("%s, " * 8)[:-2]
    final_str = "INSERT INTO symbol (%s) VALUES (%s)" %(column_str, insert_str)
    print(final_str)

    
    cur = con.cursor()
    cur.executemany(final_str, symbols)
    con.commit()


if __name__ == "__main__":
    symbols = obtain_parse_wiki_snp500()
    insert_snp500_symbols(symbols)