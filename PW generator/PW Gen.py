# Get user input and return password(s) after given the users qualifications.
import random
#Establish counter for our generating loops
counter = 0
#Establish guidelines for the generating numbers
generator_floor = 34
generator_celing = 122

#See if user needs more than one password.
multiple_pass = str (input("Do you need multiple passwords? (y/n) "))

#Conditional block for Multiple password option
#Conditional statement to parse through the response
while multiple_pass != 'n' or multiple_pass != 'N' or multiple_pass != 'y' or multiple_pass != 'Y':
    #If the user needs multiple passwords, get the number of passwords that the user needs.
	if multiple_pass == 'Y' or multiple_pass == 'y':
		num_pass = int (input("How many passwords do you need? "))
		break
	#If the user doesn't need multiple passwords the variable multiple_pass can be set to one
	elif multiple_pass == 'N' or multiple_pass == 'n':
		num_pass = 1
		break
	#Any other input from the user results in this error and prompts the user to enter a valid response until the user enters y or n.
	else:
		print("Invalid response!  Please try again")
		multiple_pass = str (input("Do you need multiple passwords? (y/n) "))


#Get password length requirements.
pass_length = int (input("How long do you want the password to be? "))

#Figure out if the users password needs to include special characters.
#Return the passwords using the same conditional statement
spec_characters = str (input("Does your password require special characters? "))

#While loop that catches invalid response and continues asking until the user enters y or n.
while spec_characters != 'n' or spec_characters != 'N' or spec_characters != 'y' or spec_characters != 'Y':
	#Conditional block for special characters and password Generation
	#Conditional that runs if the user says they need special characters.
	if spec_characters == 'y' or spec_characters == 'Y':
		#Runs until the variable counter is greater than or equal to the value of the number of passwords needed
		while counter < num_pass:
			#For loop that generates a random number the number of times as the value of the requested password length
			for i in range (pass_length):
				number = random.randint(generator_floor, generator_celing)
				#Convert the generated number to a character
				character = chr(number)
				#print the character.  End keeps the curson on the same line
				print(character, end = "")
			#counter variable adds one
			counter += 1
			#Print new line
			print('\n')
		break

	#Conditional that runs if the user says they don't need special characters
	elif spec_characters == 'n' or spec_characters == 'N':
		#If no special characters are needed, we raise the generator floor by 15.
		generator_floor += 15
		#Runs until the variable counter is greater than or equal to the value of the number of passwords needed
		while counter < num_pass:
			#for loop that generates a random number the number of times as the value of the requested password length
			for j in range (pass_length):
				number = random.randint(generator_floor, generator_celing)
				#If number generated is between 58 and 64, generate a new number
				if number >= 58 and number <= 64:
					number = random.randint(65, 90)
				#If number generated is between 91 and 96 generate a new number
				elif number >= 91 and number <= 96:
					number = random.randint(97, 122)

				#Convert the generated number into a character
				character = chr(number)
				#print the character.  End keeps the cursor on the same line.
				print(character, end = "")
				#Counter variable adds one
			counter += 1
			#Print new line
			print('\n')
		break


	#Else statement that runs if the initial special characters input is anything other than y or n.
	else:
		#Prints error message and reruns the special characters prompt.
		print("Invalid response!  Please try again")
	spec_characters = str (input("Does your password require special characters? "))