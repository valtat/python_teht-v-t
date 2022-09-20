import mysql.connector

yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'p0lnud123',
    autocommit=True
    )

def haeEtäisyys():
    sql = 'SELECT distance FROM airport;'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos