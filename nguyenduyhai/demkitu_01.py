#Thuc hien dem so ky tu a,b,c trong chuoi do nguoi dung nhap vao va cho phep an Q de quit

A = input('Moi ban doan A:')

while 1:
	print "Moi ban nhap so binh phuong cua A hoac Q de quit:"
	B = raw_input()

	if B == 'q' or 'Q':
		break
	elif B != 'q' or 'Q':
		C = int(B)
		C = pow(A,2)
		if C > 0:
			if C < B:
				print "Ban phai doan nho hon"
			elif C == B:
				print "Ban da doan chinh xac"
				break
			else:
				print "Ban phai doan lon hon"
		else: 
			print "Hay doan lai mot so khac:"
