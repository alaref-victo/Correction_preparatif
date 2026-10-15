texte = input("Entrez du texte : ")


# Il est important de choisir des permissions qui permette l'ecriture dans un fichier
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write(texte)