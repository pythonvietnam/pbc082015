#Bai tap them ki tu
print "===========Them chuoi ki tu============="
#str = "abcdef"
str = raw_input("Nhap chuoi:")
#print len(str)
print ','.join([str[i] for i in range(0,len(str))])