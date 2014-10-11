#!/usr/bin/env python3

from pokemon import Pokemon
from pokemon_list import pokemon
from multi import setter

import json, os

def main():
    """Main function"""
    """base, item_number, ability_number, hp_ev, hp_iv,
            attack_ev, attack_iv, defense_ev, defense_iv, sp_atk_ev, sp_atk_iv,
            sp_def_ev, sp_def_iv, speed_ev, speed_iv, plus, minus"""

    if not os.path.isfile("ev_iv.json"):
        iv_list, ev_list = setter()
        with open("downloaded.json", 'w') as outfile:
            json.dump({'ev_list':ev_list, 'iv_list':iv_list}, outfile)
    else:
        ev_iv_data = open("ev_iv.json", "r").read()
        data = json.loads(ev_iv_data)
        ev_list = data['ev_list']
        iv_list = data['iv_list']

    for i in ev_list:
        for j in i:
            for k in j:
                for l in iv_list:
                    for m in l:
                        for n in m:
                            greninja = Pokemon(pokemon[0], 0, 0, k[0], n[0], k[1], n[1], k[2],
                                    n[2], k[3], n[3], k[4], n[4], k[5], n[5], "sp_atk", "sp_def")
                            print(greninja.attr)


main()
