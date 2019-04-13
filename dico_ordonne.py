# -*utf-8*

class Dico():

    def __init__(self):
        #Construction des 2 listes
        self._liste_clé = list()
        self._liste_valeur = list()
        self._dictio={}

    def copi(self,un_dico):

        keys = list()
        values = list()
        for cle, valeur in un_dico:
            keys.append(cle)
            values.append(valeur)
            self._dictio[keys]=values
        self._liste_clé = keys
        self ._liste_valeur = valeur


    def __str__(self):

        return "{}".format(self._dictio)

    def __setitem__(self, key, value):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
                On redirige vers self._dictionnaire[index] = valeur"""

        self._dictio[key] = value
        self._liste_clé.append(key)
        self._liste_valeur.append(value)
    def __delitem__(self, key):
        del self._dictio[key]
        
didi={}
didi["clé 1"]=1
didi["clé 2"]=2

mon_dico = Dico()

mon_dico["clé one"]="the first"
mon_dico["clé two"]="the second"
mon_dico["clé one"]="la premiere"
del mon_dico["clé two"]

print(mon_dico)

