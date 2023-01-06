L = [10, 8, 12, 13, 4]
print(L[1])


def somme_voisines():
    result = L[2] + L[4]
    L.insert(3, result)
    print(L[3])
    print(L[-1])


somme_voisines()
