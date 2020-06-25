import pymysql


def showPlayerStatistics():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    FirstName = input("Podaj imie zawodnika: \n")
    Surname = input("Podaj nazwisko zawodnika: \n")
    sql = "SELECT RozegraneMecze.MatchID, RozegraneMecze.Wynik FROM RozegraneMecze \
    INNER JOIN ListaZawodnikow ON RozegraneMecze.Gracz1 = ListaZawodnikow.PlayerID\
    WHERE ListaZawodnikow.FirstName='%s' AND ListaZawodnikow.Surname='%s';" % (FirstName, Surname)
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


def showWhiteBlackStatistics():
    def showWhiteStatistics():
        connection = pymysql.Connect(
            host='localhost',
            user='root',
            db='LigaSzachowa'
        )

        sql = "SELECT Wynik, COUNT(*) FROM RozegraneMecze WHERE  Wynik = 'Wygrana bialych';"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    for r in row:
                        print(r, end=' | ')
                print("\n")
        finally:
            connection.close()

    def showBlackStatistics():
        connection = pymysql.Connect(
            host='localhost',
            user='root',
            db='LigaSzachowa'
        )

        sql = "SELECT Wynik, COUNT(*) FROM RozegraneMecze WHERE  Wynik = 'Wygrana czarnych';"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    for r in row:
                        print(r, end=' | ')
                print("\n")
        finally:
            connection.close()

    def showDrawStatistics():
        connection = pymysql.Connect(
            host='localhost',
            user='root',
            db='LigaSzachowa'
        )

        sql = "SELECT Wynik, COUNT(*) FROM RozegraneMecze WHERE  Wynik = 'Remis';"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    for r in row:
                        print(r, end=' | ')
                print("\n")
        finally:
            connection.close()

    showWhiteStatistics()
    showBlackStatistics()
    showDrawStatistics()


def statisticsMenu():
    while True:
        print("1. Statystyki zawodnika")
        print("2. Statystyki wygranych (białe & czarne)")
        print("3. Powrot")
        what_to_do = input("Wybierz jedną z opcji:\n")

        if what_to_do == '1':
            showPlayerStatistics()
        elif what_to_do == '2':
            showWhiteBlackStatistics()
        elif what_to_do == '3':
            return
        else:
            print("Bledny wybor. Sprobuj jeszcze raz.\n")
