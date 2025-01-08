import pygame
from config import *

# Mode de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

def draw_text(text, x, y, color, size, screen):
    """
    Cette fonction permet d'écrire du texte sur la fenêtre du jeu, à des positions spécifiques.
    """
    font = pygame.font.SysFont("Consolas", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_center_line(screen):
    """
    Fonction pour dessiner une ligne verticale pointillée.
    """
    line_x = SCREEN_WIDTH // 2
    line_height = 20  # Hauteur de chaque ligne
    space = 10  # Espace entre les lignes
    for i in range(0, SCREEN_HEIGHT, line_height + space):
        pygame.draw.line(screen, WHITE, (line_x, i), (line_x, i + line_height), 2)

def main_menu():
    """
    Fonction pour afficher le menu principal avec la sélection "single player" ou "multi player". 
    """
    selecting = True
    while selecting:
        screen.fill(BLACK)
        draw_text("PONG", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, WHITE, 70, screen)
        draw_text("1 SINGLE PLAYER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40, WHITE, 36, screen)
        draw_text("2 MULTI-PLAYER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40, WHITE, 36, screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "single player" 
                    selecting = False
                elif event.key == pygame.K_2:
                    game_mode = "multi player"
                    selecting = False

    return game_mode  # Retourner le mode de jeu sélectionné ("single" ou "multi")

def select_difficulty():
    """
    Cette fonction permet d'afficher le menu de sélection de la difficulté ("easy", "medium" ou "hard"). 
    """
    selecting = True
    while selecting:
        screen.fill(BLACK)
        draw_text("SELECT DIFFICULTY", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, WHITE, 48, screen)
        draw_text("1 EASY", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40, WHITE, 36, screen)
        draw_text("2 MEDIUM", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE, 36, screen)
        draw_text("3 HARD", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40, WHITE, 36, screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "easy"
                    selecting = False
                elif event.key == pygame.K_2:
                    difficulty = "medium"
                    selecting = False
                elif event.key == pygame.K_3:
                    difficulty = "hard"
                    selecting = False
    
    return difficulty

def pause_menu():
    """
    Cette fonction permet de mettre le jeu en pause lorsqu'on appuie sur la touche "ESC", 
    avec l'option de résumer la partie ou de retourner au menu principal. 
    """
    while True:
        screen.fill(BLACK)
        draw_text("PAUSE MENU", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, WHITE, 48, screen)
        draw_text("PRESS 'R' TO RESUME", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE, 36, screen)
        draw_text("PRESS 'M' FOR MAIN MENU", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, WHITE, 36, screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'resume'
                if event.key == pygame.K_m:
                    return 'main menu'

        pygame.display.flip()
