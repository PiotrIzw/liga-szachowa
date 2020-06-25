# Liga szachowa


| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :-------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Szymon Janiszewski         | WIMiIP  | IS       |   4     | 2     | 2019/2020      |
| Piotr Izworski         | WIMiIP  | IS       |   4     | 3     | 2019/2020      |
## Projekt bazy danych
Na schemacie mamy przedstawione 4 tabele: ListaZawodnikow, RozegraneMecze, ListaTurniejow i Ranking.
Jeden zawodnik może się pojawić w rankingu zarówno dla kategorii OPEN jak i JUNIOR, dlatego występuje tu relacja jeden do wielu. Ta sama relacja jest pomiędzy tabel turniejów i rozegranych meczy.
Wyjątkowo pomiędzy tabelą rankingu i listą zawodników występuje relacja wiele do wielu.

![alt text](https://raw.githubusercontent.com/phajder-databases/db2020-project-liga-szachowa/3688e88b3ad2ce7247aa0670a20d7dbe8e569d02/resources/LigaSzachowa.svg)
## Implementacja zapytań SQL
1. Wyświetlenie 10 zawodników z najwiekszą ilością punktow z kategorii OPEN 
![img](https://i.imgur.com/dgUZw1g.png)
2. Wyświetlenie 10 zawodników z najwiekszą ilością punktow z kategorii OPEN z Polski <br>
![img](https://i.imgur.com/Yfk8bkK.png)
3. Wyświetlenie 5 zawodników z najwiekszą ilością punktow z kategorii JUNIOR urodzonych po roku 2002 <br>
![img](https://i.imgur.com/oW6rD4l.png)
4. Wyswietlenie 10 najmlodszych zawodnikow <br>
![img](https://i.imgur.com/GGLb44o.png)
5. Wyswietlenie listy wszystkich turniejow ktore sie jeszcze nie odbyly <br> 
![img](https://i.imgur.com/v3C4GAG.png)
6. Wyswietlenie listy wszystkich meczy rozegranych przez Adama Kowalskiego <br>
![img](https://i.imgur.com/kFMTs10.png)
7. Wyswietlenie listę wszystkich rozegranych meczy na Mistrzowstach Polski <br>
![img](https://i.imgur.com/8jFS10H.png)
8. Wyswietlenie wszystkich zawodnikow alfabetycznie wg. nazwiska <br>
![img](https://i.imgur.com/NUcXFgW.png)
9. Wyswietlenie danych statystycznych - jak wiele razy wygrały białe (Gracz1 = biale) <br>
![img](https://i.imgur.com/PcBOc09.png)
10. Wyswietlenie danych statystycznych - jak wiele razy wygrały czarne (Gracz2 = czarne) <br>
![img](https://i.imgur.com/B6qW1bs.png)
11. Wyswietlenie danych statystycznych - jak wiele razy wystąpił remis <br>
![img](https://i.imgur.com/qDJHnMe.png)
12. Dodanie nowego turnieju i sprawdzenie jego wartości <br>
![img](https://i.imgur.com/Y9IV6jK.png)
13. Przełożenie daty turnieju i sprawdzenie jego wartości <br>
![img](https://i.imgur.com/KmzY90R.png)
14. Usunięcie turnieju z bazy <br>
![img](https://i.imgur.com/klzHEQW.png)
## Aplikacja
Nasza aplikacja została napisana w języku Python. Na początku wyświetla się menu w którym możliwe jest zalogowanie
na zawodnika, wyświetlenie interesujących statystyk lub rankingu i wyjście z aplikacji. <br>

Dla zawodnika mamy możliwość rejestracji i sprawdzenia nadchodzących turniejów. Oto przykład rejestracji: <br>

W menu Statystyki możliwe jest sprawdzenie statystyk konkretnego zawodnika oraz tego którego koloru szachy wygrywały najczęściej. Przykład wyświetlenia statystyk zawodnika: <br>

Ostatnią opcją jest wyświetlenie rankingów. Jako że w naszej bazie wyróżniamy trzy kategoriie to musimy wybrać której konkretnie kategorii ranking nas interesuje. Oto przykład dla kategorii WOMAN: <br>

## Dodatkowe uwagi
W tej sekcji możecie zawrzeć informacje, których nie jesteście w stanie przypisać do pozostałych. Mogą to być również jakieś komentarze, wolne uwagi, itp.

