# Plusieurs maniere de faire
lettre = "z"
chaine = "abcdefghz"

# la facon classique
def contient_lettre1(chaine, lettre):
    for c in chaine:
        if c == lettre:
            return True
    return False


# un maniere plus facile avec le mot cle in
def contient_lettre2(chaine, lettre):
    return lettre in chaine
    

print(contient_lettre1(chaine,lettre))
print(contient_lettre1(chaine,"x"))

print(contient_lettre2(chaine,lettre))
print(contient_lettre2(chaine,"x"))