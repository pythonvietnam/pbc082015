#Viet chuong trinh doc chuoi nhap vao tu nguoi dung va chi xu ly 
#in ra nhung chuoi nao bat dau voi tu "chatmsg:", thoat chuong trinh bang phim "q"
#haind

l = list()
begin = "chatmsg: "

for i in range(5):
	s = raw_input("Hay nhap chuoi: ")
	if s == 'q':
		print l
		break
	elif s.startswith(begin):
		l.append(s)

