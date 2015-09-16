#chuong trinh Quan ly Hoc Sinh
#su dung modules
#haind
#python

from Modules import menu
menu.menu()

from Modules import themHS
themHS.themHS()

from Modules import timHS
timHS.timHS()

#thuc hien vong lap chuong trinh
vonglap = 1
choice = 0
while vonglap == 1:
	choice = menu()
	if choice == 1:
		themHS()
	elif choice == 2:
		timHS()
	elif choice == 3:
		vonglap = 0

print "Cam on ban da su dung chuong trinh"

