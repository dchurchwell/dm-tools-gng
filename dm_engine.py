import csv
import mobs

class Interface():
    def tell(self, msg):
        self.tell_DM(msg)

    def tell_DM(self, msg):
        print(msg)

    def tell_PCs(self):
        print("Not yet implemented")

    def ask_DM(self, msg=""):
        return input(msg)

    def ask_PCs(self):
        print("Not yet implemented")

    def update_turn(self):
        print("Not yet implemented")

    def update_actions_options(self):
        print("Not yet implemented")

    def update_action_suboptions(self):
        print("Not yet implemented")

    def DM_make_selection(self, items, text=''):
        print(text)
        for i, item in enumerate(items):
            if type(item) == type(""): 
                print(f"[{i}]: {item}")
            else:
                print(f"[{i}]: {item.text}")
        selection = int(input('Make a selection: '))
        return items[selection]