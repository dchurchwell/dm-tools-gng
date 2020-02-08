import combat_turns
import dm_engine
import test_dice
import os

class TestInterface(dm_engine.Interface):
    def __init__(self):
        self.inputs = [
            '-200',
            '100',
            '200',
            '-100',
            'test monster',
            '2',
            '20',
            'x',
            '',
            '',
            '',
        ]
        self.in_index = -1
    def ask_DM(self, msg=''):
        self.in_index += 1

        if self.in_index >= len(self.inputs):
            quit()

        print(msg + self.inputs[self.in_index])
        return self.inputs[self.in_index]


if os.path.exists('monster_data/test_monster.json'):
    os.remove('monster_data/test_monster.json')

window = TestInterface()
fight = combat_turns.Combat(window)
fight.set_combatants('test_players.txt')
fight.combat_loop()

combatants = fight.combatants

assert combatants[0].name == 'Lyan Amaranthia'
assert combatants[0].current_initiative == 200
assert 'test monster' in combatants[2].name
assert 'test monster' in combatants[3].name
assert combatants[3].current_initiative > 20
assert combatants[3].current_initiative <= 40
