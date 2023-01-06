L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste = []
for i in L:
    if i not in liste:
        liste += [i]
print(liste)
