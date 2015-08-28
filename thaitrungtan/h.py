a = input("so can doan")

for i in range(11):
	b = input("nhap so ban doan")
	if b>a:
		print"so ban doan cao hon so can tim"
	elif b==a:
		print"ban da doan chinh xac"
		break
	else:
		print"so ban doan nho hon so can tim"
