#python
#loitd
#pythonvietnam
#bai 02 - input

print '''
----------------------------------------------
welcome. You have to answer some questions.
----------------------------------------------'''

#asking for input
age = input("how old are you?")
print "You've answer %d?"%(age+1)

#conditional
if age < 16:
	print "Please goto somewhere for children."
else:
	print "ok. You are in."