#"fromXwithlove: I love Python. Send email to loitd@pythonvietnam.info"
#Tach chuoi nay de dua ra duoc ten nguoi gui, thong diep va email nguoi nhan
#haind

print '''
==========================
Day la bai tap Tach String
=========================='''

#cho chuoi string
print "Chuoi can tach la:  " 
s = "fromXwithlove: I love Python. Send email to loitd@pythonvietnam.info"

#thuc hien tach chuoi
a = s.split(": ",1)
c = s.split(" Send email to ")

#in chuoi
print "From people: %s"%(a)
print c

