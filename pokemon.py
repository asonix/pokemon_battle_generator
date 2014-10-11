from item_list import items
import math

class Pokemon(object):
    """This class provides the base for all pokemon"""
    def __init__(self, base, item_number, ability_number, hp_ev, hp_iv,
            attack_ev, attack_iv, defense_ev, defense_iv, sp_atk_ev, sp_atk_iv,
            sp_def_ev, sp_def_iv, speed_ev, speed_iv, plus, minus):
        self.base_attr = {
                'name' : base['name'],
                'ability' : base['abilities'][ability_number],
                'hp' : base['hp'] + hp_ev + hp_iv,
                'attack' : base['attack'] + attack_ev + attack_iv,
                'defense' : base['defense'] + defense_ev + defense_iv,
                'sp_atk' : base['sp_atk'] + sp_atk_ev + sp_atk_iv,
                'sp_def' : base['sp_def'] + sp_def_ev + sp_def_iv,
                'speed' : base['speed'] + speed_ev + speed_iv,
                'type' : base['type'],
            }
        self.attr = {
                'item' : items[item_number],
                'hp' : self.base_attr['hp'],
                'attack' : self.base_attr['attack'],
                'defense' : self.base_attr['defense'],
                'sp_atk' : self.base_attr['sp_atk'],
                'sp_def' : self.base_attr['sp_def'],
                'speed' : self.base_attr['speed'],
                'type' : self.base_attr['type'],
                'status' : ''
            }
        self.attr[plus] += math.floor(self.attr[plus] * 0.1)
        self.attr[minus] -= math.floor(self.attr[minus] * 0.1)

