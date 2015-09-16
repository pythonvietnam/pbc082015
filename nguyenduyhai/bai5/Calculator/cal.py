#Module Menu hien thi loi chao
#haind
#python

#menu hien thi
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

#module chuc nang tinh Cong (+)
#haind
#python

#tao ham phep tinh Cong
def add():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Cong (+)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num1, "+", num2, "=", num1 + num2
	print ""

#module chuc nang tinh Tru (-)
#haind
#python

#tao ham phep tinh Tru
def sub():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Tru (-)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num2, "-", num1, "=", num2 - num1
	print ""

#module chuc nang tinh Nhan (*)
#haind
#python

#tao ham phep tinh Nhan
def mul():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Nhan (*)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num1, "*", num2, "=", num1 * num2
	print ""

#module chuc nang tinh Chia (/)
#haind
#python

#tao ham phep tinh Chia
def div():
	print "Cam on ban da lua chon, ban vua chon thuc hien phep Chia (/)"
	num1 = input("So hang thu nhat: ")
	num2 = input("So hang thu hai: ")
	print "Ket qua cua phep tinh la: " 
	print num1, "/", num2, "=", num1 / num2
	print ""

