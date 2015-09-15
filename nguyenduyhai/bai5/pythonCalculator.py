#Xay dung Python Calculator, xay dung moi phep tinh bang ham
#haind
#Python

#/usr/bin/python
# coding: utf-8

def menu():
	print '''
	Chao mung ban den voi chuong trinh May tinh!

		Su dung:
		1. Cong (+)
		2. Tru (-)
		3. Nhan (*)
		4. Chia (/)
		5. Thoat chuong trinh (quit)
		'''
	return input("Moi ban lua chon: ")

def add():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Cong (+)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num1, "+", num2, "=", num1 + num2
	print ""

def sub():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Tru (-)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num2, "-", num1, "=", num2 - num1
	print ""

def mul():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Nhan (*)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num1, "*", num2, "=", num1 * num2
	print ""

def div():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Chia (/)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num1, "/", num2, "=", num1 / num2
	print ""

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
