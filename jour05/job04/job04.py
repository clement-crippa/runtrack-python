message = input("Entrer un mot (sans espace) a crypter: ")
message = message.lower()
cryptage = ""
cryptage_gauche = ""
for i in range(len(message)):
    lettre = message[i]
    decallage = 2
    decallage_gauche = -4
    # Lettre Minuscule UNICODE
    cryptage += chr((ord(lettre) + decallage - 96) % 26 + 97)
    cryptage_gauche += chr((ord(lettre) + decallage_gauche - 96) % 26 + 97)
print("Decallage droite:", cryptage)
print("Decallage gauche:", cryptage_gauche)
