import csv
from dice import *

import mobs
import players
import dm_engine

class Combat:
    def __init__(self, interface):
        self.interface = interface

    def set_combatants(self, player_file = "players.txt"):
        # Get player initiative scores
        combatants = players.load_player_data(player_file)
        print("Enter initiative scores for the players: ")
        for player in combatants:
            player.interface = self.interface
            player.combat = self
            player.current_initiative = int(self.interface.ask_DM(player.name + ':'))

        print("Add monsters:  (Enter X when done)")
        while True:
            mobname = self.interface.ask_DM("Name: ")
            if mobname in ['x', 'X']:
                break
            num_mobs = int(self.interface.ask_DM("Number: "))

            # Format file name based on mob name
            filename = 'monster_data/' + '_'.join(mobname.split(' ')) + '.json'

            for i in range(num_mobs):
                # Create a mob and add it to the combatants
                if num_mobs > 1:
                    name_num = mobname + ' ' + str(i+1)
                else:
                    name_num = mobname
                this_mob = mobs.Mob(name_num, self.interface, filename)
                this_mob.roll_initiative(self)
                combatants.append(this_mob)
                
            # Sort combatants
            combatants.sort(key=lambda x: x.current_initiative, reverse=True)

            self.combatants = combatants
            
        # Collect combatants from files and input
        for mob in self.combatants:
            self.interface.tell(f"{mob.name} rolled {mob.current_initiative}")

    def combat_loop(self):

        i = 0
        while True:
            # Output who's going next
            combatant = self.combatants[i]
            self.interface.tell(f"It's {combatant.name}'s turn!")

            # Have them act (Move, Action, Bonus Action, Free Action)
            combatant.do_action()

            # Confirm end of turn
            #self.interface.ask_DM()

            # Move to the next person
            i += 1
            i = i % len(self.combatants)

