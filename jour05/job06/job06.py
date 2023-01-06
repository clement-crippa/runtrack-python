def arrondir(note_initial):
    arrondies = []
    for note_arrondie in note_initial:
        if note_arrondie < 40:
            arrondies.append(note_arrondie)
        else:
            if note_arrondie % 5 < 3:
                arrondies.append(note_arrondie - note_arrondie % 5)
            else:
                arrondies.append(note_arrondie + (5 - note_arrondie % 5))
    return arrondies


print(arrondir([30, 39, 40, 46, 41, 90, 96, 74, 83, 82]))
