import pygame

import game
from game import main
import pygame
import menu

WIDTH = 900
HEIGHT = 700
FPS = 60
score = 0
game_open = True
game.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
menu = menu.Menu(WIDTH, HEIGHT, FPS)
while game_open:
    menu.main_menu()
    score += main(score)
    menu.game_over()



#cool gra
