# RockPaperScissors


This is a simple rock paper and scissors game. 


You play against a machine until the point difference is of four or more


## How does the machine choose an option? (rock,paper or scissors?)

The computer generates a random number between 0 and 1.

If the number is:

* Lower than 1/8 -> rock
* Lower than 1/4 **and** higher than 1/8 -> paper
* Lower than 3/8 **and** higher than 1/4 -> scissors
* Higher than 3/8 an algorithm kicks in.

### How does the algorithm work? 


The algorithm gives rock paper and scissors a value.

It always chooses the one with the lowest value.
All options start with the same value (-9999)

If the computer wins the value of option that it won with decreases (this makes it **more likely** that it will be chosen again)

If the computer loses the value of the option that it lost with increases (this makes it **less likely** that it will be chosen again)

## UPDATE V1.1

Made it so you cn play various rounds and choose the point difference you play to
