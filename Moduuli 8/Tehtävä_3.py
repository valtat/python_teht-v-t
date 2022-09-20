import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'p0lnud123',
    autocommit=True
    )

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
def haeEtäisyys(icao):
    tuple = (icao,)
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;'
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos

etäisyys1 = haeEtäisyys(icao1)
etäisyys2 = haeEtäisyys(icao2)
if etäisyys1 and etäisyys2 is not None:
    print(f"Lentokenttien välinen etäisyys on: ",distance.distance(etäisyys1, etäisyys2))
else:
    print("ICAO-koodia ei löydy.")