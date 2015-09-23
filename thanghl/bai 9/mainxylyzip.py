#thanghl
#xylyzip
import xylyfilezipv2
listname=str()
read=raw_input('Nhap file giai nen ')
xylyfilezipv2.giainen(read,listname)
print 'dong moi ' + listname
readpw=raw_input('Nhap file giai nen chua pass : ')
xylyfilezipv2.giainenpw(readpw)


