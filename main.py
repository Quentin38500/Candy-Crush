import random
import matplotlib.pyplot as plt
import copy


def generate_grid(size, colors):
    """
    Cette fonction génère une grille de taille size x size remplie de bonbons de couleur aléatoire.

    Paramètres :
    size (int) : taille de la grille
    colors (list) : liste des couleurs utilisées

    Retour :
    grid (list) : grille de jeu
    """
    grid = []
    for i in range(size):
        l = []
        for j in range(size):
            l.append(random.choice(colors))
        grid.append(l)
    return grid


def ask_coordinates():
    """
    Cette fonction demande à l'utilisateur de choisir les coordonnées d'un bonbon.

    Retour :
    (int(x), int(y)) (tuple) : tuple contenant les coordonnées X et Y du bonbon
    """
    x, y = input("Numéro de ligne : "), input("Numéro de colonne : ")
    return int(x), int(y)


def swap(grid):
    """
    Cette fonction permet d'échanger deux bonbons.

    Paramètre :
    grid (list) : grille de jeu
    """
    candy_1 = ask_coordinates()
    candy_2 = ask_coordinates()

    # On créé une copie de la liste afin de vérifier que l'échange amène bien à une combinaison
    grid_copy = copy.deepcopy(grid)

    # On simule l'échange des bonbons dans la copie de la liste
    grid_copy[candy_1[0]][candy_1[1]], grid_copy[candy_2[0]][candy_2[1]] = grid_copy[candy_2[0]][candy_2[1]], grid_copy[candy_1[0]][candy_1[1]]

    # Échange des deux bonbons dans la grille de jeu
    # On vérifie que les bonbons sont bien adjacents
    if not ((candy_1[0] == candy_2[0] + 1 and candy_1[1] == candy_2[1]) or (candy_1[0] == candy_2[0] - 1 and candy_1[1] == candy_2[1]) or (candy_1[1] == candy_2[1] + 1 and candy_1[0] == candy_2[0]) or (candy_1[1] == candy_2[1] - 1 and candy_1[0] == candy_2[0])):
        print("Ce déplacement n'est pas possible car les bonbons ne sont pas adjacents")

    # On vérifie que l'échange amène bien à une combinaison
    elif (not detecte_coordonnees_combinaison(grid_copy, candy_1[0], candy_1[1], size) and not detecte_coordonnees_combinaison(grid_copy, candy_1[0]-1, candy_1[1], size) and not detecte_coordonnees_combinaison(grid_copy, candy_1[0]+1, candy_1[1], size) and not detecte_coordonnees_combinaison(grid_copy, candy_1[0], candy_1[1]-1, size) and not detecte_coordonnees_combinaison(grid_copy, candy_1[0], candy_1[1]+1, size)) and (not detecte_coordonnees_combinaison(grid_copy, candy_2[0], candy_2[1], size) and not detecte_coordonnees_combinaison(grid_copy, candy_2[0]-1, candy_2[1], size) and not detecte_coordonnees_combinaison(grid_copy, candy_2[0]+1, candy_2[1], size) and not detecte_coordonnees_combinaison(grid_copy, candy_2[0], candy_2[1]-1, size) and not detecte_coordonnees_combinaison(grid_copy, candy_2[0], candy_2[1]+1, size)):
        print("Ce déplacement n'est pas possible car il n'amène pas à une combinaison")
    else:
        grid[candy_1[0]][candy_1[1]], grid[candy_2[0]][candy_2[1]] = grid[candy_2[0]][candy_2[1]], grid[candy_1[0]][candy_1[1]]


