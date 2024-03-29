import pygame
from Menu import MainMenu
from Sorting import List
from Search import Grid


#Implement Buttons?
x_box = None
y_box = None

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.infoobject = pygame.display.Info()
        self.DISPLAY_W, self.DISPLAY_H = (self.infoobject.current_w)*2//4, (self.infoobject.current_h)*3//4
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        pygame.display.set_caption("Algorithm Visualizer")
        self.font_name = pygame.font.get_default_font()
        self.WHITE, self.GREY, self.BLUE = (255, 255,255), (224, 224, 224), (0,102,102)
        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu
        self.lst = List(100, self.DISPLAY_H*9/10, self, self.DISPLAY_W * 1/10)
        self.grid = None
        self.playing = False
        self.search = None

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
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.UP_KEY = True

             
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def text_width(self,text, size):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        width = font.size(text)
        return width[0]
          

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_rect(self, rect):
        pygame.draw.rect(self.display, self.BLUE, rect)
        self.window.blit(self.display, (0,0))



g = Game()

while g.running:
    g.curr_menu.display_menu()



#When selecting search or sort - grid is built and then the options are drawn. 