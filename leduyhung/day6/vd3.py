#hungld
'''
-----------------------------------
Chuong trinh doc chuoi nhap vao tu nguoi dung va chi xu ly in ra nhung chuoi nao batdau voi tu: "chatmsg:", thoat bam "q"
----------------------------------
'''
l=list()
beginw="chatmsg:"
while 1:
	s=raw_input("hay nhap vao chuoi bat ky, bam q de quit ")
	if s=="q" or s=="Q":
		break
	elif s.startswith(beginw):
		l.append(s)
			
print l
