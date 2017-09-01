import os
import time
import datetime
from datetime import datetime


def checkngayxoa(ngaycu, ngayhientai):


    a = ngayhientai - ngaycu
    if a > 2:
        #print ("lon hon 2 ngay xoa")
        return 1
    else:
        #print ( " nho hon 2 ngay giu")
        return 0
# The top argument for walk
topdir = 'D:\GenTools'
# The extension to search for
exten = '.dmp'
logname = 'findfiletype.log'
# What will be logged
bkfoler = 'D:\scmdb'
results = str()
localtime = datetime.today()
now = localtime.day

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            # Save to results string instead of printing	
            ffile = os.path.join(dirpath, name)		
            results += '%s\n' % os.path.join(dirpath, name)
            mv = ('move ' + ffile + ' ' + bkfoler  )
            print (mv)
            os.system(mv)
codeweb='D:\WWW\scm.topica.edu.vn'
bkcode = ('aws s3 sync  ' + codeweb + ' s3://uniscm/scm.topica.edu.vn/')
os.system(bkcode)
cmd = ('aws s3 sync  ' + bkfoler + ' s3://uniscm/')
os.system(cmd)
print (cmd)

