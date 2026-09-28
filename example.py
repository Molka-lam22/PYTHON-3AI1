produit = "ordinateur"
prix = 79.99
stock = 25

print("produit : " + produit + "- Prix : " + str(prix))
print("Stock disponible : " + str(stock))
prix_ttc =[12.99, 15.99, 19.99, 24.99, 29.99]
prix_ht =[]
for prix in prix_ttc:
    prix_ht.append(round(prix / 1.2, 3))

print("Prix HT : " + str(prix_ht))

prix_ht_1 = [round(prix / 1.2, 3) for prix in prix_ttc]
print(prix_ht_1)

prix_sup = [ prix for prix in prix_ttc if prix >= 15]
print(prix_sup)

articles = ["ordinateur", "souris", "clavier", "écran"]
catalogue = {
    art: round(prix * 0.9, 2)
    for art, p in zip(articles, prix_ttc)
    if prix > 20
}
print("catalogue filtré :" , catalogue)

def calcul(prix, tva): 
    return round(prix * (1 + tva), 2)
print(calcul(100, 0.2))

