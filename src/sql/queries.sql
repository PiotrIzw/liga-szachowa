#Tworzenie bazy
CREATE DATABASE LigaSzachowa;

#Uzycie bazy
USE LigaSzachowa


#Tworzenie tabeli ListaZawodnikow
CREATE TABLE ListaZawodnikow (
    PlayerID int(11) NOT NULL AUTO_INCREMENT,
    Name varchar(255) NOT NULL,
    Surname varchar(255) NOT NULL,
    Country varchar(255) NOT NULL,
    BYear DATE NOT NULL,
    PRIMARY KEY(PlayerID)
    );
