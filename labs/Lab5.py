import random
guess = 0
goalNumber = random.randint(1,100)
print("Random number generated between 1 & 100... Try to guess it!")


while guess != goalNumber:
	try:
		guess = int(input())
		if guess > goalNumber:
			print("Your guess is too high")
		elif guess < goalNumber:
			print("Your guess is too low")
		elif guess == goalNumber:
			print("You got it right!")
	except ValueError:
		print("Try again")


