#1
#Wybiera maksymalnie 10 zawodnikow wedlug najwiekszej liczby punktow z kategorii OPEN

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID
WHERE Ranking.Kategoria='OPEN'
ORDER BY Ranking.Rating DESC
LIMIT 10;

#2
#Wybiera maksymalnie 10 zawodnikow wedlug najwiekszej liczby punktow z kategorii OPEN o kraju pochodzenia Polska

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID
WHERE ListaZawodnikow.Country='Polska' AND Ranking.Kategoria='OPEN'
ORDER BY Ranking.Rating DESC
LIMIT 10;

#3
#Wybiera maksymalnie 5 zawodnikow wedlug najwiekszej liczby punktow z kategorii JUNIOR powyzej roku urodzenia 2002.

SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria
FROM ListaZawodnikow
INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID
WHERE Ranking.Kategoria='JUNIOR' AND ListaZawodnikow.BYear>='2002-01-01'
ORDER BY Ranking.Rating DESC
LIMIT 5;

#4
#Wyswietla 10 pierwszych zawodnikow od najmlodszych do najstarszych

SELECT PlayerID, FirstName, Surname, Country, BYear
FROM ListaZawodnikow
ORDER BY BYear DESC
LIMIT 10;

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

#12
#Dodaje nowy turniej i spradza
INSERT INTO ListaTurniejow (Nazwa, MiejsceStartu, DataStartu) VALUES
('Mistrzostwa Malopolski', 'Krakow', '2020-08-23 12:30:00');

SELECT * FROM ListaTurniejow
WHERE Nazwa = 'Mistrzostwa Malopolski';

#13
#Przeklada datę turnieju i wyświetla
UPDATE ListaTurniejow
SET DataStartu = '2020-09-01 10:00:00'
WHERE Nazwa = 'Mistrzostwa Malopolski';

SELECT * FROM ListaTurniejow
WHERE Nazwa = 'Mistrzostwa Malopolski';

#14
#Usuwa turniej z bazy
DELETE FROM ListaTurniejow
WHERE Nazwa = 'Mistrzostwa Malopolski';




















