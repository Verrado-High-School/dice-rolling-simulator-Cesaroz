# Cesar Ortalejo:
# Period 2
# Dice Rolling Simulator

import random 

diceroll = int(input("How many times will you roll the dice? \n"))
yeehaw = 1

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

while yeehaw <= diceroll :
	print("Your number is " + str(random.randint(1, 6)))
	boi = random.randint(1,6)
	yeehaw = yeehaw + 1


	if yeehaw >= diceroll + 1:
		break

	if boi == 1:
		num1 = num1 + 1
	if boi == 2:
		num2 = num2 + 1
	if boi == 3:
		num3 = num3 + 1
	if boi == 4:
		num4 = num4 + 1
	if boi == 5:
		num5 = num5 + 1
	if boi == 6:
		num6 = num6 + 1

print("The number of 1's are " + str(num1))
print("The number of 2's are " + str(num2))
print("The number of 3's are " + str(num3))
print("The number of 4's are " + str(num4))
print("The number of 5's are " + str(num5))
print("The number of 6's are " + str(num6))


p1 = (num1 / diceroll) * 100
print("The percent of 1 is " + str(p1))
p2 = (num2 / diceroll) * 100
print("The percent of 2 is " + str(p2))
p3 = (num3 / diceroll) * 100
print("The percent of 3 is " + str(p3))
p4 = (num4 / diceroll) * 100
print("The percent of 4 is " + str(p4))
p5 = (num5 / diceroll) * 100
print("The percent of 5 is " + str(p5))
p6 = (num6 / diceroll) * 100
print("The percent of 6 is " + str(p6))




