##bai1

print '''
================================================
Welcome ,you have to answer some question.
================================================
'''

#ask for input
age = input ("Ban bao nhieu tuoi?")
#age = int(age)
print "Tuoi cua toi la %d?" %(age+12)
age = age+12


#conditional
if age < 16:
	print "khong du tuoi"
else:
	print "ok"