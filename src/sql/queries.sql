#1
#Wybiera zawodnikow wedlug najwiekszej liczby punktow z kategorii OPEN

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID WHERE Ranking.Kategoria='OPEN' ORDER BY Ranking.Rating DESC;

#2
#Wybiera zawodnikow wedlug najwiekszej liczby punktow ze wszystkich kategorii o kraju pochodzenia Polska

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID WHERE ListaZawodnikow.Country='Polska' ORDER BY Ranking.Rating DESC;

#3
#Wybiera zawodnikow wedlug najwiekszej liczby punktow z kategorii JUNIORS powyzej roku urodzenia 2002.

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID WHERE Ranking.Kategoria='JUNIORS' AND ListaZawodnikow.BYear>='2002-01-01' ORDER BY Ranking.Rating DESC;

#4
#Wyswietla zawodnikow od najmlodszych do najstarszych

SELECT PlayerID, FirstName, Surname, Country
FROM ListaZawodnikow
ORDER BY BYear ASC;

#5
#Wyswietla liste wszystkich turniejow ktore sie jeszcze nie odbyly

SELECT Nazwa, MiejsceStartu, DataStartu FROM ListaTurniejow WHERE DataStartu>=CURDATE();

#6
SELECT RozegraneMecze.MatchID, RozegraneMecze.Wynik
FROM RozegraneMecze
INNER JOIN ListaZawodnikow ON RozegraneMecze.Gracz1 = ListaZawodnikow.PlayerID
WHERE ListaZawodnikow.FirstName='Adam' AND ListaZawodnikow.Surname='Kowalski';
