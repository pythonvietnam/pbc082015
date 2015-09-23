#loitd
#python

l=list()
beginw = "chatmsg:"

for i in range(5):
	s = raw_input("Hay nhap chuoi")
	if s == 'q':
		print l
		break
	elif s.startswith(beginw):
		l.append(s)


		