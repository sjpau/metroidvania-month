import pygame
pygame.init()
import sys
from states.gameplay import Gameplay
from game import Game
import defs.finals as finals
pygame.display.set_mode(finals.display_resolution['320x180'])
pygame.display.set_caption(finals.CAPTION)
game = Game(Gameplay())
game.run()

pygame.quit()
sys.exit()
