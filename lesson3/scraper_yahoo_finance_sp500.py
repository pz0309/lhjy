import requests
import datetime
from bs4 import BeautifulSoup
import mysql.connector as mdb

if __name__ == "__main__":
    
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

def obtain_daily_price_snp500(symbol):

    '''
    cur = con.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    '''

    url = "https://au.finance.yahoo.com/quote/MMM/history?p=" + symbol
    #print(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    #  for a given symbol
    list_trs = soup.select('table')[0].select('tbody')[0].findAll('tr')
    
    for i in range(0, len(list_trs)-1):
        list_tds = soup.select('table')[0].select('tbody')[0].select('tr')[i].findAll('td')

        if(len(list_tds) == 7):
            
            symbol_date = list_tds[0].select('span')[0].text
            symbol_open_price = list_tds[1].select('span')[0].text
            symbol_high_price = list_tds[2].select('span')[0].text
            symbol_low_price = list_tds[3].select('span')[0].text
            symbol_close_price = list_tds[4].select('span')[0].text
            symbol_adjClose_price = list_tds[5].select('span')[0].text
            symbol_volume_price = list_tds[6].select('span')[0].text
        
            print(symbol_date)
            print(symbol_open_price)
            print(symbol_high_price)
            print(symbol_low_price)
            print(symbol_close_price)
            print(symbol_adjClose_price)
            print(symbol_volume_price)

if __name__ == "__main__":
    obtain_daily_price_snp500('MMM')

    