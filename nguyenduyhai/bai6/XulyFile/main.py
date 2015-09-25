#Chuong trinh chinh Xu ly file
#haind
#python

import xulyfile

#vong lap lua chon chuong trinh
vonglap = 1
choice = 0
while vonglap == 1:
	choice = xulyfile.menu()
	if choice == 1:
		xulyfile.creatFile()
	elif choice == 2:
		xulyfile.creatCSV()
	elif choice == 3:
		xulyfile.creatZIP()
	elif choice == 4:
		vonglap = 0

print "Cam on ban da su dung chuong trinh."
