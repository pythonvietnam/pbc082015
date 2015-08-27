#hungld
'''
-----------------
Bai toan doan ky tu
----------------
'''
n1=0
n2=0
n3=0
n = raw_input("Nhap vao chuoi ky tu bat ky:  ")
for i in n:
	if i=="a":
		n1 = n1 + 1
	elif i=="b":
		n2 = n2 + 1
	elif i=="c":
		n3 = n3 + 1
print "Co tat ca %d ky tu a trong chuoi ban da nhap"%(n1)
print "Co tat ca %d ky tu b trong chuoi ban da nhap"%(n2)
print "Co tat ca %d ky tu c trong chuoi ban da nhap"%(n3)
