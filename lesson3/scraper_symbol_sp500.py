from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C://tools//chromedriver.exe")
#driver = webdriver.PhantomJS("C://Users//marco.zhang//.m2//repository//com//codeborne//phantomjsdriver//1.4.0//phantomjsdriver-1.4.0.jar")
driver.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
driver.maximize_window()

list_symbol = driver.find_elements_by_xpath("//table[@id='constituents']/tbody/tr/td[1]/a")

f= open("C://Users//marco.zhang//Documents//lhjy//lesson3//symbols.csv","w+")
for elem_symbol in list_symbol: 
    print(elem_symbol.text)
    f.write(elem_symbol.text + "\n")

f.close() 