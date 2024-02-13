liste_originale = [1, 7, 9, 3, 0, 2]


def total_fichier_liste(liste):
    try:
        total = 0
        f = open('fichier_inexistant.txt', 'r')
        x = 0
        for ligne in f.read():
            total += liste[x] + str(ligne)
            x += 1
        return total
    except FileNotFoundError:
        print('Le fichier n\'existe pas')
        raise
    finally:
        liste.clear()
        return


print(total_fichier_liste(liste_originale))

# Expliquer pourquoi dans le code précédent, même si le fichier est inexistant et qu’il devrait engendrer
# une exception FileNotFoundError, l’exception ne sera jamais déclenchée
