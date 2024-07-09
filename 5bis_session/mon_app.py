# mon_app.py

from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

# $ python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = '4b1becb0d665e692d5185628dc8a9d9378c1fca8d48a5bf481b8ed12ba35cdcd'


@app.route("/")
def index():
    return render_template('index.html', titre="Accueil")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Logique de connexion (validation, etc.)
        session['logged_in'] =True
        
        # redirige l'utilisateur vers une autre route associe a la fonction index()
        # qui a son tour utilisera render_template () pour afficher une page
        return redirect(url_for('index'))

    # retourne la page login.html    
    return render_template('login.html', titre="Connexion")


if __name__ == '__main__':
    app.run(host='192.168.1.13', port=5001, debug=True)