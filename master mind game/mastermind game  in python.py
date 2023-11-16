#start
print (" - MASTERMIND -\n")
player_name=input("Please Enter Your Name:-\n")
print("Hii " + player_name, "Welcome To Game Int")

import random
print ("Please Enter The four digit Number.\nYou Can go with 1-White ,2-Blue, 3-Red, 4-Yellow, 5-Green, 6-Purple")

colured_numbers = ["1", "2", "3", "4", "5", "6"]
chances = 0
game = True

# using random library  computer for automettically choose number
color_code = random.sample(colured_numbers,4)	

# player guesses the number	
while game:
	true_colour = ""
	choosed_colour = ""
	player_choice = input("\n Please Enter 4 digit numbers from the given list [1, 2, 3, 4, 5, 6]").upper()

	if '0000' in player_choice :
		print("\n      Thanks for Playing, See You Soon",player_name," ;) ")
		quit()
	chances += 1
	
	# checking if player's input is correct
	if len(player_choice) != len(color_code):
		print ("\nThe Secret Code is  Four Digit, Please Try Again!")
		continue
	for i in range(4):
		if player_choice[i] not in colured_numbers:
			print ("\nInvalid Number, "+ player_choice[i]+" is not valid "+" Please Enter A Valid Number.")
			break
		    
	# connection between colour code vs player choice
	if true_colour != "1111":
		for i in range(4):
			if player_choice[i] == color_code[i]:
				true_colour += "1"
			if  player_choice[i] != color_code[i] and player_choice[i] in color_code:
				choosed_colour += "0"
		print (true_colour +  choosed_colour + "\n")		
		
	if true_colour == "1111":
		if chances == 1:
			print ("Nice work you guess the answer with in first chance")
		else:
			print ("perfect.. You  have only " + str(chances) + " chances to guess.")
		game = False
		
	if chances >= 1 and chances <8 and true_colour != "1111":
		print ("You have " + str(8-chances) + " chances to  left. Next attempt: ")
	elif chances >= 8:
		print("GAME OVER")
		print ("You didn't guess. The secret color code was: " + str(color_code))
		game=False;
		

	# play or not to play
	
	while game == False:
		finish_game = input("\nDo you want to play another game (Yes/No)?").upper()	
		chances = 0
		if finish_game =="No":
			print  ("Thankyou")
			quit()
		elif finish_game == "Yes":
			game = True
			print ("So, let's play again... Guess the secret code: ")

#end