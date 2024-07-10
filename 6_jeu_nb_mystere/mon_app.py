# mon_app.py

from flask import Flask, render_template, request, redirect, url_for, session
from random import randint

app = Flask(__name__)

# cle secrete de session pour les cookies
app.secret_key = "dd54c000bc824ffafd342864a7f8ae027c3ebb9c6455963de25d042f427d5066"

# les cookies de sessions ne sont pas conserves et detruit a la fermeture du navigateur
#app.config['SESSION_PERMANENT'] = False

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/jeu", methods=['POST', 'GET'])
def jeu():
    if request.method == 'POST':
        # traiter les donnees du formulaire
        reponse = int(request.form.get('nombre'))   # on recupere la donnee 'name' du formulaire
        if reponse == session['nb_mystere']:
            message = "Bravo, c'est gagne"
        elif reponse < session['nb_mystere']:
            message = "Votre nombre est trop petit"
        else:
            message = "Votre nombre est trop grand"
        print(session)
        return render_template('nombre-mystere.html', message=message)
    else:
        # debut de partie
        nb_mystere = randint(0, 100)            # on cree le nb_mystere
        session['nb_mystere'] = nb_mystere      # on memorise le nb mystere
        print(session)
        
        # afficher le formulaire
        return render_template("nombre-mystere.html")



# un tableau d'utilisateurs (dictionnaoire)
utilisateurs = [
    {"nom": "admin", "mdp": "1234"},
    {"nom": "marie", "mdp": "1234"},
    {"nom": "paul", "mdp": "1234"},
]


def recherche_utilisateurs(nom_utilisateur, mot_de_passe):
    for utilsateur in utilisateurs:
        if utilsateur['nom'] == nom_utilisateur and utilsateur['mdp'] == mot_de_passe:
            return utilsateur
    return None


@app.route("/formulaires")
def formulaires():
    return render_template('formulaires.html')


'''La fonction login() affiche le formulaire et 
   realise le traitement des donnees saisies'''
@app.route("/login", methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')

        utilisateur = recherche_utilisateurs(nom, mdp)

        if utilisateur is not None:
            print("utilsateur trouve")
            session['nom_utilisateur'] = utilisateur['nom']
            print(session)
            return redirect(url_for('index'))
        else:
            print( 'utilisateur inconnu')
            return redirect(request.url)    
    else: 
        print(session)
        if 'nom_utilisateur' in session:
            return redirect(url_for('index'))
       
        return render_template('login.html')


@app.route('/logout')
def logout():
    print(session)
    session.pop('nom_utilisateur', None)
    print(session)
    return redirect(url_for('login'))


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