def detecte_coordonnes_vertical(grid, x, y, size):
    """
    Cette fonction permet de répertorier les coordonnées des bonbons faisant partie d'une combinaison verticale.

    Paramètres :
    grid (list) : grille de jeu
    x (int) : coordonnée X du bonbon
    y (int) coordonnée Y du bonbon
    size (int) : taille de la grille

    Retour :
    [(x, y), (x+1, y), (x-1, y)] (list) : liste comprenant les coordonnées des bonbons faisant partie de la combinaison
    """
    # Vérification de l'existence d'une combinaison verticale de 3 bonbons
    if 0 <= x < size and x - 1 >= 0 and x + 1 < size and grid[x][y] == grid[x + 1][y] and grid[x][y] == grid[x - 1][y]:
        return [(x, y), (x + 1, y), (x - 1, y)]
    else:
        return []


def detecte_coordonnes_horizontal(grid, x, y, size):
    """
    Cette fonction permet de répertorier les coordonnées des bonbons faisant partie d'une combinaison horizontale.

    Paramètres :
    grid (list) : grille de jeu
    x (int) : coordonnée X du bonbon
    y (int) coordonnée Y du bonbon
    size (int) : taille de la grille

    Retour :
    [(x, y), (x, y+1), (x, y-1)] (list) : liste comprenant les coordonnées des bonbons faisant partie de la combinaison
    """
    # Vérification de l'existence d'une combinaison horizontale de 3 bonbons
    if 0 <= x < size and y - 1 >= 0 and y + 1 < size and grid[x][y] == grid[x][y + 1] and grid[x][y] == grid[x][y - 1]:
        return [(x, y), (x, y + 1), (x, y - 1)]
    else:
        return []


def detecte_coordonnees_combinaison(grid, x, y, size):
    """
    Cette fonction permet de répertorier les coordonnées des bonbons faisant partie d'une combinaison.

    Paramètres :
    grid (list) : grille de jeu
    x (int) : coordonnée X du bonbon
    y (int) coordonnée Y du bonbon
    size (int) : taille de la grille

    Retour :
    coordonnees (list) : liste comprenant les coordonnées des bonbons faisant partie d'une combinaison
    """
    # Somme des combinaisons verticales et horizontales
    coordonnees = detecte_coordonnes_vertical(grid, x, y, size) + detecte_coordonnes_horizontal(grid, x, y, size)

    # Passage à un tuple afin d'éliminer les occurences multiples d'un bonbon
    return list(tuple(coordonnees))


def delete(grid, size):
    """
    Cette fonction assigne la valeur de -1 à chaque bonbon faisant partie d'une combinaison.

    Paramètres :
    grid (list) : grille de jeu
    size (int) : taille de la grille

    Retour :
    deleted (bool) : True si une combinaison a été supprimée, False sinon
    """
    global score

    # La variable "deleted" permet de savoir si toutes les combinaisons ont été supprimées
    deleted = False

    # La liste "toutes_combinaisons" contient l'ensemble des bonbons faisant partie d'une combinaison
    toutes_combinaisons = []

    # On parcourt tous les bonbons de la grille
    for x in range(size):
        for y in range(size):

            # Pour chaque bonbon, on récupère les coordonnées des combinaisons possibles
            combinaison = detecte_coordonnees_combinaison(grid, x, y, size)

            # On ajoute ces coordonnées à la liste comportant l'ensemble des combinaisons
            toutes_combinaisons.append(combinaison)

    # On assigne la valeur -1 à chaque bonbon faisant partie d'une combinaison
    for i in toutes_combinaisons:
        for j in i:
            print(i)

            # On ajoute tous les bonbons de même valeur qui sont voisins d’un bonbons supprimé à la liste des bonbons à supprimer (niveau 3)
            if j[0]+1 < size and grid[j[0]+1][j[1]] == grid[j[0]][j[1]] and grid[j[0]+1][j[1]] != -1:
                i.append((j[0]+1, j[1]))
                print(i)
            if j[0]-1 >= 0 and grid[j[0]-1][j[1]] == grid[j[0]][j[1]] and grid[j[0]-1][j[1]] != -1:
                i.append((j[0]-1, j[1]))
                print(i)
            if j[1]+1 < size and grid[j[0]][j[1]+1] == grid[j[0]][j[1]] and grid[j[0]][j[1]+1] != -1:
                i.append((j[0], j[1]+1))
                print(i)
            if j[1]-1 >= 0 and grid[j[0]][j[1]-1] == grid[j[0]][j[1]] and grid[j[0]][j[1]-1] != -1:
                i.append((j[0], j[1]-1))
                print(i)

            # On assigne -1 à la valeur du bonbon supprimé
            if grid[j[0]][j[1]] != -1:
                grid[j[0]][j[1]] = -1
                deleted = True
                score += 1
    return deleted


