def parcours(nombre_marches, hauteur_marche):
    distance = 2 * nombre_marches * hauteur_marche
    distance_semaine = distance * 5 * 7
    return distance_semaine / 100


nombre_marches = input("Entrer le nombre de marches : ")
hauteur_marche = input("Entrer la hauteur des marches en cm : ")
nombre_marches = int(nombre_marches)
hauteur_marche = int(hauteur_marche)
distance = parcours(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcours {distance} m par semaine.")
