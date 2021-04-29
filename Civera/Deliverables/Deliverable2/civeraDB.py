import mysql.connector

mydb = mysql.connector.connect(host="", user="", passwd="")

if (mydb):
    print("Connection Successful")

else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()

mycursor.execute("Show databases")

for db in mycursor:
    print(db)