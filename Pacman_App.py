import pygame
import sys
import copy
from PacmanSettings import *
from PacmanPlayer import *

pygame.init()
vec = pygame.math.Vector2

class App:
    def _init_(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = Maze_width//28
        self.cell_height= Maze_height//30
        self.player = Player(self, Player_Starting_POS)

    def run(self):
        while (self.running == True): 
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
                self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
    
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def intro_update(self):
        pass

    def intro_draw(self):
        pass
# alot need to be done in draw and update
    def playing_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0,-1))

   
    def playing_update(self):
        self.player.update()
        pass

    def playing_draw(self):
    #code for background here
        self.screen.fill(Black)
        self.screen.blit(self.background,(Top_Bottom_Buffer//2, Top_Bottom_Buffer//2))
        self.draw_grid()
        self.draw_text('Current Score: 0', self.screen, [60,0,], 18, White, Start_font)
        self.player.draw()
        pygame.display.update()
        