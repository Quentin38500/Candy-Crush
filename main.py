import random
import matplotlib.pyplot as plt


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
    x, y = input("Coordonnée X : "), input("Coordonnées Y : ")
    return int(x), int(y)


def swap(grid):
    """
    Cette fonction permet d'échanger deux bonbons.

    Paramètre :
    grid (list) : grille de jeu
    """
    candy_1 = ask_coordinates()
    candy_2 = ask_coordinates()

    # Échange des deux bonbons dans la grille de jeu
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
    if x-1 >= 0 and x+1 < size and grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x-1][y]:
        return [(x, y), (x+1, y), (x-1, y)]
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
    if y-1 >= 0 and y+1 < size and grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y-1]:
        return [(x, y), (x, y+1), (x, y-1)]
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
    # La variable "deleted" permet de savoir si toutes les combinaisons ont été supprimées
    deleted = False

    # On parcourt tous les bonbons de la grille
    for x in range(size):
        for y in range(size):

            # Pour chaque bonbon, on récupère les coordonnées des combinaisons possibles
            combinaison = detecte_coordonnees_combinaison(grid, x, y, size)

            # On assigne la valeur -1 à chaque bonbon faisant partie d'une combinaison
            for i in combinaison:
                if grid[i[0]][i[1]] != -1:
                    grid[i[0]][i[1]] = -1
                    deleted = True
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
        for i in range(size-1):
            for j in range(size):

                # Pour chaque bonbon ayant un bonbon supprimé (-1) en dessous, on le fait descendre
                if grid[i][j] != -1 and grid[i+1][j] == -1:

                    # Échange des bonbons
                    grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
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
    plt.imshow(grid, vmin=0, vmax=nb_type_bonbons-1, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)


# Choix des paramètres de jeu
size = 4
colors = [0, 1, 2, 3]
grid = generate_grid(size, colors)
gagne = False

# Programme principal
while not gagne:
    affichage_grille(grid, len(colors))
    while delete(grid, size):
        gravite(grid, size)
        replace(grid, size, colors)
    affichage_grille(grid, len(colors))
    swap(grid)
