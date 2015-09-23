#python
#loitd
#pbc

print '''
Just a welcome!
'''

#get user input
k = 1
a = input("Let's try: 1+2+3 or k: ")
print "your score is: " + str(a)

#in python 3.x raw_input() -> input(); input() -> removed
a = int(raw_input("Hay nhap so:"))
b = long(raw_input("Hay nhap binh phuong:"))
print "Calculating ..."

#tinh binh phuong
aa = long(pow(a,2))

#so sanh
if aa == b:
	print "Xin chuc mung. Ban da doan dung."
elif aa < b:
	print "Doan thap xuong"
else:
	print "Doan cao len."

