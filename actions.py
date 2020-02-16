from dice import d, roll

class Action():
    def __init__(self, text='', interface=None):
        self.text = text
    def __call__(self):
        return self.text


class Attack(Action):
    def __init__(self, mob, bonus='0', dmg='0', text='Attack'):
        self.mob = mob
        self.bonus = int(bonus)
        self.dmg = dmg
        self.text = f"{text} (+{bonus}, {dmg})"

    def __call__(self):
        # Select target
        target = self.mob.interface.DM_make_selection(self.mob.combat.combatants, 'Select target:')

        # Make an attack
        atkRoll = d(20)
        if atkRoll == 1:
            return "Missed - Critical failure!"
        crit = False
        if atkRoll == 20:
            crit = True
        atkRoll += self.bonus

        if crit or atkRoll >= target.get('AC'):
            dmg = roll(self.dmg, crit)
            target.take_dmg(dmg)
            return f"Rolled {atkRoll} for {dmg} damage."
        
        return f"Rolled {atkRoll} - Missed!"

class PlayerAttack(Action):
    def __init__(self, mob, text='Make an attack'):
        self.text = text
        self.mob = mob
    def __call__(self):
        # Select target
        target = self.mob.interface.DM_make_selection(self.mob.combat.combatants, 'Select target:')
        self.mob.interface.tell_DM(f"{target.name}'s AC is {target.get('AC')}")
        dmg = self.mob.interface.ask_DM("Enter damage:")
        target.take_dmg(dmg)
        return f"{self.mob.name} hits {target.name} for {dmg}"



class CreateAttack(Action):
    def __init__(self, mob):
        self.mob = mob
        self.text = "Create a new attack"
    def __call__(self):
        name = self.mob.interface.ask_DM("Enter attack name: ")
        bonus = self.mob.interface.ask_DM("Enter attack bonus: ")
        dmg = self.mob.interface.ask_DM("Enter damage dice and types: ")
        self.mob.actions.append(Attack(self.mob, bonus, dmg, name))
        self.mob.do_action()
        return f"Created {name} attack ({bonus}, {dmg})"