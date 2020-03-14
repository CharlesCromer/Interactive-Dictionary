# Interactive Dictionary
# Created by Charles Cromer
# Created on 12/18/2019
# Last Modified on 12/18/2019
# This is an interactive dictionary that will ask the user for a word to define
# and print out the resulting definition(s)

import json

def main():
    welcome()
    runAgain = 'Y'  #Sets flag for "Run Again?" loop
    while runAgain.upper() == 'Y':  #Run Again loop
        word = input('Enter Word: ')
        print(translate(word))
        runAgain = input('\nWould you like to define another word?  [Y/N]\n' )
    print('Thank you for using the interactive dictionary!')


# Welcome message
def welcome():
    print('\n\n\n\n\n\n\n\nInteractive Dictionary\n')
    print('This program is an interactive dictionary that will allow you to')
    print('enter a word you wish to have defined. It will then produce the')
    print('definition(s).\n\n')

def translate(word):
    data = json.load(open("data.json"))     # Loads dictionary into 'data'
    word = word.lower()
    if word in data:    #validates word is in .json file
        return data[word]
    else:
        return "\nThe word doesn't exist. Please double check it."


main()

