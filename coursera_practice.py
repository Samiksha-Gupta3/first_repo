import shutil
du = shutil.disk_usage('/')
print(du)
print(du.free/du.total*100)
import psutil
usage = psutil.cpu_percent(0.8)
print(usage)
file = open('file.html','r')
print(file.readline())
file.close()
with open("file.html") as file:
    print(file.read())

import os
print(os.path.exists("file.html"))
print(os.path.exists("hello.py"))
print(os.path.getsize("file.html"),'bytes')
print(os.path.getmtime("file.html"))
print(os.path.join(os.getcwd(),os.pardir))
os.rename('file.html','file.html')
print(os.getcwd())
print(os.path.abspath('file.html'))
print(os.path.abspath('hello.py'))
os.chdir('C:\Program Files')
print(os.getcwd())
print(os.path.abspath('C:'))
print(os.path.getsize("C:\Program Files"))
os.chdir(r'C:\Users\hp123\Desktop')
print(os.getcwd())
print(os.listdir(os.getcwd()))
dir = os.getcwd()
for i in os.listdir(dir):
    j = os.path.join(dir,i)
    if os.path.isdir(j):
        print("It is directory")
    else:
        print("It is file")
import datetime
timestamp = datetime.datetime.fromtimestamp(os.path.getmtime("file.html"))
print(timestamp)