Explication du projet :

classe qui crée 2 listes :
	- 1 liste contient les clés
	- 1 liste qui contient les valeurs
Les clés et les valeurs doivent toujours être associé (comme si c'était un vrai dico)

l'ordre d'ajout est important, pour trier ou/et inverser.

1) On doit pouvoir créer le dico du plusieurs façon :
 *Vide : on appelle le constructeur sans lui passer aucun paramètre et le dictionnaire créé est donc vide. ////////////// OK //////////////////////

 *Copié depuis un dictionnaire: on passe en paramètre du constructeur un dictionnaire que l'on copie par la suite dans notre objet. On peut ainsi écrire constructeur(dictionnaire) et les clés et valeurs contenues dans le dictionnaire sont copiées dans l'objet construit.
 *Pré-rempli grâce à des clés et valeurs passées en paramètre : comme les dictionnaires usuels, on doit ici avoir la possibilité de pré-remplir notre objet avec des couples clés-valeurs passés en paramètre (constructeur(cle1 = valeur1, cle2 = valeur2, …)).

2) clés et valeur sont associé, si on supprime une clé la valeur est supprimée aussi. liste valeur et liste clé sont de même taille.
///////////////////// OK //////////////////////

3) On doit pouvoir faire objet[cle]=valeur pour la modifier ou del objet[cle] pour la supprimer.
//////////////////// OK  /////////////////////

4) Quand on modifie une valeur elle écrase la valeur précédent
//////////////////// OK //////////////////////

5) On doit pouvoir savoir grâce au mot-clé in si une clé se trouve dans notre dictionnaire (cle in dictionnaire).

6) len(dictionnaire) doit fonctionner.

7) print(dictionnaire) doit l'afficher comme un print sur un dictionnaire classique : exemple : {cle1: valeur1, cle2: valeur2, …}

8) Créer méthodes pour trier (avec sort) et pour inverser (avec reverse).
Le tri dois se faire en fonction des clés.

9) L'objet doit pouvoir être parcouru. Quand on écrit for cle in dictionnaire, on doit parcourir la liste des clés contenues dans le dictionnaire.

10) À l'instar des dictionnaires, trois méthodes keys() (renvoyant la liste des clés), values() (renvoyant la liste des valeurs) et items() (renvoyant les couples (clé, valeur)) doivent être mises en œuvre. Le type de retour de ces méthodes est laissé à votre initiative : il peut s'agir d'itérateurs ou de générateurs (tant qu'on peut les parcourir).

11) On doit pouvoir ajouter deux dictionnaires ordonnés (dico1 + dico2) ; les clés et valeurs du second dictionnaire sont ajoutées au premier.
