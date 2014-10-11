def change_type(pokemon):
    """Changes type of pokemon with attributes p_dict"""
    pokemon.attr['type'] = pokemon.last_attack['type']

def change_attack(pokemon):
    """Changes attack of pokemon"""
    pokemon.attr['attack'] *= pokemon.base_attr['ability']['amount']

abilities = {
        'protean' : {
                'when' : 'move',
                'function' : change_type
            },
        'torrent' : {
                'when' : '<= 1/3 hp',
                'amount' : 1.5,
                'function' : change_attack
            }
        }

