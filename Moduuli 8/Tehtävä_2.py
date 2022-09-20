import mysql.connector

yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'p0lnud123',
    autocommit=True
    )

maakoodi = input('Anna maakoodi: ')

def haeTyypit():
    sql = 'SELECT DISTINCT type FROM airport;'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def haeKenttienLkm(maakoodi, tyyppi):
    sql = '''SELECT COUNT(type) FROM airport
    WHERE iso_country = %s
    AND type = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi, tyyppi))
    tulos = kursori.fetchone()
    return tulos

tyypit = haeTyypit()
#print('tyypit: ', tyypit)

for tyyppi in tyypit:
    lkm = haeKenttienLkm(maakoodi, tyyppi[0])
    print(f"{tyyppi[0]} lukumäärä: {lkm[0]}")

#lkm = haeKenttienLkm(maakoodi, tyyppi)
#print('Lukumäärä ', lkm)