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
    # classe = request.args['c']    # cree une erreur si c n existe pas dans l'url
    classe = request.args.get('c')
    if classe:
        eleves_selectionnes = [ eleve for eleve in liste_eleves if eleve['classe'] == classe ]
    else:
        eleves_selectionnes = []
    print(classe)
    return render_template("eleves.html", eleves=eleves_selectionnes)


if __name__ == '__main__':
    app.run(debug=True)