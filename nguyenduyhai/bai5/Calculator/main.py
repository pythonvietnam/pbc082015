#Chuong trinh Python Calculator
#Su dung cac Module, Function
#haind
#Python

from Modules import menu
menu.menu()

from Modules import cong 
cong.add()

from Modules import tru 
tru.sub()

from Modules import nhan
nhan.mul()

from Modules import chia
chia.div()

#vong lap lua chon chuong trinh
vonglap = 1
choice = 0
while vonglap == 1:
	choice = menu()
	if choice == 1:
		add()
	elif choice == 2:
		sub()
	elif choice == 3:
		mul()
	elif choice == 4:
		div()
	elif choice == 5:
		vonglap = 0

print "Cam on ban da su dung chuong trinh."
