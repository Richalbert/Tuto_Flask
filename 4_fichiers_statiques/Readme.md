TUTORIEL FLASK #4 : Fichiers statiques et heritage de templates
===============================================================


[source du tuto](https://www.youtube.com/watch?v=FdA1P7dY_18&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=4)


1. Fichiers statiques
   
   - css, 
   - .js, 
   - images

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

    - 1er parametre indique le nom du dossier, ici *static*
    - le 2nd parametre indique le chemin dans se dossier au fichier

2. Heritage de templates

   -  parfois les pages ont le meme aspect et plutot de reecrire les pages, on va re-utiliser les parties communes
   -  on cree un template commun a toutes les pages du site
   -  soit *base.html* le squelette de base du site
   -  les balises *head* sont communes a toutes les pages
   -  les balises *nav* de navigation sont communes 
   -  et on cree un *block* que l'on nomme *content*
  
  et voici la partie de la page qui va differer d'une page a l'autre
  ```html
  {% block content %}{% endblock %}
    ```