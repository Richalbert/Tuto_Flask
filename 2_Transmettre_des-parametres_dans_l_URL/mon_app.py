# mon_app.py

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template('index.html')


liste_eleves = [
    {'nom': 'Dupont', 'prenom': 'Jean', 'classe': '2A'},
    {'nom': 'Dupont', 'prenom': 'Jeanne', 'classe': 'TG2'},
    {'nom': 'Marchand', 'prenom': 'Marie', 'classe': '2A'},
    {'nom': 'Martin', 'prenom': 'Adeline', 'classe': '1G1'},
    {'nom': 'Dupont', 'prenom': 'Lucas', 'classe': '2A'}
]


@app.route("/eleves")
def eleves():
    print(request.args['c'])
    print(request.args['autre'])
    return render_template("eleves.html", eleves=liste_eleves)


if __name__ == '__main__':
    app.run(debug=True)