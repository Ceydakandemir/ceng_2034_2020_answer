import requests
import os
import sys
import multiprocessing
import threading

#checking URL
print("2xx is successful. 4xx or 5xx mean failed.\n")
def requestByThread(url):

	answer = requests.get(url)
	print(answer.status_code,"  ",url)
	
thread1 = threading.Thread(target = requestByThread,args=("https://api.github.com",))
thread2 = threading.Thread(target = requestByThread,args=("http://bilgisayar.mu.edu.tr/",))
thread3 = threading.Thread(target = requestByThread,args=("https://www.python.org/",))
thread4 = threading.Thread(target = requestByThread,args=("http://akrepnalan.com/ceng2034",))
thread5 = threading.Thread(target = requestByThread,args=("https://github.com/caesarsalad/wow",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()



	#print PID
print("\nPID:",os.getpid())		

	#print nproc
nproc=multiprocessing.cpu_count()
print("\nNproc:",nproc)			

	#print loadavg
platform = sys.platform
if(platform == "linux"):
	print("loadavg: ",os.getloadavg())
	
	#print loadavg 5 minutes
load1,load5,load15 = os.getloadavg()
print("\nLoadavg 5 minutes:",load5)
	

	#If the loadavg value is near(or close ) to the cpu core count then exit script

print("\n(nproc-5 min loadavg<5) exit script. ")
while(True):					
		
	load1,load5,load15 = os.getloadavg()	
	if((nproc-load5)<1):			
		print("5minLoadAvg is too close to nproc...\nProgram Terminated!")
	break
