
import pygame
from random import randint


# WIDTH = 1000
# HEIGHT = 1000
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Sorting Algo")
# display_surface = pygame.display.get_surface()
# display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))

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

    def swap(self, index1, index2):
        self.lst[index1].change_x(index2), self.lst[index2].change_x(index1)
        self.lst[index1], self.lst[index2] = self.lst[index2], self.lst[index1]
        

    #generate list function
    def generate_list(self):   
        jump = self.rng//self.elements
        w = self.width/self.elements
        for i in range(self.elements):
            self.lst.append(Node(((i + 1)* jump), w, i))
        
            draw(self.win, self.lst)

            #Delay for visibility
            pygame.time.delay(2)

    #Randomize list
    def randomize_list(self):
        for i in range(len(self.lst)):

            rnd = randint(0, len(self.lst)-1)
            
            self.swap(i, rnd)
            draw(self.win, self.lst)

            #Delay for visibility
            pygame.time.delay(2)



    def bubble_sort(self):
        x = len(self.lst)
        
        for i in range(x):

            for j in range(0, x-i-1):
                self.lst[j].red()
                if self.lst[j].value > self.lst[j + 1].value:
                    self.swap(j, j+1)
                draw(self.win, self.lst)
                #pygame.time.delay()
                self.lst[j + 1].normal()
                self.lst[j].normal()
        self.finished()



    #Calls the merge sort function on self.lst
    def merge_sort(self):
        self.lst = self.merge(self.lst)
        self.finished()



    def merge(self, array):
        #Recursive call = divide
        if len(array) <= 1:
            return array
        midpoint = len(array)//2
        self.count += 1
        left, right = self.merge(array[:midpoint]), self.merge(array[midpoint:])


        #Merge
        result = []
        left_pointer = right_ponter = 0

        min = left[0].index
        while left_pointer < len(left) and right_ponter < len(right):

            #Check each node at both side = make red
            left[left_pointer].red(), right[right_ponter].red()
            draw(self.win, self.lst) 
            pygame.time.delay(5)

            #Update Min if less than left pointer value index
            if left[left_pointer].index < min:
                min = left[left_pointer].index

            #Update Min if less than right pointer value index
            if right[right_ponter].index < min:
                min = right[right_ponter].index

            if left[left_pointer].value < right[right_ponter].value:
                result.append(left[left_pointer])
                left_pointer += 1

            else:
                result.append(right[right_ponter])
                right_ponter += 1

            #Make node normal
            left[left_pointer - 1].normal(), right[right_ponter - 1].normal()
            draw(self.win, self.lst)


        while left_pointer < len(left):
            #Check
            left[left_pointer].red()
            draw(self.win, self.lst) 

            if left[left_pointer].index < min:
                min = left[left_pointer].index

            result.append(left[left_pointer])
            left_pointer += 1

            #Normal
            left[left_pointer - 1].normal()
 

        while right_ponter < len(right):
            right[right_ponter].red()
            draw(self.win, self.lst) 

            if right[right_ponter].index < min:
                min = right[right_ponter].index

            result.append(right[right_ponter])
            right_ponter += 1

            right[right_ponter - 1].normal()
       
        
        #once done comparing and have final list draw final list
        #Swap position in grid
        #keep track of min index - for as man nodes in result increment the min index and assign new index for each node
        max = min
        for index, node in enumerate(result):
            node_index = node.index
            swap_index = min + index
            self.swap(node_index, swap_index)
            max += index
            
        draw(self.win, self.lst)

        #draw sequence of sorted subarray
        for node in result:
            node.red()
            draw(self.win, self.lst)
            pygame.time.delay(5)
            node.normal()
        

        return result



    def insertion_sort(self):
        #check node - if greater than node on left, swap positions until not greater than node on left
        for i in range(1, len(self.lst)):
            j = i
            self.lst[j].red()
            while self.lst[j -1].value > self.lst[j].value and j > 0:
                self.swap(j, j-1)
                #pygame.time.delay(1)
                draw(self.win,self.lst)
                j -= 1
            self.lst[j].normal()
        self.finished()




    def finished(self):
        for i in self.lst:
            i.red()
            
            draw(self.win, self.lst)
            pygame.time.delay(2)
            i.searching()


def draw(win, lst):
    for node in lst:
        node.draw(win)
    pygame.display.update()

    #exit loop in draw function = easiest
    exit_loop()

