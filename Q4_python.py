def lire_fichier_en_mots(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
    
    print(contenu.split())
    return contenu.split()   


def trouver_mot(liste_mots, mot):
    return mot in liste_mots   


print(trouver_mot(lire_fichier_en_mots("texte.txt"), "Sense"))