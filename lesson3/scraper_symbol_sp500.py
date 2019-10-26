from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import mysql.connector as mdb

driver = webdriver.Chrome("C://tools//chromedriver.exe")
'''
#driver = webdriver.PhantomJS("C://Users//marco.zhang//.m2//repository//com//codeborne//phantomjsdriver//1.4.0//phantomjsdriver-1.4.0.jar")
driver.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
driver.maximize_window()

#list_symbol = driver.find_elements_by_xpath("//table[@id='constituents']/tbody/tr/td[1]/a")


f= open("C://Users//marco.zhang//Documents//lhjy//lesson3//symbols.csv","w+")
for elem_symbol in list_symbol: 
    print(elem_symbol.text)
    f.write(elem_symbol.text + "\n")

f.close() 
'''

def obtain_daily_price_snp500(symbol):

    '''
    cur = con.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    '''

    url = "https://au.finance.yahoo.com/quote/MMM/history?p=" + symbol
    now = datetime.datetime.utcnow()
    #print(url)
    driver.get(url)
    driver.maximize_window()
    #driver.execute_script("window.scrollTo(0, 10000);")
    
    #  for a given symbol

    list_trs = driver.find_elements_by_xpath("//table[1]/tbody/tr")
    #list_trs = soup.select('table')[0].select('tbody')[0].findAll('tr')
    
    
    for i in range(1, len(list_trs)):

        list_tds = driver.find_elements_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td")
        
        #print(len(list_tds))
        
        if(len(list_tds) == 7):
            
            symbol_date = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[1]").text
            symbol_open_price = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[2]").text
            symbol_high_price = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[3]").text
            symbol_low_price = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[4]").text
            symbol_close_price = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[5]").text
            symbol_adjClose_price = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[6]").text
            symbol_volume_price = driver.find_element_by_xpath("//table[1]/tbody/tr[" + str(i) + "]/td[7]").text
        
            print(symbol_date)
            print(symbol_open_price)
            print(symbol_high_price)
            print(symbol_low_price)
            print(symbol_close_price)
            print(symbol_adjClose_price)
            print(symbol_volume_price)

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
            column_str = "data_vendor_id, symbol_id, price_date, created_date, open_price, high_price, low_price, close_price, adj_close_price, volume"
            insert_str = ("%s, " * 10)[:-2]
            final_str = "INSERT INTO daily_price (%s) VALUES (%s)" %(column_str, insert_str)
            #print(final_str)
            #sql = "SELECT CAST(CONV(symbol_volume_price,16,10) AS UNSIGNED INTEGER)"
            
            data_daily = ("1", "3031", symbol_date, now, symbol_open_price, symbol_high_price, symbol_low_price, symbol_close_price, symbol_adjClose_price, int(symbol_volume_price, 16))
            
            cur = con.cursor()
            cur.execute(final_str, data_daily)
            #myresult = mycursor.fetchall()
            con.commit()
            #print(myresult)

    driver.quit()

if __name__ == "__main__":
    obtain_daily_price_snp500('MMM')