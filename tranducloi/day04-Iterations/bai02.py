#python
#loitd
#demo switch with dictionary

print '''------
Welcome to program
A. Usage
    1. Cong
    2. Tru
    3. Nhan
    4. Chia
------'''

#switch with dictionary
choice = raw_input("Please input your choice? ")
x = int(raw_input("Nhap toan hang X: "))
y = int(raw_input("Nhap toan hang Y: "))

#without default value
result={
	'1':lambda x,y: x+y, 
	'2':lambda x,y: x-y, 
	'99':lambda x,y: x+y}[choice](x,y)

#switch with dictionary with default value
result={'1':lambda x,y: x+y, '2':lambda x,y: x-y}.get(choice,lambda x,y: x+y)(x,y)

print result