def gravite(grid, size):
    """
    Cette fonction déplace les bonbons vers le bas pour remplir les trous laissés par les bonbons supprimés (simulation de la gravité).

    Paramètres :
    grid (list) : grille de jeu
    size (int) : taille de la grille
    """
    # La variable "change" permet de savoir si tous les changements liés à la gravité ont été effectués
    change = True

    # Tant que tous les changements n'ont pas été effectués
    while change:
        changement = 0

        # On parcourt tous les bonbons jusqu'à l'avant dernière ligne
        for i in range(size - 1):
            for j in range(size):

                # Pour chaque bonbon ayant un bonbon supprimé (-1) en dessous, on le fait descendre
                if grid[i][j] != -1 and grid[i + 1][j] == -1:
                    # Échange des bonbons
                    grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]
                    changement += 1
        if changement == 0:
            change = False


def replace(grid, size, colors):
    """
    Cette fonction remplace les trous laissés par l'application de la fonction gravité avec des bonbons de couleur aléatoire.

    Paramètres :
    grid (list) : grille de jeu
    size (int) : taille de la grille
    colors (list) : liste des couleurs utilisées
    """
    # On parcourt tous les bonbons de la grille
    for i in range(size):
        for j in range(size):

            # On remplace tous les bonbons supprimés (-1) par une couleur aléatoire
            if grid[i][j] == -1:
                grid[i][j] = random.choice(colors)


def affichage_grille(grid, nb_type_bonbons):
    """
    Cette fonction affiche la grille contenant au maximum "nb_type_bonbons" couleurs de bonbons différentes.

    Paramètres :
    grid (list) : grille de jeu
    nb_type_bonbons (int) : nombre de couleurs de bonbons différentes
    """
    plt.imshow(grid, vmin=0, vmax=nb_type_bonbons - 1, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)


def end(grid, size):
    """
    Cette fonction détermine s'il reste des combinaisons possibles dans la grille de jeu.

    Paramètres :
    grid (list) : grille de jeu
    size (int) : taille de la grille

    Retour :
    True si le jeu est fini (plus de combinaisons possibles), False sinon
    """
    # On parcourt tous les bonbons de la liste
    for i in range(size):
        for j in range(size-1):

            # On créé une copie de la liste afin de ne pas la modifier
            grid_copy = copy.deepcopy(grid)

            # On simule l'échange horizontal de deux bonbons
            candy_1 = (i, j)
            candy_2 = (i, j+1)
            grid_copy[candy_1[0]][candy_1[1]], grid_copy[candy_2[0]][candy_2[1]] = grid_copy[candy_2[0]][candy_2[1]], grid_copy[candy_1[0]][
                candy_1[1]]

            # On parcourt la grille afin de vérifier s'il reste des combinaisons possibles avec l'échange effectué précédemment
            for x in range(size):
                for y in range(size):
                    combinaison = detecte_coordonnees_combinaison(grid_copy, x, y, size)

                    # Si au moins une combinaison est possible, le jeu n'est pas terminé donc on renvoie la valeur "False"
                    for k in combinaison:
                        if grid_copy[k[0]][k[1]] != -1:
                            return False

    # On répéte le même algorithme pour l'échange vertical
    for j in range(size):
        for i in range(size-1):
            grid_copy = copy.deepcopy(grid)
            candy_1 = (i, j)
            candy_2 = (i+1, j)
            grid_copy[candy_1[0]][candy_1[1]], grid_copy[candy_2[0]][candy_2[1]] = grid_copy[candy_2[0]][candy_2[1]], grid_copy[candy_1[0]][
                candy_1[1]]
            for x in range(size):
                for y in range(size):
                    combinaison = detecte_coordonnees_combinaison(grid_copy, x, y, size)
                    for k in combinaison:
                        if grid_copy[k[0]][k[1]] != -1:
                            return False
    return True


