import random

# Dimensions de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dimensions et vitesse de déplacement des raquettes
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 50
paddle_speed = 11

# Taille de la balle
BALL_SIZE = 5

# Vitesse de la balle
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Initialisation des points à 0 pour le début du match
player1_score = 0
player2_score = 0

# Variables des menus de sélection 
game_mode = None  # Mode du jeu : "single player" ou "multi player"
difficulty = None  # Difficulté (pour le mode "single player" seulement) : "easy", "medium" ou "hard"

# Initialisation
ball_x = None
ball_y = None
ball_velocity_x = None
ball_velocity_y = None