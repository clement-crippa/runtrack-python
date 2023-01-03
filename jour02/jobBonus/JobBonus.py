def triangle(ab, ac, bc):
    if (ab + ac > bc) and (ab + bc > ac) and (bc + ac > ab):
        print("Il est possible de construire un triangle")
        if (bc * bc == (ac * ac) + (ab * ab)) and (ab == ac or ab == bc or ac == bc) or (
                ab * ab == (ac * ac) + (bc * bc)) and (ab == ac or ab == bc or ac == bc) or (
                ac * ac == (bc * bc) + (ab * ab)) and (ab == ac or ab == bc or ac == bc):
            print("C'est un triangle rectangle isocèle")
        elif (bc * bc == (ac * ac) + (ab * ab)) or (ab * ab == (ac * ac) + (bc * bc)) or (
                ac * ac == (bc * bc) + (ab * ab)):
            print("C'est un triangle rectangle")
        elif ab == ac == bc:
            print("C'est un triangle équilatéral")
        elif ab == ac or ab == bc or ac == bc:
            print("C'est un triangle isocèle")
        else:
            print("C'est un triangle quelconque")
    else:
        print("Il n'est pas possible de construire un triangle")


triangle(8, 8, 8)
triangle(8, 8, 10)
triangle(float(5.5), float(7.3), float(4.8))
triangle(float(3), float(5.5), float(7.5))
triangle(1, 2, 10)
