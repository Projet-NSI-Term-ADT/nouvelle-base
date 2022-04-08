import sqlite3
#connexion à la base
bdd=sqlite3.connect("BD_SITE.db")
curseur=bdd.cursor()
#désactivation de la vérification des contraintes de clé étrangère
curseur.execute('PRAGMA foreign_keys = ON')
#suppression éventuelle de l'ancienne table

# Creation table Communes
requete= """
CREATE TABLE TYPES
(
    ID_Type INTEGER NOT NULL UNIQUE,
    Type TEXT,
    PRIMARY KEY("ID_Type" AUTOINCREMENT)
);"""
curseur.execute (requete)

requete1= """
CREATE TABLE LANGUES
(
    ID_Langue INTEGER NOT NULL UNIQUE,
    Langue TEXT NOT NULL,
    PRIMARY KEY("ID_Langue" AUTOINCREMENT)
);"""
curseur.execute (requete1)

requete2= """
CREATE TABLE DEV
(
    ID_Dev INTEGER UNIQUE,
    Nom TEXT NOT NULL,
    Profil TEXT NOT NULL,
    Accepter BINARY(1),
    PRIMARY KEY("ID_Dev" AUTOINCREMENT)
);"""
curseur.execute (requete2)

requete3= """
CREATE TABLE LICENCES
(
    ID_Licence INTEGER NOT NULL UNIQUE,
    Type_de_licence TEXT,
    PRIMARY KEY("ID_Licence" AUTOINCREMENT)
);"""
curseur.execute (requete3)

requete4= """
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
curseur.execute (requete4)

requete5= """
CREATE TABLE ADMIN
(
    ID_Admin INTEGER NOT NULL UNIQUE,
    ID_Utilisateur INT NOT NULL,
    FOREIGN KEY (ID_Utilisateur) REFERENCES UTILISATEUR(ID_Utilisateur)
    PRIMARY KEY("ID_Admin" AUTOINCREMENT)
);"""
curseur.execute (requete5)

requete6= """
CREATE TABLE JEUX
(
    ID_Jeu INTEGER NOT NULL,
    Nom_de_jeu TEXT NOT NULL,
    ID_Dev INT NOT NULL,
    Date_publication DATE,
    Date_Derniere_Maj DATE,
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
curseur.execute (requete6)

requete7= """
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
curseur.execute (requete7)

requete8= """
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
curseur.execute (requete8)

requete9= """
CREATE TABLE STATUT
(
    ID_Statut INTEGER NOT NULL,
    ID_Utilisateur INT NOT NULL,
    Statut_ban BINARY(1),
    Date_ban DATE,
    PRIMARY KEY("ID_Statut" AUTOINCREMENT),
    FOREIGN KEY("ID_Utilisateur") REFERENCES UTILISATEURS("ID_Utilisateur")
);"""
curseur.execute (requete9)


