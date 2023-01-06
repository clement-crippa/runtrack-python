L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
liste = len(L)
multiplication = 1

for i in range(liste):
    if 25 <= L[i] <= 90:
        multiplication = multiplication * L[i]
print(multiplication)
