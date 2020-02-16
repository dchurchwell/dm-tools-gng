import combat_turns
import dm_engine
import test_dice
import os

class TestInterface(dm_engine.Interface):
    def __init__(self):
        self.inputs = [
            # Initiative scores for the four players
            '-200',
            '100',
            '200',
            '-100',
            # Two test monsters
            'test monster',
            '2',
            '20',
            'x',
            # Lyan attacks a monster for 100 dmg
            '1', # Select attack
            '2', # Select monster
            '20', # Set AC
            '100', # Roll damage
            '110', # Set monster HP to 110
            # Keth does nothing
            '0',
            # Test monster creates a new attack
            '1',
            'Morningstar',
            '+200',
            '1d10+2 bludgeoning 1d6 fire',
            # Test monster does its new attack for max 12 bludgeoning and 6 fire against Keth
            '2', # Select the attack
            '1', # Select Keth
            '100', # Set Keth's AC
            '100', # Set Keth's HP
        ]
        self.in_index = -1
    def ask_DM(self, msg=''):
        self.in_index += 1

        if self.in_index >= len(self.inputs):
            quit()

        print(msg + self.inputs[self.in_index])
        return self.inputs[self.in_index]

    def DM_make_selection(self, items, text=''):
        self.in_index += 1

        if self.in_index >= len(self.inputs):
            quit()

        print(text)
        for i, item in enumerate(items):
            if type(item) == type(""): 
                print(f"[{i}]: {item}")
            else:
                print(f"[{i}]: {item.text}")
        print('Make a selection: ' + self.inputs[self.in_index])
        return items[int(self.inputs[self.in_index])]


for fname in ['monster_data/test_monster.json',
              'player_data/test_ari.json',
              'player_data/test_keth.json',
              'player_data/test_lyan.json',
              'player_data/test_kiir.json',]:
    if os.path.exists(fname):
        os.remove(fname)

window = TestInterface()
fight = combat_turns.Combat(window)
fight.set_combatants('test_players.txt')
fight.combat_loop()

combatants = fight.combatants

assert combatants[0].name == 'Lyan Amaranthia'
assert combatants[0].current_initiative == 200
assert 'test monster' in combatants[2].name
assert combatants[2].get('HP') == 10
assert 'test monster' in combatants[3].name
assert combatants[3].current_initiative > 20
assert combatants[3].current_initiative <= 40
