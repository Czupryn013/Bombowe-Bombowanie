import pygame
import game

class Menu:
    def __init__(self,width, height, FPS):
        self.width =width
        self.height =height
        self.FPS = FPS

    def draw_text(self,content, color, size, x, y, centered=False):
        font = pygame.font.SysFont("arialblack", size)
        text = font.render(str(content), True, color)
        if centered:
            t_width = text.get_rect().width
            game.WIN.blit(text, (x - (t_width // 2), y))
        else:
            game.WIN.blit(text, (x, y))

    def main_menu(self):
        game.WIN.fill((255, 255, 0))
        show_menu = True
        clock = pygame.time.Clock()
        while show_menu:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        show_menu = False
                    if event.key == pygame.K_2:
                        pygame.quit()
            self.draw_text("1 - Play", (255, 0, 0), 40, self.width // 2, self.height // 2 + 50, centered=True)
            self.draw_text("2 - Quit", (255, 0, 0), 40, self.width // 2, self.height // 2, centered=True)
            pygame.display.update()
    def shop(self):
        pass
    def game_over(self):
        game.WIN.fill((0, 0, 0))

        show_game_over = True
        clock = pygame.time.Clock()
        while show_game_over:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        show_game_over = False

            self.draw_text("Zgon",(255, 0, 0), 40, self.width // 2, self.height // 2, centered=True)
            pygame.display.update()