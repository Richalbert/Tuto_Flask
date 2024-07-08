TUTORIEL FLASK #3 : Formulaires, methodes GET et POST
=====================================================


[source du tuto](https://www.youtube.com/watch?v=FdA1P7dY_18&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=3)


Comment les donnees saisies par un utilisateur sont transmises au serveur
- soit par la methode GET
- soit par la methode POST

Les formulaires
---------------

- inclus dans une balise *form*
- la balise *form* a toujours 2 attributs, *action* et *method*
- GET par defaut
- action="" correspond a la route sur le serveur ou va etre transmis la requete
- la route par defaut (si on ne met rien) est la page actuelle
- on pourait ecrire en dur la route, par ex action="/traitement", mais avec Flask on prefere
- utiliser **action="{{ url_for('traitement') }}** et definir a qui on va transmettre les donnees
- on passe donc le nom de la fonction associee a la route et non la route

### Resume

si la method est GET alors les donnees sont tranmise au serveur via l'URL
et on peut recuperer ces valeurs avec *request.args* qui est un dictionnaire passe en parametre
une requete GET n'est pas adaptee a l'envoi de donnees sensible au serveur


### avec la methode POST
- les donnees ne sont plus transmise dans l'URL
- mais n'est pas un gage de securite (cf onglet requete de l'inspecteur)
- pour plus de securite il faut coupler l'envoi de la requete avec le protocole HTTPS
- une route par defaut n'accepte pas la methode POST, il faut ecrire
- *request.args* devient un dictionnaire vide puisque cela correspond au donnees transmise dans l'URL
- *request.form* est l'objet qui permet de recuperer les donnees du formulaire avec POST




Les elements de type *text*
---------------------------

- balise *for* et *id* doivent avoir la meme valeur
```html 
  <label for="nom">
  <input type="text" id="nom">
```

Les elements de type *password*
-------------------------------

- le contenu est masque par defaut
```html 
  <label for="mdp">
  <input type="password" id="mdp">
```

Les elements de type *email*
----------------------------

Les elements de type *radio*
----------------------------

- choix entre plusieurs options
- on en selectionne qu'une seule
- si on a plusieurs choix, il faut que l'attribut *name* soit le meme pour les lier
```html 
  <input type="radio" id="choix1" name="chocolat">
  <label for="choix1">

  <input type="radio" id="choix2" name="chocolat">
  <label for="choix2">
```

Les listes d'options
--------------------

- menu deroulant avec plusieurs options

Les textes sur plusieurs lignes
-------------------------------


Les boutons 
-----------


dans la requete le nom du champ *name* apparait comme cle dans l'url transmise et la valeur ce qui aura ete saisie

... ?nom=toto&mdp=titi&email=toto%40toto.fr&transport=Velo&commentaire=

donc les parametres sont attribues par chaque champ *name* de la balise *input*