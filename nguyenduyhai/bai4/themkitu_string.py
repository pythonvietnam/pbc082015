#Cho nguoi dung nhap vao mot chuoi sau do tu dong thuc hien them moi mot ky tu bat ky
#vao sau cua moi ky tu trong chuoi ban dau. Vi du: neu nguoi dung nhap chuoi "abc", ket qua
#phai la chuoi "a,b,c"
#haind

print'''
-----------------------------------------------------
Bai tap them ky tu vao 1 chuoi do nguoi dung nhap vao
-----------------------------------------------------'''

s = raw_input("Moi ban nhap mot chuoi:")
list('s')
a = ','.join(s)
print "Ky tu tach chuoi la: %s"%(a)