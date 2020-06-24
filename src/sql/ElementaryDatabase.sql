#Usun baze
DROP DATABASE LigaSzachowa;

#Tworzenie bazy
CREATE DATABASE LigaSzachowa;

#Uzycie bazy
USE LigaSzachowa;


#Tworzenie tabeli ListaZawodnikow
CREATE TABLE ListaZawodnikow (
    PlayerID int(11) NOT NULL AUTO_INCREMENT,
    FirstName varchar(255) NOT NULL,
    Surname varchar(255) NOT NULL,
    Country varchar(255) NOT NULL,
    BYear DATE NOT NULL,
    PRIMARY KEY(PlayerID)
    );

#Tworzenie tabeli ListaTurniejow
CREATE TABLE ListaTurniejow (
    TournamentID int(11) NOT NULL AUTO_INCREMENT,
    Nazwa varchar(255) NOT NULL,
    MiejsceStartu varchar(255) NOT NULL,
    DataStartu DATETIME NOT NULL,
    PRIMARY KEY(TournamentID)
    );

#Tworzenie tabeli RozegraneMecze
CREATE TABLE RozegraneMecze (
    MatchID int(11) NOT NULL AUTO_INCREMENT,
    DataRozegrania DATE NOT NULL,
    TurniejID int(11) NOT NULL,
    Kategoria varchar(255) NOT NULL,
    Gracz1 int(11) NOT NULL,
    Gracz2 int(11) NOT NULL,
    Wynik varchar(255) NOT NULL,
    Etap varchar(255) NOT NULL,
    PRIMARY KEY(MatchID),
    FOREIGN KEY (Gracz1) REFERENCES ListaZawodnikow(PlayerID),
    FOREIGN KEY (Gracz2) REFERENCES ListaZawodnikow(PlayerID),
    FOREIGN KEY (TurniejID) REFERENCES ListaTurniejow(TournamentID)
    );


#Tworzenie tabeli Ranking
CREATE TABLE Ranking (
    RankingID int(11) NOT NULL AUTO_INCREMENT,
    PlayerID int(11) NOT NULL UNIQUE,
    Rating int(11) NOT NULL,
    Kategoria varchar(255) NOT NULL,
    PRIMARY KEY(RankingID),
    FOREIGN KEY (PlayerID) REFERENCES ListaZawodnikow(PlayerID)
    );

