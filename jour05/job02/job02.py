hauteur = int(input("Entrer un nombre pour la hauteur:"))
largeur = int(input("Entrer un nombre pour la largeur(plus grand que 2:"))
cote = "|"
haut_bas = "-"
for i in range(hauteur):
    if i == 0 or i == hauteur - 1:
        print(cote + haut_bas * (largeur - 2) + cote)
    else:
        print(cote + ' ' * (largeur - 2) + cote)
