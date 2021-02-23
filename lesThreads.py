#coding:utf-8
import time
import threading
import random
my_lock =threading.RLock()

class MyProcess(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		i=0
		while i<3:
			with my_lock:
				letters="ABC"
				for it in letters:
					print(it)
					time.sleep(random.randint(0,1))
			i+=1


th1 = MyProcess()
th2 = MyProcess()

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin d'exécution des threads !!!")