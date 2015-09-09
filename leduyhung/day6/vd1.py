#hungld
'''
-----------------------------------
Bai toan tach chuoi
-----------------------------------
'''
s="fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info"
a=s.split(":")
x1=a[:1]
s2=a[1]
b=s2.split(".")
x2=b[:1]
s3=b[1]
c=s3.split("to")
x3=c[1:]

print '''Trong chuoi: "fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info" thi: 
'''
print "Ten nguoi gui:  %s"%x1[0]
print "Thong diep:  %s"%x2[0]
print "Dia chi email nguoi nhan:  %s"%x3[0]
