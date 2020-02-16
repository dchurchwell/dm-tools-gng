import random
import re

def d(n, skill=0, adv=0):
    if adv != 0:
        print("Advantage not implemented")
    return random.randint(1, n) + skill

def roll(string, crit=False):
    """Roll a string of dice
    
    Arguments:
        string {string} -- Standard format of dice string, e.g. 8d6+10, 4d4-1, 2d6+2d8+5
    
    Returns:
        int -- The result of the dice
        If damage types (such as lightning) are included, it will return a dictionary instead.
    """    

    if string == '':
        return 0
    if type(string) == int:
        return string

    total = 0
    string = string.replace(' ', '')
    string = string.replace(',', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.lower()

    damage_types = '|'.join(['acid',
                    'bludgeoning',
                    'cold',
                    'fire',
                    'force',
                    'lightning',
                    'necrotic',
                    'piercing',
                    'poison',
                    'psychic',
                    'radiant',
                    'slashing',
                    'thunder'])

    try:
        # Resolve different damage types, resulting in a dictionary instead of an int
        type_dict = {}
        # Split on damage type keywords
        split = re.split('(' + damage_types + ')', string)
        if len(split) > 1:
            # Loop through damage types
            for i in range(len(split)):
                if i % 2 == 0 and i < len(split)-1:
                    type_dict[split[i+1]] = roll(split[i], crit)
            return type_dict


        elif '+' in string:
            for die in string.split('+'):
                total += roll(die, crit)
        elif '-' in string:
            total += roll(string.split('-')[0], crit)
            for die in string.split('-')[1:]:
                total -= roll(die, crit)
        elif 'd' in string:
            num, die = string.split('d')
            die = int(die)
            for i in range(int(num)):
                total += d(die)
                if crit:
                    total += d(die)
        else:
            total += int(string)
    except Exception as e:
        print(e)
        print("Invalid string:", string)
        return 0

    return total