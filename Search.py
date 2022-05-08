#G cost - distance from start node
#H (heuristic) cost - distance from end node
#F cost - G + H
import pygame
import random
from queue import PriorityQueue


WIDTH = 1000
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OCR")

#Static colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (153,255,153)
BLUE = (153,255,255)
PURPLE = (204,153,255)
RED = (255, 153, 153)
YELLOW = (255,255,153)


FPS = 60


#Node class
class Node:
    def __init__(self, x, y, a_x, a_y, width, color = WHITE):
            self.adjusted_x = a_x
            self.adjusted_y = a_y
            self.x = x
            self.y = y
            self.row = int(x/width)
            self.col = int(y/width)
            self.cord = (self.col, self.row)
            self.color = color
            self.width = width
            self.neighbors = []

    def __repr__(self):
        return str(self.col) +" " + str(self.row)

    def get_pos(self):
        return self.col, self.row

    def is_closed(self):
        return self.color is RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        if self.color == BLACK:
            return True
        else:
            return False

    def is_start(self):
        return self.color == BLUE

    def is_target(self):
        return self.color == YELLOW

    def is_path(self):
        return self.color == PURPLE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = BLUE

    def make_target(self):
        self.color = YELLOW

    def make_path(self):
        self.color = PURPLE

    def make_clear(self):
        self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.adjusted_x, self.adjusted_y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        #add left and right nodes
        for i in range(-1, 2):
            if (self.col + i) <= len(grid.grid_list) - 1 and (self.col + i) >=0:
                if not grid.grid_list[self.col + i][self.row].is_barrier():
                    self.neighbors.append(grid.grid_list[self.col + i][self.row])

        #add top and bottom nodes
        for j in range(-1, 2):
            if (self.row + j) <= len(grid.grid_list) -1 and (self.row + j) >= 0:
                if not grid.grid_list[self.col][self.row + j].is_barrier():
                    self.neighbors.append(grid.grid_list[self.col][self.row + j])

        #remove instances of self
        for index, node in enumerate(self.neighbors):
            if node is self or node.is_barrier():
                self.neighbors.pop(index)

    def __lt__(self, other):
        return False

#Grid class to take care of drawing and updating grid
class Grid:
    def __init__(self, start_x, start_y, end_x, end_y, win, number_blocks):
        self.start_x = start_x
        self.start_y = start_y
        self.delta_x = end_x - start_x
        self.delta_y = end_y - start_y
        self.start = None
        self.end = None
        self.win = win
        self.number_blocks = number_blocks
        self.blockSize = self.delta_x//number_blocks
        self.s_e = False
        self.grid_list = []
        #self.grid_list = [
            #[Node(x+start_x, y+start_y, self.blockSize) 
            #for x in range(0, self.delta_x, self.blockSize)] 
            #for y in range(0, self.delta_y, self.blockSize)
        #]
        for y in range(0, self.delta_y, self.blockSize):
            self.grid_list.append([])
            for x in range(0, self.delta_x, self.blockSize):
                box = Node(x, y, x+start_x, y+start_y, self.blockSize) 
                self.grid_list[y//self.blockSize].append(box)

        for row in self.grid_list:
            for box in row:
                box.update_neighbors(self)

    def draw(self):
        for row in self.grid_list:
            for box in row:
                box.draw(self.win)

        for y in range(0, self.delta_y, self.blockSize):
            for x in range(0, self.delta_x, self.blockSize):
                rect = pygame.Rect(x+self.start_x, y+self.start_y, self.blockSize, self.blockSize) #create and draw grid
                pygame.draw.rect(self.win, BLACK, rect, 1)


    def clear_all(self):
        for row in self.grid_list:
            for box in row:
                box.make_clear()
        self.s_e = False


    def generate_start_end(self):
        if self.s_e == False:
            s_y, s_x = random.randint(0, self.number_blocks-1), random.randint(0, self.number_blocks-1)
            e_y, e_x = random.randint(0, self.number_blocks-1), random.randint(0, self.number_blocks-1)
            if s_y != e_y and s_x != e_x:
                self.grid_list[s_y][s_x].make_start()
                self.start = self.grid_list[s_y][s_x]
                self.grid_list[e_y][e_x].make_target()
                self.end = self.grid_list[e_y][e_x]
                self.s_e = True
            else:
                self.generate_start_end()

    def reconstruct_path(self, came_from, current):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw(self.win, self)

    def astar_search(self):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, self.start))
        came_from = {}
        g_score = {node: float("inf") for row in self.grid_list for node in row}
        g_score[self.start] = 0
        f_score = {node: float("inf") for row in self.grid_list for node in row}
        f_score[self.start] = h(self.start.get_pos(), self.end.get_pos())

        open_set_hash = {self.start}

        while not open_set.empty():

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            #start by popping lowest cost node
            #get just the node from the get function
            current = open_set.get()[2]
            current.update_neighbors(self)
            open_set_hash.remove(current)

            if current == self.end:
                self.reconstruct_path(came_from, self.end)
                self.end.make_path()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), self.end.get_pos())
                    if neighbor not in open_set_hash:
                        count +=1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            
            draw(self.win, self)
            
            if current != self.start:
                current.make_closed()
        return None

def h(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(y2 - y1) + abs(x2 - x1)

def draw(win, grid):
    win.fill(BLACK)
    grid.draw()
    pygame.display.update()




def main(start_x, start_y, end_x, end_y, number_blocks, win):
    run = True
    clock = pygame.time.Clock()
    grid = Grid(start_x, start_y, end_x, end_y, win, number_blocks)
    div_factor = grid.grid_list[0][0].width

    while run:
        draw(win, grid)
        clock.tick(FPS)
        for event in pygame.event.get():


            #left click barrier creation function
            if pygame.mouse.get_pressed() == (1,0,0):
                x_box, y_box = pygame.mouse.get_pos()
                if start_x <= x_box and x_box <= end_x and start_y <= y_box and y_box  <= end_y:
                    x, y = int((x_box-start_x)/div_factor), int((y_box-start_y)/div_factor)
                    grid.grid_list[y][x].make_barrier()

            #right click barrier remove function
            if pygame.mouse.get_pressed() == (0,0,1):
                x_box, y_box = pygame.mouse.get_pos()
                if start_x <= x_box and x_box <= end_x and start_y <= y_box and y_box  <= end_y:
                    x, y = int((x_box-start_x)/div_factor), int((y_box-start_y)/div_factor)
                    grid.grid_list[y][x].make_clear()


            if event.type == pygame.KEYDOWN:
                if str(pygame.key.name(event.key)).upper() == "BACKSPACE":
                    #grid.clear_all()

                    grid.astar_search()


                if str(pygame.key.name(event.key)).upper() == "RETURN":
                    grid.generate_start_end()
                    

            if event.type == pygame.QUIT:
                run = False

    
    pygame.quit()


main( 20, 20, 980, 980, 48, WIN)