import pymysql
import os

connection = pymysql.Connect(
    host='localhost',
    user='root',
    db='LigaSzachowa'
)



def createPlayer():
    name = input("Podaj imię zawodnika: \n")
    surname = input("Podaj nazwisko: \n")
    country = input("Podaj kraj pochodzenia: \n")
    byear = input("Podaj rok urodzenia (YYYY-MM-DD): \n")

    sql = "INSERT INTO `ListaZawodnikow` (`Name`, `Surname`, `Country`, `BYear`)" \
          " VALUES ('%s', '%s', '%s', '%s');" % (name, surname, country, byear)
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
