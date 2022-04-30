import pygame
from Menu import MainMenu


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 720, 480
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.WHITE, self.BLACK = (255, 255,255), (0, 0, 0)
        self.curr_menu = MainMenu(self)


    def program_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            #reset screen to update menu
            self.display.fill(self.BLACK)
            self.draw_text("Thanks for Playing", 20, 360, 240)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    #Checks if player is pressing key/what key is being pressed
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False


    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)



g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.program_loop()