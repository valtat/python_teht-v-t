import mysql.connector
koodi = input("Anna ICAO-koodi, saat lentokentän nimen ja kunnan: ")

def haelentokenttä(icao):
    tuple = (icao,)
    sql = """SELECT name, municipality FROM airport WHERE ident = %s"""
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos;


yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user = 'root',
    password = 'p0lnud123',
    autocommit=True
    )

kentta = haelentokenttä(koodi)
if kentta is not None:
    print(f'Nimi: {kentta[0]}\nKunta: {kentta[1]}')
else:
    print("ICAO-koodia ei löydy.")