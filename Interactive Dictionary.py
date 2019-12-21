# Interactive Dictionary
# Created by Charles Cromer
# Created on 12/18/2019
# Last Modified on 12/18/2019
# This is an interactive dictionary that will ask the user for a word to define
# and print out the resulting definition(s)

import json

#loads data.json file
data = json.load(open('data.json'))

# Welcome message
def welcome():
    print('\n\n\n\n\n\n\n\nInteractive Dictionary\n')
    print('This program is an interactive dictionary that will allow you to')
    print('enter a word you wish to have defined. It will then produce the')
    print('definition(s).\n\n')

def translate(word):
    return data[word]

welcome()

word = input('Enter Word: ')
print(translate(word))
