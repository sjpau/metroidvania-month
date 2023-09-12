import pygame
import sys
import defs.finals as finals
pygame.init()
pygame.display.set_mode(finals.display_resolution['1280x720'])
pygame.display.set_caption(finals.CAPTION)
from game import Game
from entity.player import Player
import defs.lvl as lvl

lvl.desert_areas['desert_one'].preload()

game = Game(lvl.desert_areas['desert_one']) # TODO start from main menu
game.run()

pygame.quit()
sys.exit()
