import pymysql

connection = pymysql.Connect(
    host='localhost',
    user='root',
    db='LigaSzachowa'
)


def createPlayer():
    name = input("Podaj imię zawodnika: \n")
    surname = input("Podaj nazwisko: \n")
    country = input("Podaj kraj pochodzenia: \n")
    b_year = input("Podaj rok urodzenia (YYYY-MM-DD): \n")

    sql = "INSERT INTO `ListaZawodnikow` (`Name`, `Surname`, `Country`, `BYear`)" \
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
        connection.commit()
    finally:
        connection.close()


def deletePlayer():
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


def playerMenu():
    print("1. Dodaj zawodnika:")
    print("2. Usuń zawodnika:")
    what_to_do = input("Wybierz jedną z opcji:\n")

    if what_to_do == '1':
        createPlayer()
    elif what_to_do == '2':
        deletePlayer()
    else:
        return
