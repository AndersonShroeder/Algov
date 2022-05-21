import pygame
import Search

y_offset = 40 #distance of options from top of screen
x_offset = 50# distance of options from eachother/edge of screen
cursor_offset = 30
banner_y_offset = 80
FONT_SIZE = 20


class Menu():
    def __init__(self,game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0, 20,20)
        self.offset = -100 #offset

    def draw_cursor(self):
        self.game.draw_text('*', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        for node in self.game.lst.lst:
            node.draw(self.game.window)
        pygame.display.update()
        self.game.reset_keys()

    def blit_screen_grid(self):
        self.game.window.blit(self.game.display, (0,0))
        for row in self.game.grid.grid_list:
            for node in row:
                node.draw(self.game.window)

        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game) #init with all the values of a Menu class
        self.state = "Sort"
        self.sortingx, self.sortingy = self.mid_w, self.mid_h + 30
        self.searchx, self.searchy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.sortingx + self.offset, self.sortingy)
        self.banner = pygame.Rect(game.DISPLAY_W * 3/10, game.DISPLAY_H * 3/10, game.DISPLAY_W * 4/10,  game.DISPLAY_H * 4/10)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events() #set flags to allow to move cursor
            self.check_input()
            self.game.display.fill(self.game.GREY)
            self.game.draw_rect(self.banner)
            self.game.draw_text("Main Menu", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H / 2 - 20) #Main menu title is at the center slighty above options
            self.game.draw_text("Sorting Algorithms", 20, self.sortingx, self.sortingy)
            self.game.draw_text("Search Algorithms", 20, self.searchx, self.searchy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            #if down key is pressed, curosr is moved to next option and state is adjusted accordingly
            if self.state == 'Sort':
                self.cursor_rect.midtop = (self.searchx + self.offset, self.searchy)
                self.state = 'Search'
            elif self.state == 'Search':
                self.cursor_rect.midtop = (self.sortingx + self.offset, self.sortingy)
                self.state = 'Sort'
        elif self.game.UP_KEY:
            if self.state == 'Sort':
                self.cursor_rect.midtop = (self.searchx + self.offset, self.searchy)
                self.state = 'Search'
            elif self.state == 'Search':
                self.cursor_rect.midtop = (self.sortingx + self.offset, self.sortingy)
                self.state = 'Sort'


    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Sort':
                self.game.curr_menu = SortingMenu(self.game)
            elif self.state == 'Search':
                self.game.curr_menu = SearchMenu(self.game)
            elif self.state == 'Options':
                pass
            self.run_display = False

class SortingMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Bubble'
        self.bubw, self.insw = self.game.text_width("Bubble Sort", FONT_SIZE), self.game.text_width("Insertion Sort", FONT_SIZE)
        self.mergew, self.neww =self.game.text_width("Merge Sort", FONT_SIZE), self.game.text_width("Generate New List", FONT_SIZE)
        self.quickw = self.game.text_width("Quick Sort", FONT_SIZE)
        self.bubx, self.buby = x_offset+50, y_offset #menu buttons across top sep x pixels
        self.insx, self.insy = self.bubw//2 + self.bubx + self.insw//2 + x_offset, y_offset
        self.mergex, self.mergey = self.insx + self.insw//2 + self.mergew//2 + x_offset, y_offset
        self.quickx, self.quicky  = self.mergex + self.mergew//2 + self.quickw//2 + x_offset, y_offset
        self.newx, self.newy = self.quickx + self.quickw//2 + self.neww//2 + x_offset, y_offset
        self.banner = pygame.Rect(0, 0, game.DISPLAY_W, banner_y_offset)
        self.cursor_rect.midtop = (self.bubx, self.buby + cursor_offset)
        self.lst_printed = False

    def move_cursor(self):
        if self.game.DOWN_KEY:
            #if down key is pressed, curosr is moved to next option and state is adjusted accordingly
            if self.state == 'Bubble':
                self.cursor_rect.midtop = (self.newx, self.newy + cursor_offset)
                self.state = 'New'
            elif self.state == 'Merge':
                self.cursor_rect.midtop = (self.insx, self.insy + cursor_offset)
                self.state = 'Insert'
            elif self.state == 'Insert':
                self.cursor_rect.midtop = (self.bubx, self.buby + cursor_offset)
                self.state = 'Bubble'
            elif self.state == 'New':
                self.cursor_rect.midtop = (self.quickx, self.quicky + cursor_offset)
                self.state = 'Quick'
            elif self.state == 'Quick':
                self.cursor_rect.midtop = (self.mergex, self.mergey + cursor_offset)
                self.state = 'Merge'
        elif self.game.UP_KEY:
            if self.state == 'Bubble':
                self.cursor_rect.midtop = (self.insx, self.insy + cursor_offset)
                self.state = 'Insert'
            elif self.state == 'Insert':
                self.cursor_rect.midtop = (self.mergex, self.mergey + cursor_offset)
                self.state = 'Merge'
            elif self.state == 'Merge':
                self.cursor_rect.midtop = (self.quickx, self.quicky + cursor_offset)
                self.state = 'Quick'
            elif self.state == 'Quick':
                self.cursor_rect.midtop = (self.newx, self.newy + cursor_offset)
                self.state = 'New'
            elif self.state == 'New':
                self.cursor_rect.midtop = (self.bubx, self.buby + cursor_offset)
                self.state = 'Bubble'

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.GREY)
            self.game.draw_rect(self.banner)
            self.game.draw_text("Bubble Sort", FONT_SIZE, self.bubx, self.buby)
            self.game.draw_text("Insertion Sort", FONT_SIZE, self.insx, self.insy)
            self.game.draw_text("Merge Sort", FONT_SIZE, self.mergex, self.mergey)
            self.game.draw_text("Quick Sort", FONT_SIZE, self.quickx, self.quicky)
            self.game.draw_text("Generate New List", FONT_SIZE, self.newx, self.newy)
            self.draw_cursor()
            self.blit_screen()
            if not self.lst_printed:
                self.game.lst.generate_list()
                self.game.lst.randomize_list()
                self.lst_printed = True
            pygame.display.update()
 
    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.lst.lst = []
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            #initiate search
            if self.state == 'Bubble':
                self.game.lst.bubble_sort()
            elif self.state == 'Insert':
                self.game.lst.insertion_sort()
            elif self.state == 'Merge':
                self.game.lst.merge_sort()
            elif self.state == 'Quick':
                self.game.lst.quicksort()
            elif self.state == 'New':
                self.game.lst.lst = []
                self.game.lst.generate_list()
                self.game.lst.randomize_list()
            self.run_display = False

class SearchMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.game.grid = Search.Grid(
                                    self.game.DISPLAY_W * 1//20, 
                                    (self.game.DISPLAY_H - banner_y_offset) * 1//20 + banner_y_offset, 
                                    self.game.DISPLAY_W * 19//20, 
                                    (self.game.DISPLAY_H - banner_y_offset) * 19//20 + banner_y_offset, 
                                    self.game, 50
                                    )
        self.state = 'A*'
        self.astarw = self.game.text_width("A* Search", FONT_SIZE)
        self.neww = self.game.text_width("Generate New Grid", FONT_SIZE)
        self.astarx, self.astary = x_offset+50, y_offset #menu buttons across top sep x pixels
        self.newx, self.newy = self.astarw//2 + self.astarx + self.neww//2 + x_offset, y_offset
        self.banner = pygame.Rect(0, 0, game.DISPLAY_W, banner_y_offset)
        self.cursor_rect.midtop = (self.astarx, self.astary + cursor_offset)
        self.lst_printed = False
        self.grid_printed = False
        

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'A*':
                self.cursor_rect.midtop = (self.newx, self.newy + cursor_offset)
                self.state = 'New'
            elif self.state == 'New':
                self.cursor_rect.midtop = (self.astarx, self.astary + cursor_offset)
                self.state = 'A*'
        elif self.game.UP_KEY:
            if self.state == 'A*':
                self.cursor_rect.midtop = (self.newx, self.newy + cursor_offset)
                self.state = 'New'
            elif self.state == 'New':
                self.cursor_rect.midtop = (self.astarx, self.astary + cursor_offset)
                self.state = 'A*'
            
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.GREY)
            self.game.draw_rect(self.banner)
            self.game.draw_text("A* Search", FONT_SIZE, self.astarx, self.astary)
            self.game.draw_text("Generate New Grid", FONT_SIZE, self.newx, self.newy)
            self.draw_cursor()
            self.blit_screen_grid()
            if not self.grid_printed:
                self.game.grid.generate_grid()
                self.game.grid.generate_start_end()
                self.grid_printed = True
            pygame.display.update()
 
    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.grid.grid_list = []
            self.game.curr_menu = self.game.main_menu
            self.run_display = False


        #left click barrier creation function
        elif pygame.mouse.get_pressed() == (1,0,0):
            self.game.grid.click().make_barrier()

        #right click barrier remove function
        elif pygame.mouse.get_pressed() == (0,0,1):
            self.game.grid.click().make_clear()


        elif self.game.START_KEY:
            if self.state == "A*":
                self.game.grid.astar_search()
            if self.state == 'New':
                self.game.grid.grid_list = []
                self.game.grid.generate_grid()
                self.game.grid.generate_start_end()
            self.run_display = False