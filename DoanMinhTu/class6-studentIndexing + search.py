# -*- coding: UTF-8 -*-
import sys
import os


round_number = 0
halt_token = False
StudentX = {'NAME':'None','BIRTHDAY':'None','SEX':'None','ADDRESS':'None','HOMETOWN':'None','CLASS':'None'}
student_catalogue = {}

while halt_token == False:
	check_token = False
	
	while check_token 		== False:
		continue_input 		= raw_input("Continue ?(Y/N) (input S to search)")
		
		
		if continue_input 	== 'Y' or continue_input == 'y':
			round_number 	+= 1
			print "\nGetting info of student No. %d"%round_number
			
###########################################################################################
			name_input = raw_input ('Input any name here (q or Q to quit): ')
			if name_input == 'q' or name_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Recorded name: ' + name_input
			
###########################################################################################
			check_token = False
			while check_token == False:
				DayOfB_input = raw_input("Input the DayOfB of birth: ")
				
				try: 
					DayOfB 	= int(DayOfB_input)
					check_token = True
				except:
					check_token = False
				
				if 	check_token == False:
					if DayOfB_input == 'q' or DayOfB_input == 'Q':
						print '\nReceived exit signal - Exiting \n'
						sys.exit()
					else:
						print 'Wrong input!! TRY AGAIN!\n'
				else:
					print "Record DayOfB of birth: %d"%DayOfB

###########################################################################################
			check_token = False
			while check_token == False:
				MonthOfB_input = raw_input("Input the MonthOfB of birth: ")
				
				try: 
					MonthOfB 	= int(MonthOfB_input)
					check_token = True
				except:
					check_token = False
				
				if 	check_token == False:
					if MonthOfB_input == 'q' or MonthOfB_input == 'Q':
						print '\nReceived exit signal - Exiting \n'
						sys.exit()
					else:
						print 'Wrong input!! TRY AGAIN!\n'
				else:
					print "Record MonthOfB of birth: %d"%MonthOfB

###########################################################################################
			check_token = False
			while check_token == False:
				YearOfB_input = raw_input("Input the YearOfB of birth: ")
				
				try: 
					YearOfB 	= int(YearOfB_input)
					check_token = True
				except:
					check_token = False
				
				if 	check_token == False:
					if YearOfB_input == 'q' or YearOfB_input == 'Q':
						print '\nReceived exit signal - Exiting \n'
						sys.exit()
					else:
						print 'Wrong input!! TRY AGAIN!\n'
				else:
					print "Record YearOfB of birth: %d"%YearOfB
				
###########################################################################################
			address_input = raw_input ('Input any address here (q or Q to quit): ')
			if address_input == 'q' or address_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Recorded address: ' + address_input

###########################################################################################
			sex_input = raw_input ('Input any sex here (q or Q to quit): ')
			if sex_input == 'q' or sex_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Recorded sex: ' + sex_input
			
###########################################################################################
			class_input = raw_input ('Input any class here (q or Q to quit): ')
			if class_input == 'q' or class_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Recorded class: ' + class_input 
			
###########################################################################################
			hometown_input = raw_input ('Input any hometown here (q or Q to quit): ')
			if hometown_input == 'q' or hometown_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Recorded hometown: ' + hometown_input 

###########################################################################################
		
			StudentX['NAME'] = name_input
			StudentX['BIRTHDAY'] = DayOfB_input + '/' + MonthOfB_input + '/' + YearOfB_input
			StudentX['ADDRESS'] = address_input
			StudentX['SEX'] = sex_input
			StudentX['CLASS'] = class_input
			StudentX['HOMETOWN'] = hometown_input
			
			name_element =  name_input.split()
			StudentX_ID = '_'.join(name_element)
			StudentX_ID = StudentX_ID + '_' + str(round_number)
			student_catalogue [StudentX_ID] = StudentX
			
			halt_token 		= False
			check_token     = True
			
###########################################################################################
			
		elif continue_input == 's' or continue_input == 'S':
			halt_token 		= False
			check_token     = True
			
			search_input = raw_input ('Input any search here (q or Q to quit): ')
			if search_input == 'q' or search_input == 'Q':
				print '\nReceived exit signal - Exiting \n'
				sys.exit()
			else:
				print 'Recorded searching for: ' + search_input
			
			
			search_element =  search_input.split()
			search_ID = '_'.join(search_element)
			search_result = {}
			
			for StudentX_ID in student_catalogue:
				if StudentX_ID.startswith(search_ID):
					search_token = True
					search_result [StudentX_ID] = student_catalogue[StudentX_ID]
					
					
			if len(search_result) == 0:
				print 'No studen with such name'
			else:
				for StudentX_ID in search_result:
					print '\t\tstuden ID: ' + StudentX_ID
					for StudentX_Info in search_result[StudentX_ID]:
						print StudentX_Info + ':' + (search_result[StudentX_ID])[StudentX_Info]
			
		elif continue_input == 'N' or continue_input == 'n':
			halt_token 		= True
			check_token     = True
			print '\nUser chose to stop after round %d \n'%round_number
			
		elif continue_input == 'q' or continue_input == 'Q':
			print '\nReceived exit signal - Exiting \n'
			sys.exit()
			
		else:
			check_token 	= False
			print "\nWrong input, please input Y or N or S!!\n"
			
			


			

#for StudentX_ID in student_catalogue:
#	print '\t\tstuden ID: ' + StudentX_ID
#	for StudentX_Info in student_catalogue[StudentX_ID]:
#		StudentX = student_catalogue[StudentX_ID]
#		#print StudentX_Info + ':' + StudentX[StudentX_Info]
#		print StudentX_Info + ':' + (student_catalogue[StudentX_ID])[StudentX_Info]	
		
		


