import sqlite3
#connexion à la base
bdd=sqlite3.connect("BD_SITE.db")
curseur=bdd.cursor()
#désactivation de la vérification des contraintes de clé étrangère
curseur.execute('PRAGMA foreign_keys = ON')
#suppression éventuelle de l'ancienne table


# Creation table Communes
requete100= """
CREATE TABLE TYPES
(
    ID_Type INTEGER NOT NULL UNIQUE,
    Type TEXT,
    PRIMARY KEY("ID_Type" AUTOINCREMENT)
);"""
curseur.execute (requete100)

requete101= """
CREATE TABLE LANGUES
(
    ID_Langue INTEGER NOT NULL UNIQUE,
    Langue TEXT NOT NULL,
    PRIMARY KEY("ID_Langue" AUTOINCREMENT)
);"""
curseur.execute (requete101)

requete102= """
CREATE TABLE DEV
(
    ID_Dev INTEGER UNIQUE,
    Nom TEXT NOT NULL,
    Profil TEXT NOT NULL,
    Accepter BINARY(1),
    PRIMARY KEY("ID_Dev" AUTOINCREMENT)
);"""
curseur.execute (requete102)

requete103= """
CREATE TABLE LICENCES
(
    ID_Licence INTEGER NOT NULL UNIQUE,
    Type_de_licence TEXT,
    PRIMARY KEY("ID_Licence" AUTOINCREMENT)
);"""
curseur.execute (requete103)

requete104= """
CREATE TABLE UTILISATEUR
(
    ID_Utilisateur INTEGER NOT NULL UNIQUE,
    Identifiant TEXT NOT NULL,
    Mdp TEXT NOT NULL,
    Adresse_mail TEXT NOT NULL,
    Date_de_naissance TEXT NOT NULL,
    Nombre_avertissement INT,
    Nature_Avertissement TEXT NOT NULL,
    Temp_ban BINARY(1),
    ID_Dev INT,
    FOREIGN KEY (ID_Dev) REFERENCES DEV(ID_Dev)
    PRIMARY KEY("ID_Utilisateur" AUTOINCREMENT)
);"""
curseur.execute (requete104)

requete105= """
CREATE TABLE ADMIN
(
    ID_Admin INTEGER NOT NULL UNIQUE,
    ID_Utilisateur INT NOT NULL,
    FOREIGN KEY (ID_Utilisateur) REFERENCES UTILISATEUR(ID_Utilisateur)
    PRIMARY KEY("ID_Admin" AUTOINCREMENT)
);"""
curseur.execute (requete105)

requete106= """
CREATE TABLE JEUX
(
    ID_Jeu INTEGER NOT NULL,
    Nom_de_jeu TEXT NOT NULL,
    ID_Dev INT NOT NULL,
    Date_publication DATE,
    Date_Derniere_Maj DATE,
    Version_jeu INT,
    ID_Type INT NOT NULL,
    Description TEXT,
    Nombre_joueur INT,
    Pegi INT NOT NULL,
    Lien TEXT,
    ID_Langue INT NOT NULL,
    ID_Licence INT NOT NULL,
    Image_jeu TEXT,
    Publication INT,
    PRIMARY KEY("ID_Jeu" AUTOINCREMENT),
    FOREIGN KEY("ID_Dev") REFERENCES DEV("ID_Dev"),
    FOREIGN KEY("ID_Type") REFERENCES TYPES("ID_Type"),
    FOREIGN KEY("ID_Licence") REFERENCES LICENCES("ID_Licence"),
    FOREIGN KEY("ID_Langue") REFERENCES LANGUES("ID_Langue")
);"""
curseur.execute (requete106)

requete107= """
CREATE TABLE AVIS
(
    ID_Avis INT NOT NULL,
    ID_Utilisateur INT NOT NULL,
    ID_Jeu INT NOT NULL,
    Date_avis DATE,
    Note INT(100),
    Commentaire TEXT NOT NULL,
    PRIMARY KEY("ID_Avis"),
    FOREIGN KEY("ID_Utilisateur") REFERENCES UTILISATEURS("ID_Utilisateur"),
    FOREIGN KEY("ID_Jeu") REFERENCES JEUX("ID_Jeu")
);"""
curseur.execute (requete107)

requete108= """
CREATE TABLE TELECHARGEMENT
(
    ID_Telechargement INTEGER NOT NULL,
    ID_Utilisateur INT NOT NULL,
    ID_Jeu INT NOT NULL,
    Date_telechargement DATE,
    PRIMARY KEY("ID_Telechargement" AUTOINCREMENT),
    FOREIGN KEY("ID_Utilisateur") REFERENCES UTILISATEURS("ID_Utilisateur"),
    FOREIGN KEY("ID_Jeu") REFERENCES JEUX("ID_Jeu")
);"""
curseur.execute (requete108)

