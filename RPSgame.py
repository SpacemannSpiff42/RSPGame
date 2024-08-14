import random, sys

#variables
wins = 0
losses = 0
ties = 0



print('Lets play rock, paper, scissors!')
while True:
	print(wins,"Wins, ",losses," Losses, ", ties,"Ties")
	print('Enter you move: (r)ock, (p)aper, (s)cissors or (q)uit')
	playermove = input()
	if playermove == "q":
		sys.exit()
	else:
		computermove = random.randint(1,3)
		if computermove == 1:
			computermove = 'r'
		elif computermove ==2:
			computermove = 'p'
		elif computermove == 3:
			computermove = 's'
		print("The computer picked ",computermove)
		if playermove == computermove:
			#print("Rock Versus Rock")
			print("It's a tie")
			ties += 1
		elif playermove == "r" and computermove == 'p':
			print("Rock Versus Paper")
			print("You lose")
			losses +=1
		elif playermove == "r" and computermove == 's':
			print("Rock Versus Scissors")
			print("You win")
			wins +=1
		elif playermove == "p" and computermove == 'r':
			print("Paper Versus Rock")
			print("You win")
			wins +=1
		elif playermove == "p" and computermove == 's':
			print("Paper Versus Scissors")
			print("You lose")
			losses +=1
		elif playermove == "s" and computermove == 'r':
			print("Scissors Versus Rock")
			print("You lose")
			losses +=1
		elif playermove == "s" and computermove == 'p':
			print("Scissors Versus Paper")
			print("You win")
			wins +=1
		#print(wins,"Wins, ",losses," Losses, ", ties,"Ties")