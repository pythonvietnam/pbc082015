#python
#loitd
#demo for get user input & insert in to a list

l = list()

for i in range(10):
	element = raw_input("Please input an element:")
	l.append(element)

for i in l:
	print "Element number %d is: %s"%(i, l[i])

#end.
