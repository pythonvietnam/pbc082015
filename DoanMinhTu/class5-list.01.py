import sys
import os


round_number = 1
halt_token = False
numberList = []

while halt_token == False:
		
##################################################################################################
	check_token = False
	while check_token == False:
		number_input = raw_input("Input the  number: ")
		
		if number_input == 'q' or number_input == 'Q':
			print '\nReceived exit signal - Exiting \n'
			sys.exit()
			
		try: 
			number 	= int(number_input)
			check_token = True
		except:
			check_token = False
		
		if 	check_token == False:
			print 'Wrong input!! TRY AGAIN!\n'
		else:
			print "Record input number: %d"%number
			
##################################################################################################
	numberList.append(number)
	
##################################################################################################
	check_token = False
	while check_token 	== False:
		continue_input 	= raw_input("Continue ?(Y/N)")
		if continue_input == 'Y' or continue_input == 'y':
			round_number 	+= 1
			halt_token 		= False
			check_token     = True
			print "\nContinue to round %d"%round_number
		elif continue_input == 'N' or continue_input == 'n':
			halt_token 		= True
			check_token     = True
			print '\nUser chose to stop after round %d \n'%round_number
		elif continue_input == 'q' or continue_input == 'Q':
			print '\nReceived exit signal - Exiting \n'
			sys.exit()
		else:
			check_token 	= False
			print "\nWrong input, please input Y or N!!\n"
		
##################################################################################################


avegrage_value = float(sum(numberList))/len(numberList)
print 'The recorded list is'
print numberList
print 'The sum is: %d'%sum(numberList)
print 'The length of list is: %d'%len(numberList)
print 'The avegrage value is :%f'%avegrage_value

