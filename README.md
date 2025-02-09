# Tuto Flask

[source du tuto](https://www.youtube.com/watch?v=Ihp_cG7c2Rk&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs)

1. [Decouverte du framework, routes & templates](https://www.youtube.com/watch?v=Ihp_cG7c2Rk&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=1)
2. [Transmettre des parametres dans l'URL](https://www.youtube.com/watch?v=lvxqvNXniVc&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=2)
3. [Formulaires, methodes GET et POST](https://www.youtube.com/watch?v=FdA1P7dY_18&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=3)
4. [Fichiers statiques et heritages de templates](https://www.youtube.com/watch?v=urp_b3bWcfE&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=4)
5. [Les sessions pour memoriser des informations](https://www.youtube.com/watch?v=QAhZ8nmmYxw&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=5)
6. [Le jeu du nombre mystere](https://www.youtube.com/watch?v=QAhZ8nmmYxw&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=6)

TODO

7. [Un clone de DALL-E](https://www.youtube.com/watch?v=wuKuDXaQ8kE&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=7) 
8. [Utiliser des variables d'environnement dans un projet](https://www.youtube.com/watch?v=wuKuDXaQ8kE&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=8)

Decouverte du framework, routes & templates
===========================================

- La presence de 
```python
if __name__ == '__main__':
    app.run(debug=True)>
```
permet de lancer le programme ainsi:
```
python mon_app.py
```
sinon il faut lancer le programme Flask ainsi:
```
flask --app mo_app run --debug
```

- On peut trouver la structure d'un programme Flask minimal [ici](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application), il correspond a ceci:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def bonjour():
    return "<p>Hello, World!</p>"
```


1. l'utilisateur saisie l'url '/'
2. le serveur recoit la requete GET sur la route /
3. flask appelle la fonction bonjour()
4. la fonction renvoit au navigateur le template index.html
5. le navigateur affiche cette page a l'ecran


Resume
------

- Flask permet de creer une application web
- on ajoute des routes via les decorateurs
- chacune de ces routes est associee a une fonction
- lorsque l'utilisateur va envoyer une certaine url 
- Flask va determiner quelle est la route demandee
- Flask va executer la fonction associee
- cette fonction va retourner le template correspondant
- qui est un document htlm
- on peut creer a ce template des variables pour creer des pages dynamiques