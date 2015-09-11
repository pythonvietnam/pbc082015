##

import sys

a = 4
while 1:
	b =	raw_input("So cua toi doan la:")
	#print "Kieu %s", type(b)

	if b == 'q':
			print "thoat"
			exit(1)
	if b == 'Q':
			print "thoat"
			break
	if a!= int(b):
		print "ban doan sai"
	elif a == int(b):
		print"ban da doan dung"
		break
