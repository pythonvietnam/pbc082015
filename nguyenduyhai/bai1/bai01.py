print '''
-------------------------------------------------
welcome. you have to answer some question.
-------------------------------------------------'''

age = raw_input('how old are you?')
print "you've answer %d?"%(int(age)+1)

if age < 16:
	print "please goto somewhere for children."
else:
	print "ok.you are in."