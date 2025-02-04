# Interactive Dictionary
# Created by Charles Cromer
# Created on 12/18/2019
# Last Modified on 8/04/2020

import mysql.connector

con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database")

cursor = con.cursor()


def main():
    welcome()
    runAgain = 'Y'  # Sets flag for "Run Again?" loop
    while runAgain.upper() == 'Y':  # Run Again loop
        getInput()
        runAgain = input('\nWould you like to define another word?  [Y/N]\n')
    print('Thank you for using the interactive dictionary!')


def getInput():
    word = input('Enter Word: ')
    while not word.isalpha() or word == '':  # Validates user input
        word = input('Error, Please enter a word: ')
    translate(word)


def welcome():
    print('\n\n\n\n\n\n\n\nInteractive Dictionary\n')
    print('This program is an interactive dictionary that will allow you to')
    print('enter a word you wish to have defined. It will then produce the')
    print('definition(s).\n\n')


def translate(word):
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
    results = cursor.fetchall()
    if len(results) > 0: # Checks to make sure some result came back
        showOutput(results)
    else:
        print('I am sorry, no such word as [ {} ]'.format(word))

def showOutput(definition):
    for num in range(len(definition)): # Cycles through each definition
        print(str(num+1)+':', definition[num][1])


main()
