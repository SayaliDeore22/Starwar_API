"""
user: root
password: qwerty
host: 127.0.0.1
port: 3306
database: starwarsDB
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    password="Sayali@22",
    database="starwarsDB",
    cursorclass=pymysql.cursors.DictCursor,
)

cursor = connection.cursor()     #creating cursor object using cursor() method
cursor.execute("SHOW DATABASES")   #excuting query using excute method
results = cursor.fetchall()   #fetch data using fetchall()
for result in results:
    print(result)


