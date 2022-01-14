import pygame, sys, copy
from settings import *
from Player import *

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

        self.load()
        self.cell_width = Maze_width//28
        self.cell_height= Maze_height//30
        self.player = Player(self, Player_Starting_POS)
        
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing'
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

########################## helper functions ################################

    def draw_text(self, text, screen, pos, size, colour, font_name, centered = False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text,pos)
        
    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

########################## intro functions ###############################
    
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'


    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered = True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered = True)
        self.draw_text('HIGH SCORE', self.screen, [4,0], START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()

########################## playing functions ###############################
    
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.fill(RED)
        pygame.display.update()

