def tapis_final(taille_tapis):
    coin = "+"
    tapis = "#"
    cote = "|"
    haut_bas = "-"
    taille = taille_tapis + 1
    diagonal = taille_tapis
    for i in range(taille):
        ligne = coin if i == 0 or i == taille - 1 else cote
        if i == 0 or i == taille - 1:
            ligne += haut_bas * (taille - 2) + coin
        else:
            ligne += tapis * (diagonal - 2)
            ligne += " "
            ligne += tapis * (taille_tapis - diagonal) + cote
        print(ligne)
        diagonal = diagonal - 1 if i > 0 else diagonal


tapis_final(15)
