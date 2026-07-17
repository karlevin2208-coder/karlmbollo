# Creer un dictionnaire fruits
Fruits = {
"Pomme": "rouge",
"Banane": "jaune",
"Orange": "orange"
}

# Ajouter la cle Kiwi de valeur vert
Fruits["Kiwi"] = "vert"

# Acces a la valeur de la cle Banane, et stockons la dans couleur_banane
couleur_banane = Fruits["Banane"]

# Modifions la valeur associe a la cle pomme pour vert
Fruits["Pomme"] = "vert"

# Supprimons la cle orange
del Fruits["Orange"]

# Affichons les cles restantes dans le dictionnaire
print(Fruits.keys())
