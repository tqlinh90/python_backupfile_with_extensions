import os
import time
import datetime
from datetime import datetime

def checkngayxoa(ngaycu, ngayhientai):
    a = ngayhientai - ngaycu
    print (a)
    if (a > 2 or a < 0):
        #print ("lon hon 2 ngay xoa")
        return 1
    else:
        #print ( " nho hon 2 ngay giu")
        return 0

bkfoler = 'D:\scmdb'
for dirpath, dirnames, files in os.walk(bkfoler):
    for name in files:
        filepaths = os.path.join(dirpath, name)
        #print (filepaths )
        #a =  datetime.strptime(time.ctime(filepaths), "%a %b %d %H:%M:%S %Y")
        result = time.strftime('%d', time.gmtime(os.path.getctime(filepaths)))
        print (result)
        ngayhientai = time.strftime("%d")
        print (ngayhientai)
        if checkngayxoa(int(result),int(ngayhientai)) == 1 :
            print ("xoa")
            print (filepaths)
            os.remove(filepaths)
        else:
            print ("ko xoa")
        
    #filepath = os.path.dirname(os.path.abspath(files))
    #print (filepath)
    """
    for name in files:
        print (name)
        ffile = os.path.join(dirpath, name)
       # a =  datetime.strptime(time.ctime(name), "%a %b %d %H:%M:%S %Y")
       # a =  datetime.strptime(time.ctime(name), "%a %b %d %H:%M:%S %Y")
       #result = os.path.getmtime(path)
        #print (a)
    #print (files)


    for name in files:
        if name.lower().endswith(exten):
            # Save to results string instead of printing	
            ffile = os.path.join(dirpath, name)		
            results += '%s\n' % os.path.join(dirpath, name)
            mv = ('move ' + ffile + ' ' + bkfoler  )
            print (mv)
            os.system(mv)
			"""
