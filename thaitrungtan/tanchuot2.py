#nhap vao mot so
#doan binh phuong cua so do
print '''
--------------------------------------------
CHAO MUNG BAN DEN VOI CHUONG TRINH DOAN 
SO TRUNG THUONG!!!!!!!!!!!!!!!!!!
--------------------------------------------
'''
a = input("ban hay nhap vao mot so")
b = input("ban hay doan binh phuong cua so do")
if a*a>b:
	print "so ban doan thap hon gia tri binh phuong"
elif a*a==b:
	print "ban da doan chinh xac"
else :
	print "so ban doan cao hon gia tri binh phuong"
