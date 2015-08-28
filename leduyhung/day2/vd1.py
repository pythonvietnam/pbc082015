#hungld
print ''' 
-----------------------------------------
Xin chao. Hay tra loi mot so cau hoi?
-----------------------------------------
'''
# asking for input
y = input("Ban sinh nam bao nhieu?  ")
print "Ban sinh nam %d?"%(y) 
b=2015-y
#print " Va ban da %d tuoi"%(b)
if b < 18:
	print "Ban moi %d tuoi"%(b)
	print "Ban chua du tuoi vao trong."
else:
	print "Ban da %d tuoi"%(b)
	print "Ban da du tuoi kham pha the gioi"
