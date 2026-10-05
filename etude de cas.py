# 1.a.i — Créer une classe Livre avec les attributs demandés.
class Livre:

    # 1.a.ii — Le constructeur __init__
    def __init__(self, titre, auteur, annee, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible

    # 1.a.iii — Méthode emprunter
    def emprunter(self):
        if self.disponible == True:
            self.disponible = False
            return "Livre emprunté !"
        else:
            return "Indisponible."

    # 1.a.iv — Méthode retourner
    def retourner(self):
        if not self.disponible:
            self.disponible = True
        return "Livre retourné."

    # 1.a.v — Méthode __str__
    def __str__(self):
        disponibilite = "Oui" if self.disponible else "Non"

        return f"Titre : {self.titre}, Auteur : {self.auteur}, Année : {self.annee}, Disponible : {disponibilite}"


# 2.a.i — Créer Roman qui hérite de Livre
class Roman(Livre):

    # 2.a.ii — Ajouter l'attribut genre et utiliser super()
    def __init__(self, titre, auteur, annee, genre, disponible=True):
        super().__init__(titre, auteur, annee, disponible)
        self.genre = genre

    # 2.a.iii — Surcharger __str__
    def __str__(self):
        disponibilite = "Oui" if self.disponible else "Non"

        return f"Titre : {self.titre}, Auteur : {self.auteur}, Année : {self.annee}, Disponible : {disponibilite}, Genre : {self.genre}"


# 3.a.i — Créer la classe avec une liste de livres vide
class Bibliotheque:

    def __init__(self):
        self.livres = []

    # 3.a.ii — Méthode ajouter_livre
    def ajouter_livre(self, livre):
        self.livres.append(livre)

    # 3.a.iii — Méthode lister_livres
    def lister_livres(self):
        return [str(livre) for livre in self.livres]

    # 3.a.iv — Méthode emprunter_livre
    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                return livre.emprunter()

        return "Livre non trouvé."


# 4.a — Créer une bibliothèque et ajouter 2 livres
bibliotheque = Bibliotheque()

livre1 = Livre(
    "Le Petit Prince",
    "Antoine de Saint-Exupéry",
    1943
)

roman1 = Roman(
    "Harry Potter à l'école des sorciers",
    "J.K. Rowling",
    1997,
    "Fantastique"
)

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(roman1)


# Test 1 : lister les livres de la bibliothèque
print("=== LIVRES AU DEPART ===")

for livre in bibliotheque.lister_livres():
    print(livre)


# Test 2 : emprunter un livre
print("\n=== EMPRUNT DU PETIT PRINCE ===")

print(bibliotheque.emprunter_livre("Le Petit Prince"))


# Test 3 : lister les livres après emprunt
print("\n=== LIVRES APRES EMPRUNT ===")

for livre in bibliotheque.lister_livres():
    print(livre)


# Test 4 : retourner un livre
print("\n=== RETOUR DU PETIT PRINCE ===")

print(livre1.retourner())


# Test 5 : lister les livres après retour
print("\n=== LIVRES APRES RETOUR ===")

for livre in bibliotheque.lister_livres():
    print(livre)