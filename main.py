
import game
from game import main
import pygame


WIDTH = 900
HEIGHT = 700
FPS = 60
score = 0
game_open = True
game.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# game.menu_ bo coś się waliło jak były 2  obiekty menu, chyba nie zmieniało dif w oby dwóch


while game_open:
    game.menu_.main_menu()
    score = main(score)
    game.menu_.game_over()
    print("Koniec")




#cool gra
