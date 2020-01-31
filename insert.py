
import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="SIMOND", passwd="monoboul0702", database="plante")


def ajouter_plante( id, nom, indication, partie_utilisee, prix):

    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO plante ( id, nom,indication,partie_utilisee, prix ) VALUES ('{}','{}','{}','{}','{}')".format(id, nom, indication, partie_utilisee, prix))
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM  plante")
    for x in mycursor:
        print(x)


def consulter():

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM plante")
    for x in mycursor:
        print(x)

def supprimer(plante_supprimer):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM plante WHERE id = '{}'".format(plante_supprimer))
    mycursor.execute("SELECT * FROM plante")
    for x in mycursor:
        print(x)

def rechercher (plante_recherche):
    mycursor = mydb.cursor()
    mycursor.execute("select * FROM plante WHERE nom ='{}'".format(plante_recherche))
    for x in mycursor:
        print(x)





