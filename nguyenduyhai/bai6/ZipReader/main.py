#Chuong trinh chinh Python Zip Reader!
#haind
#python

import zipreader

#thuc hien vong lap chuong trinh
vonglap = 1
choice = 0
while vonglap == 1:
	choice = zipreader.menu()
	if choice == 1:
		zipreader.nenZip(raw_input("Hay nhap ten file nen Zip: "), raw_input("Hay nhap file can nen: "))
	elif choice == 2:
		zipreader.giainenZip(raw_input("Hay nhap file can giai nen: "))
	elif choice == 3:
		vonglap = 0

print "Cam on ban da su dung chuong trinh"
