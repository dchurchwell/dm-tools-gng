from dice import *
import json
import actions

class Mob():
    def __init__(self, name, interface=None, filename=None, player_name='DM', combat=None):
        self.combat=combat
        self.attributes = {}
        self.player = player_name
        self.interface = interface

        self.name = name
        self.text = self.name
        self.filename = filename

        self.actions = []

        # Set filename based on name
        if filename == None:
            filename = 'monster_data/' + name + '.json'
        
        # Load from file if exists
        if not filename == None:
            self.load_from_file(filename=None)
    

    def load_from_file(self, filename):
        """Loads mob data from json file
        
        Keyword Arguments:
            filename {string} -- The file to load from. (default: {None})
        """        
        if filename == None:
            filename = self.filename
        try:
            with open(filename) as f:
                load = json.load(f)
                self.attributes = load['attributes']
        except FileNotFoundError:
            print('No file for', self.name)

    def save_to_file(self, filename=None):
        """Saves mob data to json file
        
        Keyword Arguments:
            filename {string} -- The file to save to. (default: {None})
        """        
        if filename == None:
            filename = self.filename
        with open(filename, 'w+') as f:
            f.write(json.dumps({
                'attributes': self.attributes,
                #'actions': self.actions
            }))
    
    def get(self, attribute_name):
        """Returns the score for an attribute, such as ability scores or skill checks.
            Will ask for input if no score is found.
        
        Arguments:
            attribute_name {string} -- The name of the attribute to get
        
        Returns:
            int -- The score of the attribute
        """        
        if attribute_name in self.attributes:
            return self.attributes[attribute_name]
        else:
            val = self.interface.ask_DM(
                f"No {attribute_name} score found for {self.name}. Please enter a value, or press X to cancel.\n")
            if val in ['x', 'X']:
                return None
            else:
                self.attributes[attribute_name] = int(val)
                self.save_to_file()
                return int(val)
    
    def take_dmg(self, dmg=0):
        try:
            dmg = int(dmg)
            self.attributes['HP'] = max(self.get('HP') - dmg, 0)
            self.interface.tell(f"{self.name} is reduced to {self.get('HP')} hit points!")
        except TypeError:
            # TODO: Implement resistances and immunities
            for dmgType in dmg:
                self.take_dmg(dmg[dmgType])

    def do_action(self):
        if len(self.actions) == 0:
            self.actions.append(actions.Action("Do nothing"))
            if self.player == 'DM':
                self.actions.append(actions.CreateAttack(self))
            else:
                self.actions.append(actions.PlayerAttack(self))

        action = self.interface.DM_make_selection(self.actions, "Select an action for " + self.name)
        self.interface.tell(action())

        
    def do_help_action(self):
        print("Help action not yet implemented")

    def do_item_interaction(self):
        print("Item Interactions not yet implemented")

    def make_check(self):
        print("Ability checks not yet implemented")
        
    def give_inspiration(self):
        print("Not yet implemented")
    
    def roll_initiative(self, combat):
        self.current_initiative = d(20) + self.get("Initiative")
        self.combat = combat