import pygame
import random
from config import *
from menus import main_menu, select_difficulty, pause_menu, draw_text, draw_center_line

# Initialiser pygame
pygame.init()

# Initialiser la fenêtre du jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Contrôle de la fréquence d'images
clock = pygame.time.Clock()

# Police pour aficher du texte
font = pygame.font.Font(None, 36)

def reset_ball(ball_x, ball_y, ball_velocity_x, ball_velocity_y):
    """ 
    Fonction pour réinitialiser la balle lorsqu'un joueur gagne un point
    """
    
    # TODO : RÉINITIALISER LA POSITION DE LA BALLE AU CENTRE DU JEU
    # Ici, vous devez redéfinir la position de la balle pour qu'elle soit au centre de la fenêtre du jeu en x (c'est-à-dire, sur la ligne pointillée)


    # TODO : LANCEMENT DE LA BALLE APRÈS RÉINITIALISATION
    # Si le joueur 2 a gagné un point, relancer la balle de son côté (à la gauche) avec une position aléatoire en y (par en haut ou par en bas), à partir de la ligne pointillée
    # Si le joueur 1 a gagné un point, relancer la balle de son côté (à la droite) avec une position aléatoire en y (par en haut ou par en bas), à partir de la ligne pointillée

    return ball_x, ball_y, ball_velocity_x, ball_velocity_y

