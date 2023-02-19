# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Thomas Eagle
# Creation Date: 2/12/2023
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
   # Indention of While statement prevents it from triggering
   #     while cave != '1' and cave != '2':
   #        print('Which cave will you go into? (1 or 2)')
   #         cave = input()
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    #should return cave not caves
    #return caves
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #need paranthesis around the string statement to print  
        #print 'Gobbles you down in one bite!'
        print('Gobbles you down in one bite!')


displayIntro()
#choosecave should be correctly cased to chooseCave()
#caveNumber = choosecave()
caveNumber = chooseCave()
checkCave(caveNumber)
    
print("Thanks for planing")