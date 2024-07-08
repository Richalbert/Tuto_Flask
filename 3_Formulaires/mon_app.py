# mon_app.py

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template('index.html')



@app.route("/formulaires")
def formulaires():
    return render_template('formulaires.html')



@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/traitement", methods=['POST'])
def traitement():
    # return render_template('traitement.html')
    # print(request.args)
    donnees = request.form
    # print(donnees)
    # nom = donnees['nom']
    nom = donnees.get('nom')
    mdp = donnees.get('mdp')
    # print(nom, mdp)
    if nom=='admin' and mdp=='1234':
        return f"Bonjour {nom}, vous etes connecte"
    else:
        return "un probleme est survenu"



if __name__ == '__main__':
    app.run(debug=True)