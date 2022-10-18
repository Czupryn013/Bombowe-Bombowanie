import sys
import pygame
import game

class Menu:
    def __init__(self,width, height, FPS):
        self.width =width
        self.height =height
        self.FPS = FPS
        self.diciculty = "Easy"
        print("init")

    def draw_text(self,content, color, size, x, y, x_center=False, y_center = False):
        font = pygame.font.SysFont("arialblack", size)
        text = font.render(str(content), True, color)
        if x_center and y_center:
            t_width = text.get_rect().width
            t_height = text.get_rect().height
            game.WIN.blit(text, (x - (t_width // 2), y - (t_height//2)))
        elif x_center:
            t_width = text.get_rect().width
            game.WIN.blit(text, (x - (t_width // 2), y))
        elif y_center:
            t_height = text.get_rect().height
            game.WIN.blit(text, (x, y - t_height))
        else:
            game.WIN.blit(text, (x, y))

    def set_dificulty(self,dif):
        if dif == "Easy":
            game.BULLET_SPEED = 7
            game.BULLET_RNG = 100
            game.ON_DEATH = 25
            game.BONUS = 1
        elif dif == "Mid":
            game.BULLET_SPEED = 9
            game.BULLET_RNG = 50
            game.ON_DEATH = 50
            game.BONUS = 2
        elif dif == "Hard":
            game.BULLET_SPEED = 11
            game.BULLET_RNG = 25
            game.ON_DEATH = 100
            game.BONUS = 3

    def shop(self):
        pass

    def options(self):
        game.WIN.fill((255, 255, 0))
        show_opt = True
        clock = pygame.time.Clock()
        while show_opt:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.diciculty = "Easy"
                        show_opt = False
                    if event.key == pygame.K_2:
                        self.diciculty = "Mid"
                        show_opt = False
                    if event.key == pygame.K_3:
                        self.diciculty = "Hard"
                        show_opt = False
                    if event.key == pygame.K_ESCAPE:
                        show_opt = False

            if self.diciculty == "Easy":
                self.draw_text("1 - Easy", (255, 0, 255), 40, self.width // 2, self.height // 2 - 50, x_center=True,
                               y_center=True)
                self.draw_text("2 - Medium", (255, 0, 0), 40, self.width // 2, self.height // 2, x_center=True,
                               y_center=True)
                self.draw_text("3 - Hard", (255, 0, 0), 40, self.width // 2, self.height // 2 + 50, x_center=True,
                               y_center=True)
            elif self.diciculty == "Mid":
                self.draw_text("1 - Easy", (255, 0, 0), 40, self.width // 2, self.height // 2 - 50, x_center=True,
                               y_center=True)
                self.draw_text("2 - Medium", (255, 0, 255), 40, self.width // 2, self.height // 2, x_center=True,
                               y_center=True)
                self.draw_text("3 - Hard", (255, 0, 0), 40, self.width // 2, self.height // 2 + 50, x_center=True,
                               y_center=True)
            elif self.diciculty == "Hard":
                self.draw_text("1 - Easy", (255, 0, 0), 40, self.width // 2, self.height // 2 - 50, x_center=True,
                               y_center=True)
                self.draw_text("2 - Medium", (255, 0, 0), 40, self.width // 2, self.height // 2, x_center=True,
                               y_center=True)
                self.draw_text("3 - Hard", (255, 0, 255), 40, self.width // 2, self.height // 2 + 50, x_center=True,
                               y_center=True)
            pygame.display.update()

    def main_menu(self):
        show_menu = True
        clock = pygame.time.Clock()
        while show_menu:
            clock.tick(self.FPS)
            # print(f"{self.diciculty}" + "1")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        show_menu = False
                    if event.key == pygame.K_2:
                        self.shop()
                    if event.key == pygame.K_3:
                        self.options()
                    if event.key == pygame.K_4:
                        pygame.quit()
            self.set_dificulty(self.diciculty)

            game.WIN.fill((255, 255, 0))
            self.draw_text("1 - Play", (255, 0, 0), 40, self.width // 2, self.height // 2 -100, x_center=True, y_center=True)
            self.draw_text("2 - Shop", (255, 0, 0), 40, self.width // 2, self.height // 2 -50, x_center=True, y_center=True)
            self.draw_text("3 - Options", (255, 0, 0), 40, self.width // 2, self.height // 2 , x_center=True, y_center=True)
            self.draw_text("4 - Quit", (255, 0, 0), 40, self.width // 2, self.height // 2 + 50, x_center=True, y_center=True)
            pygame.display.update()

    def game_over(self):
        show_game_over = True
        clock = pygame.time.Clock()
        while show_game_over:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        show_game_over = False

            game.WIN.fill((0, 0, 0))
            self.draw_text("Zgon",(255, 0, 0), 40, self.width // 2, self.height // 2, x_center=True, y_center=True)
            pygame.display.update()