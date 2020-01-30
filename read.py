import mysql.connector



mydb = mysql.connector.connect( host= "127.0.0.1" , user="SIMOND", passwd= "monoboul0702", database= "plante")



mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM  plante" )

for x in mycursor:
  print(x)


