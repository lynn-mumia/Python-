# Name:Lynn Mumia
# Section: 2
# homework_2.py

##### Template for Homework 2, exercises 3.1-3.4  ######
import math
import random

# **********  Exercise 3.1 ********** 

# Define your rock paper scissors function here
##### YOUR CODE HERE #####
def rps(player1,player2):    
    if (player1 == 'rock' and player2 == 'scissors'):
        print 'Player 1 wins.'
    elif(player1 == 'paper' and player2 == 'scissors'):
        print 'Player 2 wins.'
    elif(player1 == 'rock' and player2 == 'paper'):
        print 'Player 2 wins.'
    elif(player1 == 'scissors' and player2 == 'rock'):
        print 'Player 2 wins.'
    elif(player1 == 'scissors' and player2 == 'paper'):
        print 'Player 1 wins.'
    elif(player1 == 'paper' and player2 == 'rock'):
        print 'Player 1 wins.'
    elif(player1 == 'rock' and player2 == 'rock'):
        print 'Tie.'
    elif(player1 == 'paper' and player2 == 'paper'):
        print 'Tie.'
    elif(player1 == 'scissors' and player2 == 'scissors'):
        print 'Tie.'
    else:
        print 'This is not a valid object selection'

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####
rps("rock","rock")
rps("paper","scissors")
rps("scissors","rock")

# *********** Exercise 3.2 ***********
## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
    return a*b+c
## 2 - Equations

angle_test = math.sin(math.pi/4)+((math.cos(math.pi/4))/2)
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = math.ceil(276/19)+ 2*math.log(12,7)
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(n):
   return (n * math.pow(math.e,-n))+ (math.sqrt(1-math.pow(math.e,-n)))

# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 3.3 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    myint= random.randint(0, 100)
    print myint
    if(myint%3 ==0):
        return True
    else:
        return False

# Test Cases
##### YOUR CODE HERE #####
rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(sides,roll_number):
    i=1
    while(i<=roll_number):
         print random.randint(0, 6)
         i=i+1
    print "Thats all!"

# Test Cases
##### YOUR CODE HERE #####                            
roll_dice(6,3)
