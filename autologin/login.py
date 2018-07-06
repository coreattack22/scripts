from time import sleep
import os
import subprocess
import sys

def activate_app(app_name):
	subprocess.Popen(app_name, shell=True)
	print ("wait for app...")
	sleep(50)

def click():
	for i in range(10):
		sleep(5)
		subprocess.run('adb shell input touchscreen tap 1000 800', shell=True)	
		subprocess.run('adb shell input touchscreen tap 1000 900', shell=True)	
		subprocess.run('adb shell input touchscreen tap 1000 1000', shell=True)
		print("clicked!")



os.chdir("C:\\Program Files (x86)\\Nox\\bin")
app_name=['nox.exe -package:jp.co.bandainamcoent.BNEI0242',
		  'nox.exe -package:jp.co.cygames.Shadowverse',
		  'nox/exe -package:com.bandainamcoent.imas_millionlive_theaterdays']

for i in app_name:
	activate_app(i)
	click()

