#chuong trinh Quan ly Hoc Sinh
#su dung modules
#haind
#python

from Packages import mol
ds = list()

#thuc hien vong lap chuong trinh
vonglap = 1
choice = 0
while vonglap == 1:
	choice = mol.menu()
	if choice == 1:
		mol.themHS()
	elif choice == 2:
		mol.timHS()
	elif choice == 3:
		vonglap = 0

print "Cam on ban da su dung chuong trinh"

