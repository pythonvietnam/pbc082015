print '''------
Welcome to program
A. Usage
	1. Cong
	2. Tru
	3. Nhan
	4. Chia
-------'''

choice = raw_input("Please input your choice? (1/2/3/4)")
x = int(raw_input("Nhap toan hang X: "))
y = int(raw_input("Nhap toan hang Y: "))

result = {'1': Lambda x,y: x+y, '2': Lambda x,y: x-y, '99': Lambda x,y: x*y}[choice](x,y)

