def legume_fruits_saison(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")


legume_fruits_saison("fruits", "hiver")
legume_fruits_saison("fruits", "ete")
legume_fruits_saison("legume", "hiver")
legume_fruits_saison("legume", "ete")
