import combat_turns
import dm_engine
import os

window = dm_engine.Interface()
fight = combat_turns.Combat(window)
fight.set_combatants()
fight.combat_loop()

