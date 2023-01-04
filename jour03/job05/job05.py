for nombre_premier in range(2, 1000 + 1):
    if nombre_premier > 1:
        for i in range(2, nombre_premier):
            if (nombre_premier % i) == 0:
                break
        else:
            print(nombre_premier)
