import pygame
pygame.init()
import sys
import defs.finals as finals
pygame.display.set_mode(finals.display_resolution['640x360'])
pygame.display.set_caption(finals.CAPTION)
from states.gameplay import Gameplay
from game import Game
import defs.lvl as lvl
game = Game(Gameplay(lvl.tmx_maps))
game.run()

pygame.quit()
sys.exit()