def test_detecte_coordonnees_combinaison():
    """
    Teste la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe,
    False sinon
    """
    # Test 1: Pas de combinaison
    grille = [[0, 3, 2, 1, 1], [3, 1, 2, 3, 3], [0, 3, 3, 0, 1], [3, 3, 1, 0, 2], [0, 1, 0, 3, 3]]
    size = 5
    i = 2
    j = 4
    print(detecte_coordonnees_combinaison(grille, i, j, size) == [])

    # Test 2: Combinaison horizontale de 3 bonbons
    grille = [[0, 3, 2, 1, 1], [3, 1, 2, 3, 3], [3, 3, 3, 0, 1], [0, 3, 1, 0, 2], [0, 1, 0, 3, 3]]
    size = 5
    i = 2
    j = 1
    print(detecte_coordonnees_combinaison(grille, i, j, size) == [(2, 1), (2, 2), (2, 0)])

    # Test 3 : Combinaison verticale de 3 bonbons
    grille = [[0, 2, 2, 1, 1], [3, 2, 2, 3, 3], [3, 2, 3, 0, 1], [0, 4, 1, 0, 2], [0, 2, 1, 3, 3]]
    size = 5
    i = 1
    j = 1
    print(detecte_coordonnees_combinaison(grille, i, j, size) == [(1, 1), (2, 1), (0, 1)])

    # Test 4 : Combinaison verticale + horizontale
    grille = [[0, 2, 2, 1, 1], [3, 2, 2, 3, 3], [3, 2, 3, 0, 1], [0, 4, 1, 0, 2], [0, 2, 1, 3, 3]]
    size = 5
    i = 1
    j = 1
    print(detecte_coordonnees_combinaison(grille, i, j, size) == [(1, 1), (2, 1), (0, 1)])


# Choix des paramètres de jeu
size = int(input("Avec quelle taille de grille voulez-vous jouer ? (entier naturel) "))
colors = [0, 1, 2, 3]
grid = [[2, 2, 2, 2, 2], [3, 2, 0, 3, 3], [3, 2, 3, 0, 1], [0, 2, 1, 0, 2], [0, 2, 2, 3, 3]]#generate_grid(size, colors)
score = 0
gagne = False

# Programme principal

# On teste la fonction detecte_coordonnees
test_detecte_coordonnees_combinaison()

# On répète la boucle tant qu'il reste des combinaisons
while not gagne:

    # Affichage de la grille
    affichage_grille(grid, len(colors))

    # Tant qu'il reste des bonbons à supprimer (la fonction delete leur assigne la valeur -1 et renvoie True s'il en reste encore à supprimer)
    while delete(grid, size):

        # Application de la gravité
        gravite(grid, size)

        # On remplace les trous laissés en ahut de la grille par la fonction gravité
        replace(grid, size, colors)

    # On vérifie si le jeu peut continuer (il reste des combinaisons possibles)
    gagne = end(grid, size)
    if not gagne:
        print(f"Votre score actuel est de {score} bonbons supprimés.")
        affichage_grille(grid, len(colors))
        swap(grid)

# Annonce de la fin du jeu et du score final
print("Le jeu est terminé, il n'y a plus de combinaison possible !")
print(f"Votre score final est de {score} bonbons supprimés.")
