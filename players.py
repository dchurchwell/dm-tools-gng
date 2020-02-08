from mobs import *
import csv

class Player(Mob):
    def make_check():
        print("Not yet implemented")


def load_player_data(self, filename='players.txt'):
    players = []
    # Get player data from files
    with open(filename) as playerfile:
        reader = csv.reader(playerfile)
        for row in reader:
            players.append(Mob(row[0], filename=row[1], player_name=row[2]))
    return players