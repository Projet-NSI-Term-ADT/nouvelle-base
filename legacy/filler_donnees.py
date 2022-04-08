import sqlite3
#connexion à la base
bdd=sqlite3.connect("BD_SITE.db")
curseur=bdd.cursor()

requete1= """
INSERT INTO LANGUES
(Langue)
VALUES
("Francais")
"""

requete2= """
INSERT INTO LANGUES
(Langue)
VALUES
("English")
"""

requete3= """
INSERT INTO LANGUES
(Langue)
VALUES
("Deutch")
"""

requete4= """
INSERT INTO LANGUES
(Langue)
VALUES
("Italian")
"""

requete5= """
INSERT INTO LANGUES
(Langue)
VALUES
("Espanol")
"""

requete6= """
INSERT INTO TYPES
(Type)
VALUES
("Action")
"""

requete7= """
INSERT INTO TYPES
(Type)
VALUES
("Aventure")
"""

requete8= """
INSERT INTO TYPES
(Type)
VALUES
("RPG")
"""

requete9= """
INSERT INTO TYPES
(Type)
VALUES
("Indie")
"""

requete10= """
INSERT INTO TYPES
(Type)
VALUES
("Platformer")
"""

requete11= """
INSERT INTO TYPES
(Type)
VALUES
("Enigme")
"""

requete12= """
INSERT INTO TYPES
(Type)
VALUES
("MMO")
"""

requete13= """
INSERT INTO DEV
(Nom,Profil)
VALUES
("Team Cherry","Equipe Australienne de 3 personnes ayant développé Hollow Knight et en préparation de Silksong")
"""

requete14= """
INSERT INTO DEV
(Nom,Profil)
VALUES
("Activision","J'adore l'argent")
"""

requete15= """
INSERT INTO DEV
(Nom,Profil)
VALUES
("Electronic Arts","Moi aussi j'adore l'argent")
"""

requete16= """
INSERT INTO DEV
(Nom,Profil)
VALUES
("Ubisoft","On aime l'argent mais on est bretons")
"""

requete17= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("cMoi","mauxdepasses","sivousenvoyezdesmailsicivousetessacrementstupide@gmail.com","20/02/2002",0,"None",0,1)
"""

requete18= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("cToujoursMoi","MaudePasse","nanmaistesconoutulefaisexpres@gmail.com","12/12/1212",0,"None",0,2)
"""

requete19= """
INSERT INTO LICENCES
(Type_de_licence)
VALUES
("CC-by")
"""

requete20= """
INSERT INTO LICENCES
(Type_de_licence)
VALUES
("CC-by-sa")
"""

requete21= """
INSERT INTO LICENCES
(Type_de_licence)
VALUES
("CC-by-nd")
"""

requete22= """
INSERT INTO LICENCES
(Type_de_licence)
VALUES
("CC-by-nc")
"""

requete23= """
INSERT INTO LICENCES
(Type_de_licence)
VALUES
("CC-by-nc-sa")
"""

requete24= """
INSERT INTO LICENCES
(Type_de_licence)
VALUES
("CC-by-nc-nd")
"""


curseur.execute(f'INSERT INTO LICENCES (Type_de_licence) VALUES ("CC-EF")')
curseur.execute(f'INSERT INTO ADMIN (ID_Utilisateur) VALUES (1)')
curseur.execute(f'INSERT INTO JEUX (Nom_de_jeu,ID_Dev,Date_publication,Date_Derniere_Maj,ID_Type,Description,Nombre_joueur,Pegi,Lien,ID_Langue,ID_Licence,image_jeu,Publication) VALUES ("Sky-Rimes",1,10-10-2000,10-10-2000,1,"Jeu trop ouf",1,16,"https://www.youtube.com/",1,1,"https://imgur.com/",0)')
curseur.execute(requete1)
curseur.execute(requete2)
curseur.execute(requete3)
curseur.execute(requete4)
curseur.execute(requete5)
bdd.commit()