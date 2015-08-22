##bai1

print '''
================================================
Welcome ,you have to answer some question.
================================================
'''

#ask for input
age = raw_input ("Ban bao nhieu tuoi?")
print "Tuoi cua toi la %s?" %(age+10005*2)


#conditional
if age < 16:
	print "khong du tuoi"
else:
	print "ok"