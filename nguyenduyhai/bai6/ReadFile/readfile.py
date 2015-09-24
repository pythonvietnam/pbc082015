#module readfile in python
#haind
#python


import os

print '''
-----------------------------
CHUONG TRINH DOC FILE - HAIND
-----------------------------
'''

filepath = raw_input ("Hay nhap duong dan file: ")

if (os.path.exists(filepath)):
    mofile = open(filepath, 'r')
    i = 0
    for line in mofile:
        i += 1
        print line.rstrip()
   
else:
	#print ""
    print "File khong ton tai, de nghi kiem tra lai!"