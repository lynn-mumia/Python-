#Name: Lynn Mumia
#Looping practice and testing
#Exercise 2.2

#Exercise 1: loop for decimal equivalent of the number

from __future__ import division
print("A program that prints floating points between 1/2....1/10")
for p in range(2,10):
    print  (1/p)

#Exercise 2: While loop for the exercise

print ("Enter a number and I will print from it to 0")
number= input("number ?")
i=0
while(i>=0 and i<=number):
    print i
    i=i+1

#Exercise 3: For loop that calculates exponentials
print ("This progrsm claculates the exponential."+
       "Enter the base and exponent as below")

base =input("Base ?")
exp = input("Exponent ?")
exponential= base**exp
print exponential

#Exercise 4: While loop for numbers divisible by two
print ("Enter a number divisible by 2")
divide=input("number ?")
while(divide%2!=0):
    print ("Oops! Not divisble by 2")
    print ("Enter a new number")
    divide =input("number ?")

print ('Congratulations. You finally got it '+
       str(divide) + ' is divisible by 2')
    
