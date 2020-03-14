# Interactive Dictionary
# Created by Charles Cromer
# Created on 12/18/2019
# Last Modified on 3/14/2020
# This is an interactive dictionary that will ask the user for a word to define
# and print out the resulting definition(s)

import json
from difflib import get_close_matches


def main():
    welcome()
    runAgain = 'Y'  # Sets flag for "Run Again?" loop
    while runAgain.upper() == 'Y':  # Run Again loop
        getInput()
        runAgain = input('\nWould you like to define another word?  [Y/N]\n')
    print('Thank you for using the interactive dictionary!')


def getInput():
    word = input('Enter Word: ')
    while not word.isalpha() or word == '':
        word = input('Error, Please enter a word: ')
    translate(word)


# Welcome message
def welcome():
    print('\n\n\n\n\n\n\n\nInteractive Dictionary\n')
    print('This program is an interactive dictionary that will allow you to')
    print('enter a word you wish to have defined. It will then produce the')
    print('definition(s).\n\n')


def translate(word):
    data = json.load(open("data.json"))  # Loads dictionary into 'data'
    if word.lower() in data:  # validates word is in .json file
        definition = data[word]
    elif word.title() in data:  # Checks for proper nouns
        definition = data[word.title()]
    elif len(get_close_matches(word.lower(), data.keys())) > 0 or len(get_close_matches(word.title(), data.keys())) > 0:
        definition = similarWord(data, word)
    else:
        definition = "\nThe word doesn't exist. Please double check it.\n"
    showOutput(definition)

def similarWord(data, word):
    if word.islower():
        similar = input("\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word, data.keys())[0]).upper()

        while similar != 'Y' and similar != 'N':  # Validation Loop for y/n
            similar = input("\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word, data.keys())[0]).upper()

        if similar == 'Y':
            definition = data[get_close_matches(word, data.keys())[0]]
        elif similar == 'N':
            if len(get_close_matches(word.title(), data.keys())) > 0:
                similar = input(
                    "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[0]).upper()
                while similar != 'Y' and similar != 'N':  # Validation Loop for y/n
                    similar = input(
                        "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[0]).upper()
                if similar == 'Y':
                    definition = data[get_close_matches(word.title(), data.keys())[0]]
                else:
                    definition = "\nThe word doesn't exist. Please double check it.\n"
        else:
            definition = "\nThe word doesn't exist. Please double check it.\n"
    elif word.istitle():
        similar = input("\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[0]).upper()

        while similar != 'Y' and similar != 'N':  # Validation Loop for y/n
            similar = input("\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[0]).upper()

        if similar == 'Y':
            definition = data[get_close_matches(word.title(), data.keys())[0]]
        elif similar == 'N':
            if len(get_close_matches(word.lower(), data.keys())) > 0:
                similar = input(
                    "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.lower(), data.keys())[0]).upper()
                while similar != 'Y' and similar != 'N':  # Validation Loop for y/n
                    similar = input(
                        "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.lower(), data.keys())[
                            0]).upper()
                if similar == 'Y':
                    definition = data[get_close_matches(word.lower(), data.keys())[0]]
                else:
                    definition = "\nThe word doesn't exist. Please double check it.\n"
        else:
            definition = "\nThe word doesn't exist. Please double check it.\n"
    return definition


def showOutput(definition):
    linenum = 1
    if type(definition) == list:
        for item in definition:
            print(str(linenum) + ':', item)
            linenum += 1
    else:
        print(definition)


main()
