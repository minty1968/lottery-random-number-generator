#!/usr/bin/env python3

import random, sys

####################################################################################################
###                                                                                              ###
###                               Main Program starts here                                       ###
###                                                                                              ###
####################################################################################################


drawType = 'National Lottery'
maxMain = 59
ballQty = 6
mainDrawNumbers = []
lottoNums = 0

# Create random lottery numbers, we are not using any analysis as yet
while lottoNums < ballQty:  # Run through from 1 to numMainBalls variable value
  numberAdded = 'No'  #  Just used to break out of while loop
  while numberAdded != 'Yes':
    randomBall = random.randint(1, maxMain)
    if randomBall not in mainDrawNumbers:
      mainDrawNumbers.append(randomBall)  #  If randomBall is not already in mainDrawNumbers then add it
      numberAdded = 'Yes'  #  If randomBall is added to mainDrawNumbers then break out of while loop, otherwise generate a new number
      lottoNums = len(mainDrawNumbers)
mainDrawNumbers.sort()   #   Sort generated numbers into numerical order

print(' ')
print(' ')
print('{} Numbers: {}'.format(drawType, mainDrawNumbers))  #  Display draw numbers to user
print(' ')
print(' ')
print(' Copyright (C) 2019  Michael Sharpe ')
print(' This program uses GNU GENERAL PUBLIC LICENSE - Version 3; ')
print(' Please see LICENSE and README.md files within this archive')
print(' ')
