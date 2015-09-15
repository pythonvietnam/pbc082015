#Xay dung Python Calculator, xay dung moi phep tinh bang ham
#haind
#Python

def menu():
	print '''Chao mung ban den voi May tinh Python!

		Su dung:
		1. Cong (+)
		2. Tru (-)
		3. Nhan (*)
		4. Chia (/)
		5. Thoat chuong trinh (quit)'''
	return input("Moi ban lua chon: ")

def add(num1,num2):
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Cong (+)"
	print "Ket qua cua phep tinh la: " 
	print num1, "+", num2, "=", num1 + num2

def sub(num1,num2):
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Tru (-)"
	print "Ket qua cua phep tinh la: " 
	print num2, "-", num1, "=", num2 - num1

def mul():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Nhan (*)"

def div():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Chia (/)"

vonglap = 1
choice = 0
while vonglap == 1:
	choice = menu()
	if choice == 1:
		add(input("So hang thu nhat: "),input("So hang thu hai: "))
	elif choice == 2:
		sub()
	elif choice == 3:
		mul()
	elif choice == 4:
		div()
	elif choice == 5:
		vonglap = 0

print "Cam on ban da su dung chuong trinh."
