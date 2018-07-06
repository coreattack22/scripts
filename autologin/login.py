from time import sleep
import os
import subprocess
import sys
import json


def activate_app(app_name):
	subprocess.Popen(app_name, shell=True)
	print ("wait for app...")
	sleep(50)

#適宜うまくログインできるように書き換え
def click():
	for i in range(10):
		sleep(5)
		subprocess.run('adb shell input touchscreen tap 1000 800', shell=True)	
		subprocess.run('adb shell input touchscreen tap 1000 900', shell=True)	
		subprocess.run('adb shell input touchscreen tap 1000 1000', shell=True)
		print("clicked!")


path = os.path.dirname(os.path.abspath(__name__)) 
print (path)

#Noxの入っているディレクトリを指定
os.chdir("C:\\Program Files (x86)\\Nox\\bin")

f = open(path+'\\applist.json', 'r')
json = json.load(f)

for i in json['AppList']:
	print('nox.exe -package:'+i)
	activate_app('nox.exe -package:'+i)
	click()
