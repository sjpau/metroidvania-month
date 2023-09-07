import pygame
import sys
import defs.finals as finals
pygame.init()
pygame.display.set_mode(finals.display_resolution['1280x720'])
pygame.display.set_caption(finals.CAPTION)
from states.gameplay import Gameplay
from game import Game
import defs.lvl as lvl
game = Game(Gameplay(lvl.tmx_maps))
game.run()

pygame.quit()
sys.exit()
