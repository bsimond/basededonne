from peewee import *

db = MySQLDatabase('herboriste', user='SIMOND', password='monoboul0702',
                         host='127.0.0.1',)


class BaseModel(Model):

    class Meta:
        database= db

class SousFamille (BaseModel):
    name = CharField ( max_length=45 )
    name_fr= CharField ( max_length=45  )

class Famille (BaseModel):
    sous_famille= ForeignKeyField( SousFamille )
    name_fr= CharField (max_length=45)
    name= CharField ( max_length=45)


class Plante (BaseModel):
    famille = ForeignKeyField (Famille)
    nom=CharField ( max_length=45)
    indication=CharField (max_length=45)
    partie_utilisee=CharField(max_length=45)
    prix= DecimalField(max_digits=9, decimal_places=2)


def prix_moyen ():
    average_price = Plante.select(Plante.indication, fn.AVG(Plante.prix).alias("ave")).order_by(Plante.indication).group_by(Plante.indication)
    for plante in average_price:
        print (plante.indication, plante.ave)


def nombre_plante_par_famille():
    nbre_plante=  Famille.select(Famille.name, fn.groupby(Plante.nom).count(Plante.nom))


nombre_plante_par_famille()