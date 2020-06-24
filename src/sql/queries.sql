#1
#Wybiera zawodnikow wedlug najwiekszej liczby punktow z kategorii OPEN

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID
WHERE Ranking.Kategoria='OPEN'
ORDER BY Ranking.Rating ASC;

#2
#Wybiera zawodnikow wedlug najwiekszej liczby punktow ze wszystkich kategorii o kraju pochodzenia Polska

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID
WHERE ListaZawodnikow.Country='Polska'
ORDER BY Ranking.Rating ASC;

#3
#Wybiera zawodnikow wedlug najwiekszej liczby punktow z kategorii JUNIORS powyzej roku urodzenia 2002.

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID
WHERE Ranking.Kategoria='JUNIORS' AND ListaZawodnikow.BYear>='2002-01-01'
ORDER BY Ranking.Rating ASC;

#4
#Wyswietla zawodnikow od najmlodszych do najstarszych

SELECT PlayerID, FirstName, Surname, Country, BYear
FROM ListaZawodnikow
ORDER BY BYear DESC;

#5
#Wyswietla liste wszystkich turniejow ktore sie jeszcze nie odbyly

SELECT Nazwa, MiejsceStartu, DataStartu
FROM ListaTurniejow
WHERE DataStartu>=CURDATE();

#6
#Wyswietla liste meczy rozegranych przez Adama Kowalskiego
SELECT RozegraneMecze.MatchID, RozegraneMecze.Wynik
FROM RozegraneMecze
INNER JOIN ListaZawodnikow ON RozegraneMecze.Gracz1 = ListaZawodnikow.PlayerID
WHERE ListaZawodnikow.FirstName='Adam' AND ListaZawodnikow.Surname='Kowalski';

#7
#Wyswietla listę wszystkich rozegranych meczy na Mistrzowstach Polski
SELECT RozegraneMecze.MatchID, RozegraneMecze.Gracz1, RozegraneMecze.Gracz2, RozegraneMecze.Wynik, ListaTurniejow.Nazwa
FROM RozegraneMecze
INNER JOIN ListaTurniejow ON RozegraneMecze.TurniejID = ListaTurniejow.TournamentID
WHERE ListaTurniejow.Nazwa = 'Mistrzostwa Polski';

#8
#Wyswietla wszystkich zawodnikow alfabetycznie wg. nazwiska.
SELECT PlayerID, Surname, FirstName, Country, BYear
FROM ListaZawodnikow
ORDER BY Surname ASC;

#9
#Wyswietla dane statystyczne - jak wiele razy wygrały białe (Gracz1 = biale)
SELECT Wynik, COUNT(*)
FROM   RozegraneMecze
WHERE  Wynik = 'Wygrana bialych';

#10
#Wyswietla dane statystyczne - jak wiele razy wygrały czarne (Gracz2 = czarne)
SELECT Wynik, COUNT(*)
FROM   RozegraneMecze
WHERE  Wynik = 'Wygrana czarnych';

#11
#Wyswietla dane statystyczne - jak wiele razy wystąpił remis
SELECT Wynik, COUNT(*)
FROM   RozegraneMecze
WHERE  Wynik = 'Remis';
























