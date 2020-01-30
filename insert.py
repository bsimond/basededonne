
import mysql.connector



mydb = mysql.connector.connect( host= "127.0.0.1" , user="SIMOND", passwd= "monoboul0702", database= "plante")



mycursor = mydb.cursor()



id = 10
nom= input( "nom de la nouvelle plante")
indication=input("indication de la plante")
partie_utilisee=input("quel partie de la plante utilisez vous")
prix = input("quel est le prix")


mycursor.execute("INSERT INTO plante ( id, nom,indication,partie_utilisee, prix ) VALUES ('{}','{}','{}','{}','{}')".format(id, nom, indication, partie_utilisee, prix))




mycursor.execute(" UPDATE plante SET partie_utilisee = 'feuille'  ")

mycursor.execute("SELECT * FROM plante")
for x in mycursor:
    print(x)