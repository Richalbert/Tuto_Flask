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


@app.route("/traitement")
def traitement():
    # return render_template('traitement.html')
    print(request.args)
    return "Traitement des donnees"



if __name__ == '__main__':
    app.run(debug=True)