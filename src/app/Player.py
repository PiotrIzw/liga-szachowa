import pymysql


def createPlayer():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    name = input("Podaj imię zawodnika: \n")
    surname = input("Podaj nazwisko: \n")
    country = input("Podaj kraj pochodzenia: \n")
    b_year = input("Podaj rok urodzenia (YYYY-MM-DD): \n")

    sql = "INSERT INTO `ListaZawodnikow` (`FirstName`, `Surname`, `Country`, `BYear`)" \
          " VALUES ('%s', '%s', '%s', '%s');" % (name, surname, country, b_year)
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print('\n')
                for r in row:
                    print(r, end=' ')
            print("Zostales pomyslnie zarejestrowany.\n")
        connection.commit()
    finally:
        connection.close()


def deletePlayer():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    player_id = input("Podaj id zawodnika: \n")

    sql = "DELETE FROM`ListaZawodnikow` WHERE (`PlayerID`) = %s;" % player_id
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print('\n')
                for r in row:
                    print(r, end=' ')
        connection.commit()
    finally:
        connection.close()


def showTournaments():
    connection = pymysql.Connect(
        host='localhost',
        user='root',
        db='LigaSzachowa'
    )

    sql = "SELECT Nazwa, MiejsceStartu, DataStartu FROM ListaTurniejow WHERE DataStartu>=CURDATE();"
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


def playerMenu():
    while True:
        print("1. Rejestracja")
        print("2. Aktualne turnieje")
        print("3. Powrot")
        what_to_do = input("Wybierz jedną z opcji:\n")

        if what_to_do == '1':
            createPlayer()
        elif what_to_do == '2':
            showTournaments()
        elif what_to_do == '3':
            return
        else:
            print("Bledny wybor. Sprobuj jeszcze raz.\n")
