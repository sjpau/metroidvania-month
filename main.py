import pygame
import sys
import defs.finals as finals
pygame.init()
pygame.display.set_mode(finals.display_resolution['1280x720'])
pygame.display.set_caption(finals.CAPTION)
from game import Game
from entity.player import Player
import defs.lvl as lvl
from loader.save import PersistentData

save = PersistentData()
save.load('persistent_data.json')
lvl.states_non_gameplay['main_menu'].player_persistent_data = save
game = Game(lvl.states_non_gameplay['main_menu']) 
game.run()

pygame.quit()
sys.exit()
