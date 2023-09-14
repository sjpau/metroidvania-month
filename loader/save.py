import pygame
import json

class PersistentData:
    def __init__(self, spawner_id=None):
        self.player_abilities = {
            'hop': False,
            'slide': False,
            'dash': False,
        }
        self.current_area = ""
        self.spawner_id = spawner_id
        self.health = 3

    def save(self):
        save_data = {
            'abilities': self.player_abilities,
            'area': self.current_area,
            'spawner_id': self.spawner_id,
            'health': self.health,
        }
        with open('persistent_data.json', 'w', encoding ='utf8') as out_file:
            json.dump(save_data, out_file)
    
    def load(self, path):
        with open('persistent_data.json', 'r', encoding ='utf8') as in_file:
            save_data = json.load(in_file)
        self.player_abilities = save_data['abilities']
        self.current_area = save_data['area']
        self.spawner_id = save_data['spawner_id']
        self.health = save_data['health']