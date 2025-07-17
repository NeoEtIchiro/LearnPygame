import pygame
from grid import Grid
from button import Button
from camera import Camera

# --- Paramètres de la fenêtre et de la grille ---
CELL_SIZE = 20      # Taille d'une cellule en pixels
COLS = 100          # Nombre de colonnes dans la grille
ROWS = 100          # Nombre de lignes dans la grille
WIDTH = 800         # Largeur de la fenêtre d'affichage
HEIGHT = 600        # Hauteur de la fenêtre d'affichage
BUTTON_PANEL_HEIGHT = 50  # Hauteur de la zone des boutons
SCREEN_HEIGHT = HEIGHT + BUTTON_PANEL_HEIGHT  # Hauteur totale

# --- Variables globales de simulation ---
running = False     # Indique si la simulation est en cours
step_flag = False   # Indique si on doit avancer d'une génération
grid_obj = Grid(ROWS, COLS)  # La grille du jeu

def bresenham_line(x0, y0, x1, y1):
    """
    Algorithme de Bresenham pour dessiner une ligne entre deux points sur une grille.
    Retourne la liste des coordonnées (row, col) de toutes les cellules traversées.
    Utile pour dessiner en glissant la souris rapidement.
    """
    points = []
    delta_x = abs(x1 - x0)
    delta_y = abs(y1 - y0)
    step_x = 1 if x0 < x1 else -1
    step_y = 1 if y0 < y1 else -1
    error = delta_x - delta_y
    while True:
        points.append((y0, x0))
        if x0 == x1 and y0 == y1:
            break
        error2 = 2 * error
        if error2 > -delta_y:
            error -= delta_y
            x0 += step_x
        if error2 < delta_x:
            error += delta_x
            y0 += step_y
    return points

def game_loop():
    """
    Fonction principale qui gère la boucle du jeu :
    - Affichage
    - Gestion des événements (souris, clavier)
    - Simulation du jeu de la vie
    """
    global running, step_flag, grid_obj
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jeu de la vie")
    clock = pygame.time.Clock()

    # Caméra pour déplacer et zoomer sur la grille
    cam = Camera(COLS, ROWS, WIDTH, HEIGHT, CELL_SIZE)
    cell_size = CELL_SIZE

    # Variables pour le dessin en glissé
    drawing = False      # True si on est en train de dessiner avec la souris
    draw_value = None    # Valeur à dessiner (1 = vivant, 0 = mort)
    last_cell = None     # Dernière cellule modifiée (pour tracer une ligne)

    # Préparer la police et les boutons
    font = pygame.font.SysFont(None, 24)
    btn_w, btn_h, spacing = 80, 30, 10
    names = ['Start', 'Stop', 'Step', 'Randomize', 'Clear', 'Quit']
    buttons = {}
    for i, name in enumerate(names):
        x = spacing + i * (btn_w + spacing)
        y = HEIGHT + 10
        rect = pygame.Rect(x, y, btn_w, btn_h)
        buttons[name] = Button(rect, name, font)

    while True:
        # --- Gestion des événements clavier/souris ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Relâchement du bouton souris : on arrête de dessiner
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                last_cell = None

            # Gestion des touches clavier
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif event.key == pygame.K_SPACE:
                    running = not running  # Pause ou reprise
                elif event.key == pygame.K_RETURN:
                    step_flag = True       # Avancer d'une génération
                elif event.key == pygame.K_r:
                    grid_obj.randomize()   # Remplir la grille aléatoirement
                elif event.key == pygame.K_c:
                    grid_obj.reset()       # Vider la grille

            # Zoom avec la molette de la souris
            elif event.type == pygame.MOUSEWHEEL:
                # On veut zoomer autour du centre de l'écran
                old_size = cell_size
                
                center_x = WIDTH / 2
                center_y = HEIGHT / 2
                
                # Coordonnées du centre dans le "monde" (grille)
                
                world_cx = (cam.x + center_x) / old_size
                world_cy = (cam.y + center_y) / old_size
                
                # Ajuster la taille des cellules
                if event.y > 0:
                    cell_size = min(cell_size + 2, 200)
                elif event.y < 0:
                    min_size = max(WIDTH // COLS, HEIGHT // ROWS)
                    cell_size = max(cell_size - 2, min_size)
                    
                cam.cell_size = cell_size  # Mettre à jour la caméra
                # Recentrer la caméra pour garder le même centre
                cam.x = world_cx * cell_size - center_x
                cam.y = world_cy * cell_size - center_y
                # Empêcher la caméra de sortir des limites
                cam.x = min(max(cam.x, 0), COLS * cell_size - WIDTH)
                cam.y = min(max(cam.y, 0), ROWS * cell_size - HEIGHT)

            # Clic souris : soit dessiner une cellule, soit cliquer un bouton
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < HEIGHT:
                    # Clic sur la grille : début du dessin
                    col = int((x + cam.x) // cell_size)
                    row = int((y + cam.y) // cell_size)
                    
                    if 0 <= row < ROWS and 0 <= col < COLS:
                        drawing = True
                        
                        # On choisit la couleur selon la cellule cliquée
                        draw_value = 1 if grid_obj.cells[row][col] == 0 else 0
                        grid_obj.toggle(row, col, draw_value)
                        last_cell = (row, col)
                else:
                    # Clic sur un bouton
                    for name, btn in buttons.items():
                        if btn.is_hover((x, y)):
                            if name == 'Start': running = True
                            elif name == 'Stop': running = False
                            elif name == 'Step': step_flag = True
                            elif name == 'Randomize': grid_obj.randomize()
                            elif name == 'Clear': grid_obj.reset()
                            elif name == 'Quit': pygame.quit(); return

        # --- Dessin en glissé (maintenir le bouton souris) ---
        if drawing:
            mx, my = pygame.mouse.get_pos()
            if my < HEIGHT:
                c = int((mx + cam.x) // cell_size)
                r = int((my + cam.y) // cell_size)
                
                if 0 <= r < ROWS and 0 <= c < COLS:
                    # Tracer une ligne entre la dernière cellule et la nouvelle
                    if last_cell is not None:
                        r0, c0 = last_cell
                        for rr, cc in bresenham_line(c0, r0, c, r):
                            grid_obj.toggle(rr, cc, draw_value)
                            last_cell = (rr, cc)
                    
                    # Mettre à jour la dernière cellule
                    last_cell = (r, c)

        # --- Simulation du jeu de la vie ---
        if step_flag:
            grid_obj.next_generation()  # Avancer d'une génération
            step_flag = False
        if running:
            grid_obj.next_generation()  # Avancer automatiquement

        # --- Affichage ---
        screen.fill((0, 0, 0))  # Fond noir

        # Dessiner la grille (uniquement les cellules vivantes)
        for r in range(ROWS):
            for c in range(COLS):
                if grid_obj.cells[r][c] == 1:
                    px, py = cam.apply(c, r)
                    # On ne dessine que si la cellule est visible à l'écran
                    if 0 <= px < WIDTH and 0 <= py < HEIGHT:
                        pygame.draw.rect(screen, (0,255,0),(px,py,cell_size-1,cell_size-1))

        # Dessiner les boutons
        for btn in buttons.values():
            btn.draw(screen)

        # Déplacement continu de la caméra avec les flèches du clavier
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: cam.move(-cell_size,0)
        if keys[pygame.K_RIGHT]: cam.move(cell_size,0)
        if keys[pygame.K_UP]: cam.move(0,-cell_size)
        if keys[pygame.K_DOWN]: cam.move(0,cell_size)

        pygame.display.flip()  # Mettre à jour l'affichage

if __name__ == "__main__":
    game_loop()