def play_game(player1_y, player2_y, player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y):
    """
    Fonction qui lance et gère le jeu 
    """
    # Définition de la variable "game_mode" comme étant la sortie du menu principal (soit "single player" ou "multi player")
    game_mode = main_menu()

    # Définition de la variable "difficulty" comme étant la sortie du menu "select difficulty" (soit "easy", "medium", ou "hard")
    if game_mode == 'single player':
        difficulty = select_difficulty() 
    else :
        difficulty = None

    running = True
    while running:
        screen.fill(BLACK)

        # Gestion des touches de clavier 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Show the pause menu and capture the return value
                    result = pause_menu()
                    if result == "main menu":
                        reset_game()  # Reset game and return to main menu
                        return  # Exit the play_game loop
                    # If 'resume', simply break out of the pause logic
                    elif result == 'resume':
                        break  # Continue the main game loop

        # Contrôle des touches de clavier
        keys = pygame.key.get_pressed()

        # TODO : IMPLÉMENTATION DU MOUVEMENT DES RAQUETTES POUR L'OPTION "MULTI PLAYER"
        #
        # Ici, vous devez implémenter le mouvement des raquettes des joueurs 1 et 2 pour le cas "multi player"
        #
        # Le mouvement de la raquette du joueur 1 doit être contrôlé par les touches "w" et "s" du clavier pour les déplacements de haut en bas, respectivement. 
        # Le mouvement de la raquette du joueur 2 doit être contrôlé par les flèches en haut et en bas du clavier. 
        #
        # * Note 1 : Vous devez utiliser la variable "paddle_speed" pour gérer les déplacements des raquettes. 
        #
        # * Note 2 : Lorsque les raquettes atteignent le haut ou le bas de la fenêtre de jeu, elles ne doivent pas dépasser ces limites. 
        #          Assurez-vous que leur position reste dans les bornes définies par la hauteur de l'écran.





        # TODO : IMPLÉMENTATION DU MOUVEMENT DES RAQUETTES POUR L'OPTION "SINGLE PLAYER"
        #
        # 1. Le joueur 1 contrôle sa raquette avec les touches "w" (haut) et "s" (bas), comme dans le mode "multi player".
        #
        # 2. La raquette du joueur 2 (contrôlée par l'ordinateur) doit suivre la position de la balle. Plus précisément : 
        #      - Si la position y de la balle est inférieure au centre de la raquette, la raquette doit monter.
        #      - Si la position y de la balle est supérieure au centre de la raquette, la raquette doit descendre.
        #
        # 3. Afin de rendre les mouvements de l'adversaire un peu plus vraisemblables, vous devez également ajouter une variable nommée "margin" à la position du centre de la raquette. 
        #    De cette façon, le centre de la raquette de l'adversaire suivra le mouvement de la balle, mais avec un léger décalage. La valeur de la variable "margin" doit varier de façon aléatoire, 
        #    c'est-à-dire : 
        #      - 90% du temps, "margin" doit être égale à 40
        #      - 10% du temps, "margin" doit être égale à 20
        #
        # 4. Adaptez la vitesse de déplacement de la raquette du joueur 2 selon le niveau de difficulté sélectionné dans le menu "SELECT DIFFICULTY" :
        #     - Pour le niveau "easy", la vitesse de déplacement de la raquette doit être égale à "paddle_speed - 5"
        #     - Pour le niveau "medium", la vitesse de déplacement de la raquette doit être égale à "paddle_speed - 4"
        #     - Pour le niveau "hard", la vitesse de déplacement de la raquette doit être égale à "paddle_speed"

        
        


        # TODO : GESTION DU MOUVEMENT DE LA BALLE 
        #
        # 1. Mettre à jour la position de la balle (les variables "ball_x" et "ball_y") en utilisant les variables "ball_velocity_x" et "ball_velocity_y".
        #
        # 2. Gérer les collisions de la balle avec le haut et le bas de la fenêtre de jeu. 
        #    Lorsque la balle atteint le haut ou le bas, sa direction verticale doit être inversée.
        #
        # 3. Gérer les collisions entre la balle et les raquettes. 
        #    Lorsque la balle frappe une raquette, sa direction horizontale doit être inversée.

        




        # TODO : GESTION DES POINTS ET RÉINITIALISATION DE LA BALLE
        #
        # 1. Vous devez implémenter l'ajout de points lorsqu'un joueur manque la balle et qu'elle frappe l'un des murs.
        #
        # 2. Vous devez également réinitialiser la balle pour qu'elle réapparaisse dans le jeu à l'aide de la fonction "reset_ball" que vous avez implémenté





        # Vérifier s'il y a un gagnant
        if player1_score == 11:
            win("PLAYER 1 WINS!")
            return
        if player2_score == 11:
            win("PLAYER 2 WINS!")
            return

        # Affichage des raquettes, de la balle et des points dans la fenêtre du jeu 
        pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE)
        draw_center_line(screen)
        draw_text("PLAYER 1", SCREEN_WIDTH // 4, 18, WHITE, 28, screen)
        draw_text(str(player1_score), SCREEN_WIDTH // 4, 55, WHITE, 36, screen)
        draw_text("PLAYER 2", SCREEN_WIDTH * 3 // 4, 18, WHITE, 28, screen)
        draw_text(str(player2_score), SCREEN_WIDTH * 3 // 4, 55, WHITE, 36, screen)

        # Mise à jour de l'affichage
        pygame.display.flip()

        # Fréquence d'images
        clock.tick(60)

def reset_game():
    """
    Réinitialisation du jeu pour débuter une nouvelle partie
    """
    player1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    player2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_velocity_x = BALL_SPEED_X
    ball_velocity_y = BALL_SPEED_Y
    player1_score = 0
    player2_score = 0
    play_game(player1_y, player2_y, player1_score, player2_score, ball_x, ball_y, ball_velocity_x, ball_velocity_y)

def win(winner_message):
    """
    Affichage d'un message lorsqu'il y a un gagnant
    """
    screen.fill(BLACK)

    # Afficher le message du gagnant 
    draw_text(winner_message, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, WHITE, 48, screen)
    draw_text("PRESS 'M' TO RETURN TO MAIN MENU", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE, 36, screen)

    # Mise à jour de l'affichage
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    main_menu()  # Retour au menu principal
                    return
                if event.key == pygame.K_r:
                    reset_game()  # Réinitialisation du jeu
                    return

