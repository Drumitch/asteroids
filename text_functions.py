import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Create a text object to display "Game Over" to the center of the screen
def game_over(text, screen):
    game_over_txt_surf = text.render("Game Over!", True, (255, 255, 255))
    text_area = game_over_txt_surf.get_rect()
    text_area.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(game_over_txt_surf, text_area)