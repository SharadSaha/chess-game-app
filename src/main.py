import pygame
import sys

from DEF import *

class Main:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("CHESS GAME")

    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

    

app=Main()
app.run()