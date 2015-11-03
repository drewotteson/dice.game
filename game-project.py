import time
import random

def dicerolled(dicesides):
	dice=random.randrange(dicesides) 
	return dice
 

def score(rolldice1, rolldice2):
	score=rolldice1 * rolldice2
	return score

#def rollof1(dice1, dice2):
	#if dice1 or dice2 == 1:
		#LOOP
		



print ("Let's play a game.")
time.sleep (1.0)

print ("* * * *")
print ("*      *")
print ("*      *")
print ("* * * *")
print ("*    ")
print ("*")
print ("*")
print ("*")

print ("")
time.sleep (1.0)

print ("* * *")
print ("  *")
print ("  *")
print ("  *")
print ("  *")
print ("  *")
print ("  *")
print ("* * *")

print ("")
time.sleep (1.0)

print(" * * * *")
print("*       *")
print("*       *")
print("*")
print("*   * * *")
print("*       *")
print(" * * * *")

print ("")

time.sleep (1.0)

print ("First, the rules.")
print("")
time.sleep (2.0)

print("Each player will roll two dice.")
print("__________________________________________________________________________")
print("")
time.sleep (1.0)
print("One die with numbers 1-6, One die with numbers 1-20.")
print("__________________________________________________________________________")
print("") 
time.sleep (1.0)
print("After each roll, the two numbers will be multiplied to create your score.")
print("__________________________________________________________________________")
print("")
enter=input ("Press the 'enter' key once, if understood.")

if enter=="":
	print("")
	print("You will roll repeatedly until you choose to 'hold' or if a 1 is rolled.")
	print("________________________________________________________________________")
	print("")
	time.sleep (1.0)
	print("If a 1 is rolled, your score is zero for the round & your turn is over.")

print ("")
#at a later time add a loop that sends an incorrect answer back.
#got it? type enter? dont got it? type help for a link to more details. (else)

#while game = on:
	#while turn = yes:
		#if dicerolled = 1
		#print "zero points, next players turn"


#choice=input ("Do you want to roll again or hold?")
    #if choice =="Yes"
        #turn == "No"



dice1= dicerolled(19)+1
print("dice1",dice1)
dice2= dicerolled(19)+1
print("dice2",dice2)

print(score(dice1, dice2))


















    









