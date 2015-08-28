import sys
import random

	

halt_token = False
round_number = 1
		
print'''Calculator program
	Use the following operator : 
		/: divide
		*: multiply
		+: addition
		-: subtract
	'''
print '\n'
	
	
while halt_token == False:
		
	print '\t\t\t Starting round %d'%round_number
		
##############################################################
	check_token = False
	while check_token == False:
		operator_input = raw_input("Input the operator: ")

		if operator_input == '/' or operator_input == '*' or operator_input == '+' or operator_input == '-': 
			check_token = True
			print "Record input operator:%s"%operator_input
		elif operator_input == 'q' or operator_input == 'Q':
			print '\nReceived exit signal - Exiting \n'
			sys.exit()
		else:
			print 'Wrong input!! TRY AGAIN!\n'
		
		
##############################################################
	check_token = False
	while check_token == False:
		number1_input = raw_input("Input the  number1: ")
		
		try: 
			number1 	= int(number1_input)
			check_token =  True
		except:
			check_token = False
		
		if check_token 	== False:
			if number1_input == 'q' or number1_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Wrong input!! TRY AGAIN!\n'
		else:
			print "Record input number1:%d"%number1

			
##############################################################
	check_token = False
	while check_token == False:
		number2_input = raw_input("Input the number2: ")
		
		try: 
			number2 	= int(number2_input)
			check_token	=  True
		except:
			check_token = False
		
		if check_token 	== False:
			if number2_input == 'q' or number2_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Wrong input!! TRY AGAIN!\n'
		else:
			print "Record input number2:%d"%number2


		#Calculation
##############################################################
	if operator_input == '/':
		result = number1/number2
	elif operator_input == '*':
		result = number1*number2
	elif operator_input == '+':
		result = number1+number2
	elif operator_input == '-':
		result = number1-number2
		
	print 'Result is:' + str(result)
		
##############################################################
	continue_input = raw_input("Continue ?(Y/N)")
	if continue_input == 'Y' or continue_input == 'y':
		round_number 	+= 1
		halt_token 		= False
		print "Continue to round %d\n"%round_number
	elif continue_input == 'N' or continue_input == 'n':
		halt_token = True
		print '\nUser chose to stop after round %d \n'%round_number
	elif continue_input == 'q' or continue_input == 'Q':
		print '\nReceived exit signal - Exiting \n'
		sys.exit()
	else:
		print "\nWrong input, please input Y or N!!\n"
##############################################################
	
