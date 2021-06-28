import mysql.connector
from sklearn import tree
from sklearn import preprocessing
cnx = mysql.connector.connect(user='root', password='Matoo1368',
                              host='localhost',
                              database='leb')
cursor = cnx.cursor()
query ='SELECT * FROM bama;'
cursor.execute(query)
x=[]
y=[]
for (model,sal,karkard,Gheymat) in cursor:
    le = preprocessing.LabelEncoder()
    le.fit([model,sal,karkard])
    x.append(le.transform([model,sal,karkard]))
    y.append(Gheymat)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x, y)
le = preprocessing.LabelEncoder()
##---------------------------------in-inport-use------
le.fit(['هیوندای i30', '2011', 'کارکرد 89,000'])
vorodi=le.transform(['هیوندای i30', '2011', 'کارکرد 89,000'])
new_data=[vorodi]
answer=clf.predict(new_data)
print(answer[0])
cnx.close()
