from insert import ajouter_plante , consulter,supprimer,rechercher



print( "que souhaitez vous faire")
print("C = CONSULTER ")
print("A = AJOUTER ")
print("S= SUPPRIMER ")
print("R=RECHERCHER")

choix=input("que choisissez-vous ")

if choix.upper()== "A":
    id = 10
    nom = input("nom de la nouvelle plante")
    indication = input("indication de la plante")
    partie_utilisee = input("quel partie de la plante utilisez vous")
    prix = input("quel est le prix")
    ajouter_plante(id,nom,indication,partie_utilisee,prix )



if choix.upper() =="C":
    consulter()

if choix.upper() == "S":
    consulter()
    plante_supprimer= input("entrez le numero de la plante a supprimer")
    supprimer(plante_supprimer)

if choix.upper()=="r":
    plante_recherchee=input("entre la plante recherchée")
    rechercher(plante_recherchee)


