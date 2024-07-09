# mon_app.py

from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)

# cle secrete de session pour les cookies
app.secret_key = "dd54c000bc824ffafd342864a7f8ae027c3ebb9c6455963de25d042f427d5066"

# les cookies de sessions ne sont pas conserves et detruit a la fermeture du navigateur
#app.config['SESSION_PERMANENT'] = False

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/formulaires")
def formulaires():
    return render_template('formulaires.html')



@app.route("/login")
def login():
    return render_template('login.html')



@app.route("/compteur")
def compteur():
    visite = 0
    # si la cle compteur n'est pas dans le dictionaire session
    if "compteur" not in session:
        session['compteur'] = 1
    else:
        session['compteur'] += 1

    print(session)

    visite = session['compteur']
    return f"Nombre de visites : {visite}"








@app.route("/traitement", methods=['POST', 'GET'])
def traitement():

    if request.method == 'POST':
        donnees = request.form
    
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
    
        if nom=='admin' and mdp=='1234':
            return render_template('traitement.html', nom_utilisateur=nom)
        else:
            return render_template('traitement.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)