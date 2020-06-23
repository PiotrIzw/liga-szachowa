import pymysql
import os

connection = pymysql.Connect(
    host='localhost',
    user='root',
    db='LigaSzachowa'
)

sql = "INSERT INTO `booking` (`id`, `offer_id`, `total_price`, `payment_deadline`, `paid`, `client_id`)" \
          " VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (id, offer_id, total_price, payment_deadline,
            paid, client_id)
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