import random
import matplotlib.pyplot as plt


def generate_grid(size, colors):
    grid = []
    for i in range(size):
        l = []
        for j in range(size):
            l.append(random.choice(colors))
        grid.append(l)
    return grid


def ask_coordinates():
    x, y = input("Coordonnée X :"), input("Coordonnées Y :")
    return int(x), int(y)


def swap(grid):
    candy_1 = ask_coordinates()
    candy_2 = ask_coordinates()
    grid[candy_1[0]][candy_1[1]], grid[candy_2[0]][candy_2[1]] = grid[candy_2[0]][candy_2[1]], grid[candy_1[0]][candy_1[1]]


def detecte_coordonnes_horizontal(grid, x, y, size):
    if x-1 >= 0 and x+1 < size and grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x-1][y]:
        return [(x, y), (x+1, y), (x-1, y)]
    else:
        return []


def detecte_coordonnes_vertical(grid, x, y, size):
    if y-1 >= 0 and y+1 < size and grid[x][y] == grid[x][y+1] and grid[x][y] == grid[x][y-1]:
        return [(x, y), (x, y+1), (x, y-1)]
    else:
        return []


def detecte_coordonnees_combinaison(grid, x, y, size):
    return detecte_coordonnes_horizontal(grid, x, y, size) + detecte_coordonnes_vertical(grid, x, y, size)


def delete(grid, size):
    deleted = False
    for x in range(size):
        for y in range(size):
            combinaison = list(tuple(detecte_coordonnees_combinaison(grid, x, y, size)))
            for i in combinaison:
                if grid[i[0]][i[1]] != -1:
                    deleted = True
                    grid[i[0]][i[1]] = -1
    return deleted


def gravite(grid, size):
    change = True
    while change:
        changement = 0
        for i in range(size-1):
            for j in range(size):
                if grid[i][j] != -1 and grid[i+1][j] == -1:
                    grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
                    changement += 1
        if changement == 0:
            change = False


def replace(grid, size, colors):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == -1:
                grid[i][j] = random.choice(colors)


def affichage_grille(grid, nb_type_bonbons):
    plt.imshow(grid, vmin=0, vmax=nb_type_bonbons-1, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)


size = 4
colors = [0, 1, 2, 3]
grid = generate_grid(size, colors)
gagne = False

while not gagne:
    affichage_grille(grid, len(colors))
    while delete(grid, size):
        gravite(grid, size)
        replace(grid,size,colors)
    affichage_grille(grid, len(colors))
    swap(grid)