requete109= """
CREATE TABLE STATUT
(
    ID_Statut INTEGER NOT NULL,
    ID_Utilisateur INT NOT NULL,
    Statut_ban BINARY(1),
    Date_ban DATE,
    PRIMARY KEY("ID_Statut" AUTOINCREMENT),
    FOREIGN KEY("ID_Utilisateur") REFERENCES UTILISATEURS("ID_Utilisateur")
);"""
curseur.execute (requete109)

requete110 = """
INSERT INTO DEV
VALUES (1,"Pierre","Menes",1),
       (2,"Bob","Lennon",1),
       (3,"Jean","Goat",1),
       (4,"Jackie","Michele",1);
"""
curseur.execute (requete110)

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

requete25= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("shinigvmi","nartuocrigolo","uneadresse@gmail.com","20/02/1000",0,"None",0,3)
"""

requete26= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("blind","pasunmdpfacile","adresseune@gmail.com","28/09/1998",0,"None",0,1)
"""

requete27= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("d1s3ase","maladie","uneadressemalade@gmail.com","14/10/1998",0,"None",0,1)
"""

requete28= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("ElouanLahougue","motdepaZe","elouanmusic@gmail.com","26/03/1998",0,"None",0,2)
"""

requete29= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("TintinLeGrand","miloulepetit","tintininspecteur@gmail.com","17/05/1998",0,"None",0,2)
"""


requete30= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("Kyrox44","soupirmptroa","kyrox44@gmail.com","11/09/1998",0,"None",0,2)
"""


requete31= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("x9lux","mainluxlol","x9lux@gmail.com","15/04/1998",0,"None",0,2)
"""


requete32= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("Dounet","doudoudoudounet","dieuvouslerendra@gmail.com","26/11/1998",0,"None",0,2)
"""


requete33= """
INSERT INTO UTILISATEUR
(Identifiant,Mdp,Adresse_mail,Date_de_naissance,Nombre_avertissement,Nature_Avertissement,Temp_ban,ID_Dev)
VALUES
("TissMeAccable","ckoicepseudo","aipakompri@gmail.com","17/07/1998",0,"None",0,2)
"""

requete34 = """
INSERT INTO TYPES
VALUES (1,"Action"),
       (2,"Aventure"),
       (3,"RPG"),
       (4,"Survie"),
       (5,"3eme personne"),
       (6,"1er personne"),
       (7,"Vue de dessus"),
       (8,"Sandbox"),
       (9,"Monde ouvert"),
       (10,"Tour par tour"),
       (11,"Réaliste"),
       (12,"Graphismes pixels"),
       (13,"Humour"),
       (14,"Rogue like"),
       (15,"Multijoueur"),
       (16,"Solo"),
       (17,"Coop online"),
       (18,"Coop écran partagé "),
       (19,"Simulation"),
       (20,"Gestion"),
       (21,"Platformer"),
       (22,"Puzzle"),
       (23,"Gimmick");
       
"""

requete35 = """
INSERT INTO JEUX 
VALUES (1,'Mario',1,DATE('now'),DATE('now'),1,1,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (2,'AMOGUS',2,DATE('now'),DATE('now'),1,1,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (3,'rock simulator',3,DATE('now'),DATE('now'),1,1,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (4,'Minecraft 2',4,DATE('now'),DATE('now'),1,1,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (5,'Sky-Rimes',1,DATE('now'),DATE('now'),1,1,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (6,'Raquette-League',1,'2020-02-01',DATE('now'),1,2,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (7,'Boom-Plage',1,DATE('now'),DATE('now'),1,2,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (8,'Mein-Kraft',1,'2020-07-13',DATE('now'),1,1,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (9,'Jenshin',1,'2021-01-29',DATE('now'),1,3,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (10,'Chevalier-Vide',1,'2021-01-29',DATE('now'),1,3,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (11,'Selesste',1,'2021-01-29',DATE('now'),1,3,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (12,'Predateur-legende',1,'2021-01-29',DATE('now'),1,3,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0),
       (13,'contre-attaque-offensive-globale',1,'2021-01-29',DATE('now'),1,3,'Jeu trop ouf, vrmt trop incroyable',1,16,'https://www.youtube.com/',1,1,'https://imgur.com/',0);
"""

curseur.execute(f'INSERT INTO LICENCES (Type_de_licence) VALUES ("CC-ef")')
curseur.execute(requete1)
curseur.execute(requete2)
curseur.execute(requete3)
curseur.execute(requete4)
curseur.execute(requete5)
curseur.execute(requete13)
curseur.execute(requete14)
curseur.execute(requete15)
curseur.execute(requete16)
curseur.execute(requete17)
curseur.execute(requete18)
curseur.execute(requete19)
curseur.execute(requete20)
curseur.execute(requete21)
curseur.execute(requete22)
curseur.execute(requete23)
curseur.execute(requete24)
curseur.execute(requete25)
curseur.execute(requete26)
curseur.execute(requete27)
curseur.execute(requete28)
curseur.execute(requete29)
curseur.execute(requete30)
curseur.execute(requete31)
curseur.execute(requete32)
curseur.execute(requete33)
curseur.execute(requete34)
curseur.execute(requete35)
bdd.commit()