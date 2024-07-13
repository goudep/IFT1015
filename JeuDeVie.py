'''
TP1 le jeu de la vie
Name : Yudi Ma, 20236724 ; Ru Qian,20234621
Date : 2024-07-04
Summary : Ce programme implémente le "Jeu de la Vie" de Conway, un automate
cellulaire. Il crée une grille 2D, initialise les cellules de manière 
aléatoire, et applique des règles prédéfinies pour simuler l'évolution des 
cellules vivantes et mortes au fil du temps.
'''

''' 
Fonction pour créer une grille 2D avec des lignes et colonnes spécifiées
paramètres : 
           -nbRangs : int type,  nombre de rangs
           -nbCol : int type, nombre de columne 
Retourne :
           - Une liste 2D représentant la grille avec toutes les cellules
           initialiséesà 0, ou -1 si les dimensions d'entrée sont invalides
'''
   
def creeGrid(nbRangs, nbCols):
    grille = [None] * nbRangs    # Initialiser la grille avec des valeurs None
    if nbRangs <= 0 or nbCols <= 0 :
        return -1                # Retourner -1 pour des dimensions invalides
    for i in range(nbRangs):
        # Créer une ligne avec nbCols colonnes, toutes à 0
        grille[i] = [0] * nbCols 
        
    return grille


# Fonction pour tester la fonction creeGrid
def testCreeGrid():
    assert creeGrid(3,2) == [[0,0],[0,0],[0,0]] 
    assert creeGrid(2,3) == [[0,0,0],[0,0,0]] 
    assert creeGrid(0,0) == -1 
    assert creeGrid(-1,3) == -1
    assert creeGrid(3,-1) == -1 
    
                 
'''
 Fonction pour générer une valeur aléatoire dans une plage
 Retourne :
          - Une valeur entière aléatoire entre 10 et 50
'''
def randomGrid():
    minVal = 10
    maxVal = 50
    # Calculer la valeur aléatoire dans la plage [minVal, maxVal]
    scaledVal = minVal + (maxVal - minVal) * random()
    resultat = int(scaledVal)
    return resultat


# Fonction pour tester la fonction randomGrid
def testRandomGrid():
    assert randomGrid() >= 10 and randomGrid() <= 50 
    assert randomGrid() >= 10 and randomGrid() <= 50 
    assert randomGrid() >= 10 and randomGrid() <= 50 

    
'''
Fonction pour initialiser la grille avec des cellules vivantes aléatoires

Paramètres :
          - grille : liste 2D, la grille à initialiser
Retourne :
          - La grille initialisée avec certaines cellules mises à 1 (vivantes)
'''
def init(grille):
    # Obtenir le nombre de lignes
    nbRangs = len(grille)
    # Obtenir le nombre de colonnes
    nbCols = len(grille[0]) if nbRangs > 0 else 0
    
    # Calculer le nombre de cellules vivantes basé sur un pourcentage aléatoire
    numCells = int(randomGrid() / 100 * nbRangs * nbCols)
    for i in range(numCells):
        # Générer une position de ligne aléatoire
        x = int(random() * nbRangs)
        
        # Générer une position de colonne aléatoire
        y = int(random() * nbCols)
        grille[x][y] = 1      # Mettre la cellule à vivante
    return grille


'''
Fonction pour obtenir une fenêtre 3x3 autour d'une cellule spécifique dans la grille
Paramètres :
           - grille : liste 2D, la grille originale
           - x : int, l'indice de ligne de la cellule centrale
           - y : int, l'indice de colonne de la cellule centrale
Retourne :
           - Une liste 3x3 représentant la fenêtre autour de la cellule (x, y)
'''
def windowGrille(grille, x, y):
    windowSize = 3 
    row = x 
    col = y
    
    # Déterminer la ligne de début de la fenêtre
    startRow = max(0,row - 1)
    
    # Déterminer la ligne de fin de la fenêtre
    endRow = min(len(grille), row + 2) 
    
    # Déterminer la colonne de début de la fenêtre
    startCol = max(0,col - 1)
    
    # Déterminer la colonne de fin de la fenêtre
    window = []
    endCol = min(len(grille[0]), col + 2) 
    window = [] 
    for i in range(startRow, endRow):
        windowRow = []
        for j in range(startCol, endCol):
            # Ajouter la valeur de la cellule à la fenêtre
            windowRow.append(grille[i][j])
        window.append(windowRow)
    return window 

