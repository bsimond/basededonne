import mysql.connector



mydb = mysql.connector.connect( host= "127.0.0.1" , user="SIMOND", passwd= "monoboul0702", database= "herboriste")



mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM plante")
for x in mycursor:
    print(x)


# mycursor.execute("SELECT round (AVG(prix),2),indication FROM plante GROUP BY indication")
# for y in mycursor:
#     print(y)
#
# mycursor.execute("SELECT plante.nom, sous_famille.name_fr FROM plante JOIN famille ON plante.famille_id = famille.id JOIN sous_famille ON sous_famille.id = sous_famille.id")
# for z in mycursor:
#     print(z)

mycursor.execute("SELECT* FROM plante JOIN famille ON plante.id = famille.id " )
for i in mycursor:
    print(i)