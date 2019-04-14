# -*utf-8*



class Dico():

    def __init__(self):
        #Construction des 2 listes
        self._liste_clé = list()
        self._liste_valeur = list()
        self.liste_dico = list()
        self.indice_fin = len(self.liste_dico)
        self.indice_debut = 0

    def copi(self,un_dico):

        keys = list()
        values = list()
        for cle, valeur in un_dico:
            keys.append(cle)
            values.append(valeur)
        self._liste_clé = keys
        self ._liste_valeur = valeur
    def __repr__(self):
        return self.liste_dico

    def __str__(self):


        return "{}".format(self.liste_dico)

    def __setitem__(self, key, value):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
                On redirige vers self._dictionnaire[index] = valeur"""

        #self._dictio[key] = value
        #self._liste_clé.remove(key)
        #self._liste_valeur.append(value)
        if key in self._liste_clé:
            for i, elt in enumerate(self._liste_clé):
                if key == elt:
                    num_indice = i
            del self._liste_valeur[num_indice]
            del self.liste_dico[num_indice]
            self._liste_valeur.insert(num_indice, value)
        else:

            self._liste_clé.append(key)
            self._liste_valeur.append(value)
            self.liste_dico.append(key+" : "+value)

    def __delitem__(self, key):
        if key in self._liste_clé:
            indice = self._liste_clé.index(key)
            self._liste_clé.remove(key)
            del self._liste_valeur[indice]
            del self.liste_dico[indice]

    def __contains__(self, key):
         if key in self._liste_clé:
             print("True")
         else:
            print("False")
    def __len__(self):
        return len(self._liste_clé)

    """def __lt__(self, key):
        return self.liste_dico.sort()"""

    """def __iter__(self):
        i=0
        for cle in self.liste_dico:

            print(cle)"""
    def __iter__(self):
        return self

    def __next__(self):
        zer = len(self)
        if self.indice_debut >= zer:
            raise StopIteration
        else:
            x = self.indice_debut
            self.indice_debut += 1
            return self.liste_dico[x]
    def _get_liste_clé(self):
        return self._liste_clé
    def _get_liste_valeur(self):
        return self._liste_valeur

    


    liste_clé = property(_get_liste_clé)
    liste_valeur = property(_get_liste_valeur)

"""mon_dico["clé one"]="the first"
mon_dico["clé two"]="the second"
mon_dico["clé one"]="la premiere"
del mon_dico["clé two"]

print(mon_dico)
print("{} {}".format(mon_dico._liste_clé, mon_dico._liste_valeur))"""

mon_dico = Dico()
#mon_dico["clé six"]="la 6"
mon_dico["clé six"]="6"
mon_dico["clé sept"]="7"
del mon_dico["clé sept"]
mon_dico["clé dix"]="10"
print("{} : {}".format(mon_dico._liste_clé, mon_dico._liste_valeur))
print(mon_dico)

"clé six" in mon_dico
print(len(mon_dico))
print(mon_dico)


for i in mon_dico:
    print(i)

for i in mon_dico.liste_clé:
    print(i)
for i in mon_dico.liste_valeur:
    print(i)

for i in mon_dico.keys:
    print(i)

