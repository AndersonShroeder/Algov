
from ctypes import pointer
import pygame
from random import randint


WIDTH = 1000
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algo")
display_surface = pygame.display.get_surface()
display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (153,255,255)
PURPLE = (204,153,255)
RED = (255, 153, 153)
YELLOW = (255,255,153)

FPS = 60

class Node():
    def __init__(self, value, width, index):
        self.value = value
        self.color = WHITE
        self.index = index
        self.x = width * self.index
        self.y = 1000
        self.width = width
        self.count = 0

    def __repr__(self):
        return str(self.value) + "; " + str(self.index)

    def change_x(self, new_index):
        self.index = new_index
        self.x = self.width * (new_index)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y-self.value, self.width, self.value))

    def normal(self):
        self.color = WHITE

    def searching(self):
        self.color = GREEN
    
    def red(self):
        self.color = RED 
        
def exit_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

class List():
    def __init__(self, win, elements, rng, window_width):
        self.win = win
        self.elements = elements
        self.rng = rng
        self.width = window_width
        self.lst = []
        self.count = 0

    #generate list function
    def generate_list(self):   
        jump = self.rng//self.elements
        w = self.width/self.elements
        for i in range(self.elements):
            self.lst.append(Node(((i + 1)* jump), w, i))
        
            draw(self.win, self.lst)

            #Delay for visibility
            pygame.time.delay(20)

    #Randomize list
    def randomize_list(self):
        for i in range(len(self.lst)):

            rnd = randint(0, len(self.lst)-1)
            self.lst[i].change_x(rnd), self.lst[rnd].change_x(i)
            self.lst[i], self.lst[rnd] = self.lst[rnd], self.lst[i]
            draw(self.win, self.lst)

            #Delay for visibility
            pygame.time.delay(20)

    def bubble_sort(self):
        x = len(self.lst)
        
        for i in range(x):

            for j in range(0, x-i-1):
                self.lst[j].red()
                if self.lst[j].value > self.lst[j + 1].value:
                    self.lst[j].change_x(j + 1), self.lst[j + 1].change_x(j)
                    self.lst[j], self.lst[j + 1] = self.lst[j+ 1], self.lst[j]
                draw(self.win, self.lst)
                pygame.time.delay(2)
                self.lst[j + 1].normal()
                self.lst[j].normal()

        self.finished()




    def merge_sort(self, array):
        if len(array) <= 1:
            return array
        midpoint = len(array)//2
        self.count += 1
        lft, rght = self.merge_sort(array[:midpoint]), self.merge_sort(array[midpoint:])
        return self.merge(lft, rght)

    def merge(self, left, right):
        result = []
        left_pointer = right_ponter = 0

        min = left[0].index
        k = 0


        print(left, right)
        while left_pointer < len(left) and right_ponter < len(right):

            if left[left_pointer].value < right[right_ponter].value:

                if left[left_pointer].index < min:
                    min = left[left_pointer].index
                result.append(left[left_pointer])

                left_pointer += 1



            else:

                if right[right_ponter].index < min:
                    min = right[right_ponter].index

                result.append(right[right_ponter])
                right_ponter += 1





        while left_pointer < len(left):
            if left[left_pointer].index < min:
                min = left[left_pointer].index
            result.append(left[left_pointer])
            left_pointer += 1




        while right_ponter < len(right):
            if right[right_ponter].index < min:
                min = right[right_ponter].index

            result.append(right[right_ponter])
            right_ponter += 1

        print(result)
        return result

    def finished(self):

        for i in self.lst:
            i.red()
            
            draw(self.win, self.lst)
            pygame.time.delay(20)
            i.searching()


def draw(win, lst):
    win.fill(BLACK)
    for node in lst:
        node.draw(win)
    pygame.display.update()

    #exit loop in draw function = easiest
    exit_loop()


def main(win, elements, rng, width):
    run = True
    clock = pygame.time.Clock()
    lst = List(win, elements, rng, width)

    while run:
        draw(win, lst.lst)
        clock.tick(FPS)
        for event in pygame.event.get():

            if pygame.mouse.get_pressed() == (1,0,0):
                lst.generate_list()
                lst.randomize_list()
                lst.merge_sort(lst.lst)
            
            if event.type == pygame.QUIT:
                run = False

    
    pygame.quit()

main(WIN, 100, 1000, 1000)
#Click start - Creates/draws sorted list - then randomizes the list visually - then sorts
