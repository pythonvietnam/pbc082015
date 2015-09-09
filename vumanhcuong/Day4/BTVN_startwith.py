#Bai tap startwith
print "========Bai tap startwith======="

while 1:
	str = raw_input ("Nhap vao chuoi:")
	if str == 'q' or str == 'Q':
		break
	elif str.startswith("chatmsg"):
		print str
	else:
		print "====Nhap lai====="