import pymysql


def showRankingOPEN():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    sql = "SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria \
    FROM ListaZawodnikow INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID \
    WHERE Ranking.Kategoria='OPEN' \
    ORDER BY Ranking.Rating DESC LIMIT 10;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print('\n')
                for r in row:
                    print(r, end=' | ')
            print("\n")
    finally:
        connection.close()


def showRankingJUNIOR():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    sql = "SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria \
        FROM ListaZawodnikow INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID \
        WHERE Ranking.Kategoria='JUNIOR' \
        ORDER BY Ranking.Rating DESC LIMIT 10;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print('\n')
                for r in row:
                    print(r, end=' | ')
            print("\n")
    finally:
        connection.close()


def showRankingWOMAN():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    sql = "SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria \
        FROM ListaZawodnikow INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID \
        WHERE Ranking.Kategoria='WOMAN' \
        ORDER BY Ranking.Rating DESC LIMIT 10;"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print('\n')
                for r in row:
                    print(r, end=' | ')
            print("\n")
    finally:
        connection.close()


def showPlayerRanking():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    PlayerID = input("Podaj id zawodnika: \n")
    sql = "SELECT ListaZawodnikow.PlayerID, ListaZawodnikow.FirstName, ListaZawodnikow.Surname, ListaZawodnikow.Country, Ranking.Rating, Ranking.Kategoria \
        FROM ListaZawodnikow INNER JOIN Ranking ON ListaZawodnikow.PlayerID = Ranking.PlayerID \
        WHERE ListaZawodnikow.PlayerID='%s';" % PlayerID
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print('\n')
                for r in row:
                    print(r, end=' | ')
            print("\n")
    finally:
        connection.close()


def rankingMenu():
    while True:
        print("1. Ranking OPEN")
        print("2. Ranking JUNIOR")
        print("3. Ranking WOMAN")
        print("4. Rating zawodnika")
        print("5. Powrot")
        what_to_do = input("Wybierz jedną z opcji:\n")

        if what_to_do == '1':
            showRankingOPEN()
        elif what_to_do == '2':
            showRankingJUNIOR()
        elif what_to_do == '3':
            showRankingWOMAN()
        elif what_to_do == '4':
            showPlayerRanking()
        elif what_to_do == '5':
            return
        else:
            print("Bledny wybor. Sprobuj jeszcze raz.\n")
