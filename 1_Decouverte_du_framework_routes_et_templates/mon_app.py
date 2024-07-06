# mon_app.py

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template('index.html')

@app.route("/heure")
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template('heure.html', heure=h, minute=m, seconde=s)
    # return f"l'heure actuelle est {h}:{m}:{s}"


if __name__ == '__main__':
    app.run(debug=True)