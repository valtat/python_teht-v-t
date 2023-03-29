from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def kentan_haku(ICAO):
    try:
        def haelentokentta(ICAO):
            tuple = (ICAO,)
            sql = """SELECT name, municipality FROM airport WHERE ident = %s"""
            kursori = yhteys.cursor()
            kursori.execute(sql, tuple)
            tulos = kursori.fetchone()
            return tulos

        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='p0lnud123',
            autocommit=True
        )

        kentta = haelentokentta(ICAO)
        kentan_nimi = kentta[0]
        kentan_kunta = kentta[1]

        tilakoodi = 200
        vastaus = {
            "ICAO": ICAO,
            "Name": kentan_nimi,
            "Municipality": kentan_kunta
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO-koodi."
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)