# Fonction pour tester la fonction windowGrille()
def testWindowGrille():
    # Créer une grille d'exemple
    grille = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    # Définir les tests avec les résultats attendus
    tests = [
        ((0, 0), [[1, 2], [5, 6]]),                    # Coin supérieur gauche
        ((0, 3), [[3, 4], [7, 8]]),                    # Coin supérieur droit
        ((3, 0), [[9, 10], [13, 14]]),                 # Coin inférieur gauche
        ((3, 3), [[11, 12], [15, 16]]),                # Coin inférieur droit
        ((1, 1), [[1, 2, 3], [5, 6, 7], [9, 10, 11]])] # Centre
    
    # Exécuter les tests et vérifier les résultats avec assert
    for (x, y), expected in tests:
        result = windowGrille(grille, x, y)
        assert result == expected

'''
Fonction pour calculer la somme de toutes les valeurs dans une fenêtre
Paramètres :
           - window : liste 2D, la fenêtre autour d'une cellule
Retourne :
         - La somme de toutes les valeurs dans la fenêtre
'''
def sommeWindow(window):
    total = 0
    
    # Additionner les valeurs de chaque ligne de la fenêtre
    for row in window:
        total += sum(row)
    return total

# Fonction pour tester la fonction sommeWindow()
def testSommeWindow():
    # Définir des fenêtres de test avec les sommes attendues
    tests = [
        ([[1, 2], [3, 4]], 10),        # Fenêtre simple
        ([[5, 5, 5], [5, 5, 5]], 30),  # Fenêtre avec des valeurs identiques
        ([[0, 0], [0, 0]], 0),         # Fenêtre avec des zéros
        ([], 0),                       # Fenêtre vide
        ([[100]], 100)]                # Fenêtre avec un seul élément
    
    # Exécuter les tests et vérifier les résultats avec assert
    for window, expected in tests:
        result = sommeWindow(window)
        assert result == expected
    
'''
Fonction pour dessiner la grille en utilisant le module turtle
Paramètres :
           - grille : liste 2D, la grille à dessiner
           - cote : int, la taille de chaque cellule dans la grille
'''
def dessinerGrid(grille, cote):
    x = len(grille)
    y = len(grille[0])
    clear()
    
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            
            # Calculer la position x de la cellule
            x_pos = j * cote - x * cote // 2
            
             # Calculer la position y de la cellule
            y_pos = -i * cote + y * cote // 2 

            # Dessiner la grille
            pu()
            goto(x_pos, y_pos)
            pd()
            pencolor(0,0,0)
            pensize(1)
            for _ in range(4):
                fd(cote)
                rt(90)

            # Remplir la cellule si elle est vivante
            if grille[i][j] == 1:
                pu()
                # Se déplacer vers la position centrale de la cellule
                goto(x_pos, y_pos - cote / 2)  
                pensize(cote)
                pencolor(1,0,0)
                pd()
                fd(cote)


'''
Fonction pour mettre à jour la grille en fonction des règles du Jeu de la Vie
Paramètres :
           - grille : liste 2D, la grille actuelle
Retourne :
         - Une nouvelle grille représentant l'état suivant
'''
def updateGrille(grille):
    
    x = len(grille)
    y = len(grille[0])
    newGrille = creeGrid(x, y)
    for j in range(y):
        for i in range(x):
            # Obtenir la fenêtre 3x3 autour de la cellule
            window = windowGrille(grille,i,j)
            vivantCote = sommeWindow(window)
            # Appliquer les règles du Jeu de la Vie
            
            # Plus de 3 voisins - la cellule meurt
            if grille[i][j] == 1 and vivantCote > 4 : 
                                newGrille[i][j] = 0 
                    
            # 2 ou 3 voisins - la cellule reste vivante
            elif grille[i][j] == 1 and vivantCote in range(3,5): 
                newGrille[i][j] = 1
                
            # Exactement 3 voisins - la cellule devient vivante
            elif grille[i][j] == 0 and vivantCote == 3:  
                                newGrille[i][j] = 1 
                    
            # Moins de 2 voisins - la cellule meurt
            elif grille[i][j] == 1 and vivantCote < 3 :  
                                newGrille[i][j] = 0
            else: newGrille[i][j] = 0
                
    return newGrille


'''
Fonction pour démarrer le Jeu de la Vie
Paramètres :
           - nx : int, nombre de colonnes dans la grille
           - ny : int, nombre de lignes dans la grille
           - largeur : int, taille de chaque cellule dans la grille
'''
def jouer(nx, ny,largeur):
    grilleVide = creeGrid(ny,nx)   # Créer une grille vide
    
    # Initialiser la grille avec des cellules vivantes aléatoires
    grille = init(grilleVide)   
    
    while True:          # Dessiner la grille
        dessinerGrid(grille,largeur)
        ht()
        sleep(1)         # Attendre 1 seconde avant de mettre à jour la grille
        grille = updateGrille(grille)    # Mettre à jour la grille

# Exécution des tests de fonctions supplémentaires 
testCreeGrid() 
testRandomGrid()
testWindowGrille()
testSommeWindow()

# Démarrer le jeu avec une grille de 20x20 et une taille de cellule de 10
jouer(20,20,10)