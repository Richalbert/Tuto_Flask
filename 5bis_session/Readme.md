render_template('index.html') VS redirect(url_for('index'))
===========================================================


Dans un cas on parle du fichier html, dans l'autre cas il s'agit d'appeler la fonction python index()



```python
render_template('index.html')
```

- cette fonction genere la reponse HTTP en rendant le fichier _index.html' situe dans le repertoire _templates_






```python
redirect(url_for('index'))
```

- cette fonction genere une reponse HTTP de redirection (code 302) vers l'URL correspondant a la route associee a la fonction index()

