import pygame

class Menu():
    def __init__(self,game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0, 20,20)
        self.offset = -100 #offset

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game) #init with all the values of a Menu class
        self.state = "Sort"
        self.sortingx, self.sortingy = self.mid_w, self.mid_h + 30
        self.searchx, self.searchy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.sortingx + self.offset, self.sortingy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events() #set flags to allow to move cursor
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Main Menu", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H / 2 - 20) #Main menu title is at the center slighty above options
            self.game.draw_text("Sorting Algorithms", 20, self.sortingx, self.sortingy)
            self.game.draw_text("Search Algorithms", 20, self.searchx, self.searchy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            #if down key is pressed, curosr is moved to next option and state is adjusted accordingly
            if self.state == 'Sort':
                self.cursor_rect.midtop = (self.searchx + self.offset, self.searchy)
                self.state = 'Search'
            elif self.state == 'Search':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.sortingx + self.offset, self.sortingy)
                self.state = 'Sort'
        elif self.game.UP_KEY:
            if self.state == 'Sort':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Search':
                self.cursor_rect.midtop = (self.sortingx + self.offset, self.sortingy)
                self.state = 'Sort'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.searchx + self.offset, self.searchy)
                self.state = 'Search'

    def check_input(self):
        
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Sort':
                self.game.playing = True
            elif self.state == 'Search':
                pass
            elif self.state == 'Credits':
                pass
            self.run_display = False