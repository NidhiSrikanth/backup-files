import time
import os
import shutil

obj= time.gmtime(0)
day= time.asctime(obj)
print("day is:",day )
time_sec= time.time()
print("time in seconds:", time_sec)
listoffiles= os.listdir(path)

for file in listoffiles:
    name, ext= os.path.splitext(file)
    ext= ext [1:]

    if ext==" ":
        continue

    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)

    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)

ctime= os.stat(path).st_ctime

return ctime
    