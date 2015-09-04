x=int(raw_input("hay nhap so:"))
while 1:
	a= x*x
	b=raw_input("ban hay doan hoac nhap 'q' de thoat: ")
	if b=='Q' or 'q':
		print"quit"
		break
	c=int(b)
	if c>a:
		print "ban hay nhap so lon hon"
	elif c==a:
		print "ban nhap dung"
		break
	else:
		print "ban da nhap sai"
	