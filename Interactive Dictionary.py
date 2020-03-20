# Interactive Dictionary
# Created by Charles Cromer
# Created on 12/18/2019
# Last Modified on 3/14/2020
# This is an interactive dictionary that will ask the user for a word to define
# and print out the resulting definition(s)

import json
import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database")

cursor = con.cursor()

def dBase():
    query = cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    print(results)



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
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
    results = cursor.fetchall()
    print(results)

#    data = json.load(open("data.json"))  # Loads dictionary into 'data'
#    if word.lower() in data:  # validates word is in .json file
#        definition = data[word.lower()]
#    elif word.title() in data:  # Checks for proper nouns
#        definition = data[word.title()]
#    elif word.upper() in data:  # Checks for Acronyms
#        definition = data[word.upper()]
#    elif len(get_close_matches(word.lower(), data.keys())) > 0 \
#            or len(get_close_matches(word.title(), data.keys())) > 0 \
#            or len(get_close_matches(word.upper(), data.keys())) > 0:
#        definition = similarWord(data, word)
#    else:
#        definition = "\nThe word doesn't exist. Please double check it.\n"
#    showOutput(definition)


'''
The following function similarWord() will take the user's input, see if it was entered in with a cap or not. 
It will then find the closest match that matches its case ie. Apple or apple.
If will ask the user if the word that matches the pattern and case the closest is what they intended
If not it will find the closest matching word that doesn't match case if there is one.
Example: If you enter Pariss, it will first see if you meant Paris, if not it will see if you meant piss.
'''


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
                        "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[
                            0]).upper()
                if similar == 'Y':
                    definition = data[get_close_matches(word.title(), data.keys())[0]]
                else:
                    definition = "\nThe word doesn't exist. Please double check it.\n"
        else:
            definition = "\nThe word doesn't exist. Please double check it.\n"
    elif word.istitle():
        similar = input(
            "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[0]).upper()

        while similar != 'Y' and similar != 'N':  # Validation Loop for y/n
            similar = input(
                "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.title(), data.keys())[0]).upper()

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
    elif word.isupper():
        if len(get_close_matches(word.upper(), data.keys())) > 0:
            similar = input(
                "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.upper(), data.keys())[0]).upper()
            while similar != 'Y' and similar != 'N':  # Validation Loop for y/n
                similar = input(
                    "\nDid you mean [ %s ] instead? [Y/N]" % get_close_matches(word.upper(), data.keys())[
                        0]).upper()
            if similar == 'Y':
                definition = data[get_close_matches(word.upper(), data.keys())[0]]
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
