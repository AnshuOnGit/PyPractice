__author__ = 'anshu'

import random

def get_state_capital(state):
    with open('StatesAndCapitals.txt','r') as f:
        line = f.readline()
        while line != '':
            line = f.readline()
            if line.upper().find(state.upper()) >0:
                values = line.split(':')
                return values[1].strip()
    return "State not Found"

def get_random_state():
    states = []
    with open('StatesAndCapitals.txt','r') as f:
        lines = f.readlines()
    for i in lines:
        states.append(i.split(':')[0].rstrip('\t ').lstrip('0123456789\t '))
    return random.choice(states)


if __name__ == '__main__':
    print 'Capital of Bihar is: '+ get_state_capital('bihar')
    print get_random_state()