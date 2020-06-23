import pymysql

connection = pymysql.Connect(
    host='localhost',
    user='root',
    db='LigaSzachowa'
)

def addTournament():
    Nazwa = input("Podaj imię zawodnika: \n")
    MiejsceStartu = input("Podaj nazwisko: \n")
    DataStartu = input("Podaj kraj pochodzenia: \n")

    sql = "INSERT INTO `ListaTurniejow` (`Nazwa`, `MiejsceStartu`, `DataStartu`)" \
          " VALUES ('%s', '%s', '%s');" % (Nazwa, MiejsceStartu, DataStartu)
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

def deleteTournament():
    tournament_id = input("Podaj id zawodnika: \n")

    sql = "DELETE FROM`ListaTurniejow` WHERE (`TournamentID`) = %s;" % tournament_id
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

def changeDateOfTournament():
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

