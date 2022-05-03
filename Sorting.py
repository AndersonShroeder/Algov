 

import pygame
from random import randint


WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (153,255,255)
PURPLE = (224,153,255)
RED = (255, 153, 153)
YELLOW = (255,255,153)
GREY = (224, 224, 224)

FPS = 240

class Node():
    def __init__(self, value, width, index, y, margin):
        self.value = value
        self.color = PURPLE
        self.index = index
        self.margin = margin
        self.x = width * self.index + margin
        self.y = y
        self.width = width
        self.count = 0

    def __repr__(self):
        return str(self.value) + "; " + str(self.index)

    def change_x(self, new_index):
        self.index = new_index
        self.x = self.width * (new_index) + self.margin

    def draw(self, win):
        pygame.draw.rect(win, GREY, (self.x, self.y-self.value, self.width, self.value))
        pygame.draw.rect(win, self.color, (self.x + 1, self.y-self.value, self.width -2, self.value))
        

    def normal(self):
        self.color = PURPLE

    def searching(self):
        self.color = GREEN
    
    def red(self):
        self.color = RED 
        
        
fpsclock = pygame.time.Clock()

class List():
    def __init__(self,elements, rng, game, margin):
        self.win = game.window
        self.elements = elements
        self.rng = rng
        self.margin = margin
        self.width = game.DISPLAY_W - 2 * self.margin
        self.height = game.DISPLAY_H
        self.lst = []
        self.display = game.display
        self.count = 0

    def swap(self, index1, index2):
        self.lst[index1].change_x(index2), self.lst[index2].change_x(index1)
        self.lst[index1], self.lst[index2] = self.lst[index2], self.lst[index1]
        
    #generate list function
    def generate_list(self):   
        jump = self.rng//self.elements
        w = self.width/self.elements
        for i in range(self.elements):
            self.lst.append(Node(((i + 1)* jump), w, i, self.height, self.margin))
        
            self.blit_screen()

            #Delay for visibility
            pygame.time.delay(2)

    #Randomize list
    def randomize_list(self):
        for i in range(len(self.lst)):

            rnd = randint(0, len(self.lst)-1)
            
            self.swap(i, rnd)
            self.blit_screen()

            #Delay for visibility
            pygame.time.delay(2)

    def quicksort(self):
        self.quick_sort(0, len(self.lst) - 1)

    def quick_sort(self, left, right):
        if left < right:
            partition_pos = self.partition(left, right)
            self.quick_sort(left, partition_pos -1)
            self.quick_sort(partition_pos + 1, right)
        
    def partition(self, left, right):
        i = left
        j = right -1
        pivot = self.lst[right].value

        while i < j:
            while i < right and self.lst[i].value < pivot:
                self.lst[i].red()
                i +=1
                self.blit_screen()
                self.lst[i-1].normal()
            while j > left and self.lst[j].value >= pivot:
                self.lst[j].red()
                j -=1
                self.blit_screen()
                self.lst[j+1].normal()
            if i < j:
                self.swap(i, j)
                self.blit_screen()
        if self.lst[i].value > pivot:
            self.swap(i, right)
            self.blit_screen()
        return i


    def bubble_sort(self):
        x = len(self.lst)
        
        for i in range(x):

            for j in range(0, x-i-1):
                self.lst[j].red()
                if self.lst[j].value > self.lst[j + 1].value:
                    self.swap(j, j+1)
                self.blit_screen()
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
            self.blit_screen()
            

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
            self.blit_screen()


        while left_pointer < len(left):
            #Check
            left[left_pointer].red()
            self.blit_screen()

            if left[left_pointer].index < min:
                min = left[left_pointer].index

            result.append(left[left_pointer])
            left_pointer += 1

            #Normal
            left[left_pointer - 1].normal()
 

        while right_ponter < len(right):
            right[right_ponter].red()
            self.blit_screen()

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
            
        self.blit_screen()

        #draw sequence of sorted subarray
        for node in result:
            node.red()
            self.blit_screen()
            node.normal()
        

        return result



    def insertion_sort(self):
        #check node - if greater than node on left, swap positions until not greater than node on left
        for i in range(1, len(self.lst)):
            j = i
            self.lst[j].red()
            while self.lst[j -1].value > self.lst[j].value and j > 0:
                self.swap(j, j-1)
                self.blit_screen()
                j -= 1
            self.lst[j].normal()
        self.finished()




    def finished(self):
        for i in self.lst:
            i.red()
            
            self.blit_screen()
            pygame.time.delay(2)
            i.searching()

    def blit_screen(self):
        self.win.blit(self.display, (0,0))
        for node in self.lst:
            node.draw(self.win)
        
        pygame.display.update()
        #fpsclock.tick(FPS)
        
        self.exit_loop()

    def exit_loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if