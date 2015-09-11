#messChild1 = list()
#messChild2 = list()
mess = "fromXwithLove: I love Python. Send email to loitd@pythonvietnam.info"
messChild1 = mess.split(': ')
print messChild1

print "Sender:  %s" %(messChild1[0])
#print messChild1[1]
messChild2 = messChild1[1].split('Send email to ')
print "Content:  %s" %(messChild2[0])
print "To:  %s" %(messChild2[1])

