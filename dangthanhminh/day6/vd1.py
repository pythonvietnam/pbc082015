#minhdt
print '''
----------------------------
Tach chuoi dua ten nguoi gui
----------------------------
'''
s = 'fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info'
s1 = s.split(':',1)
s2 = s1[1].split('.',1)

print "from X with Love%s"%(s2[0])
s3 = s.split('o ',1)
s4 = s3[1].split('o ',1)
print "Send email to:%s"%(s4[0])
