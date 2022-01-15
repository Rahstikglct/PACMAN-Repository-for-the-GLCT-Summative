# Go back to the settings file too make a change in the player settings
import pygame
from PacmanSettings import *
vec = pygame.math.Vector2 


class Player:
    def __init__(self,app,pos):
        self.grid_pos = pos
        self.app = app 
        self. pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None


    def update(self): #my update function
        self.pix_pos == self.direction
        if int(self.pix_pos.x + Top_Bottom_Buffer//2) % self.app.cell_width == 0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                if self.direction != None:
                    self.direction = self.stored_direction
        #
        if int(self.pix_pos.x + Top_Bottom_Buffer//2) % self.app.cell_heigth == 0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                if self.direction != None:
                    self.direction = self.stored_direction
        # I am setting gird position in reference to the pixel position
        self.grid_pos[0] = (self.pix_pos[0] - Top_Bottom_Buffer + self.app.cell_width//2)//self.app.cell_width + 1      
        self.grid_pos[1] = (self.pix_pos[1] - Top_Bottom_Buffer + self.app.cell_height//2)//self.app.cell_height + 1
        pass

    def draw(self): 
        # my pacman circle function
        pygame.draw.circle(self.app.screen, Player_colour, (int(self.pix_pos.x)),(int(self.pix_pos.y)),self.app.cell_width//2-2) 
        # drawing the grid position rectangle
        pygame.draw.rect(self.app.screen, Red, (self.grid_pos[0]*self.app.cell_width - Top_Bottom_Buffer//2, self.grid_pos[1] * self.app.cell_height - Top_Bottom_Buffer//2, self.app.cell.width, self.app.cell_height), 1)

    def move(self,direction):#my move function
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width) + Top_Bottom_Buffer//2 +self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height) +Top_Bottom_Buffer//2 + self.app.cell_heigth//2)
