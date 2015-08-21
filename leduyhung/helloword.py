# hungld
print ''' 
-----------------------------------------
Welcome. You have to answer some question?
-----------------------------------------
'''
# asking for input
a = raw_input("How old are you?  ")
print "You've answer %d?"%(int(a)-2)
if a < 16:
	print "Get out."
else:
	print "ok. You are in."
