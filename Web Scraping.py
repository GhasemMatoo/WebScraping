import mysql.connector
import requests
from bs4 import BeautifulSoup
cnx = mysql.connector.connect(user='root', password='Matoo1368',
                              host='localhost',
                              database='leb')
cursor = cnx.cursor()
name=input("Please Enter The Name Of The Car Models:")
r = requests.get('https://www.truecar.com/prices-new/'+name)
soup=BeautifulSoup(r.text,'html.parser')
val_1=soup.find_all('div', attrs={"heading-4 margin-top-2"})
val_2=soup.find_all('div', attrs={"class":"label-block-title"})
val_3=soup.find_all('div', attrs={"class":"label-block-text"})
for i in range(20):
    nam_model=val_1[i].text
    situation=val_2[i].text
    price=val_3[i].text
    cursor.execute('INSERT INTO car VALUES(\'%s\',\'%s\',\'%s\')'%(nam_model,situation,price))
cnx.commit()
cnx.close()
