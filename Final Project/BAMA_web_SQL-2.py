import mysql.connector
import requests
import re
from bs4 import BeautifulSoup
cnx = mysql.connector.connect(user='root', password='Matoo1368',
                              host='localhost',
                              database='leb')
cursor = cnx.cursor()
for j in range(2):
    r = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?page='+str(j))
    soup=BeautifulSoup(r.text,'html.parser')
    val_1=soup.find_all('h2', attrs={"persianOrder"})
    val_2=soup.find_all('span', attrs={"class":"price year-label hidden-xs"})
    val_3=soup.find_all('p', attrs={"class":"price hidden-xs"})
    val_4=soup.find_all('p', attrs={"class":"cost blured"})
    val_4=soup.find_all('p', attrs={"class":"cost"})
    for i in range(len(val_1)):
        Gheymat=re.sub(r' تومان','',val_4[i].text).strip()
        if Gheymat=='توافقی':
            continue
        model=re.sub(r'\s+',' ',val_1[i].text).strip()
        model=re.sub(r'\،','',model).strip()
        sal=re.sub(r'\،','',val_2[i].text).strip()
        karkard=re.sub(r'','',val_3[i].text).strip()
        if karkard=="کارکرد صفر" or karkard=="-" :
            karkard='0'
        cursor.execute('INSERT INTO bama VALUES(\'%s\',\'%s\',\'%s\',\'%s\')'%(model,sal,karkard,Gheymat))
cnx.commit()
cnx.close()
