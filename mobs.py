from dice import *
import json

class Mob():
    def __init__(self, name, interface=None, filename=None, player_name='DM'):
        self.attributes = {}
        self.player = player_name
        self.interface = interface
        self.name = name
        self.filename = filename

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
                'attributes': self.attributes
            }))
    
    def get_attribute(self, attribute_name):
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

    def do_action(self):
        print("Actions not yet implemented")
        
    def do_help_action(self):
        print("Help action not yet implemented")

    def do_item_interaction(self):
        print("Item Interactions not yet implemented")

    def make_check(self):
        print("Ability checks not yet implemented")
        
    def give_inspiration(self):
        print("Not yet implemented")
    
    def roll_initiative(self):
        self.current_initiative = d(20) + self.get_attribute("Initiative")