from colorsys import rgb_to_yiq
import pygame
from PacmanSettings import *
vec = pygame.math.Vector2


class Enemy:
    def _init_(self,app, pos, number):
        self.app = app
        self.grid = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = self.app.cell_width//2.3
        self.number = number 
        self.colour = self.set_colour()
        self.direction = vec(0,0)
        self.personality = self.set_personality()
        print (self.personality)


    def update(self):
        self.pix_pos += self.direction
        if self.time_to_move:
            self.move()

    def draw(self):
        if self.number == 0:
            pygame.draw.circle(self.app.screen, self.colour, (int(self.pix_pos.x), int(self.pix_pos.y)), self.radius)
    
    def time_to_move(self):
        pass

    def move(self):
        pass

    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width) + Top_Bottom_Buffer//2 +self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height) +Top_Bottom_Buffer//2 + self.app.cell_heigth//2)

    def set_colour(self):
        if self.number == 0:
            return  (42,78,203)
        if self.number == 1:
            return  (197,200,27)
        if self.number == 2:
            return  (189,29,29)
        if self.number == 3:
            return  (215,159,33)


    def set_personality(self):
        if self.number == 0:
            return "speedy"
        elif self.number == 1:
            return "slow"
        if self.number == 2:
            return "random"
        else:
            return "scared"
