from flask import Flask
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def summa(luku):
    try:
        luku = int(luku)
        boolean = False
        if luku <= 1:
            boolean == False
        else:
            for i in range(2, luku):
                if (luku % i) == 0:
                    break
            else:
                boolean == True

        vastaus = {
            "Number": luku,
            "isPrime": boolean
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
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