import os,time,sys
path=r"C:\Users\lalitk\Documents\code\python\database"
now=time.time()
flag=1
for f in os.listdir(path):
    f=os.path.join(path,f)
    if os.stat(f).st_mtime<now-1*86400:
        if os.path.isfile(f):
            print(f)
            flag=0;
            if f == r"C:\Users\lalitk\Documents\code\python\database\notdelete.txt":
                print(".....File is older but has to be saved")
            #print('File removed...:',f)
            #os.remove(f)
if flag is 1:
    print("  No older log files....")
