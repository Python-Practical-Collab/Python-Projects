from curses.ascii import isalpha
import os
import sys
sys.path.append("/mnt/Work/Github/Python-Projects/modules")
import time
import quote
import threading

class Main():

	def __init__(self) -> None:

		os.system("clear")

		if len(sys.argv) == 2: pass
		else: 
			print("Usage: timer 1h/1m/20s")
			sys.exit()

		self.data = {
			"h" : 3600,
			"m" : 60,
			"s" : 1
		}
		self.duration = sys.argv[1]

	def main(self):
		print("Welcome to timer. A simple CLI based timer")

		for i in self.duration:
			if i.isalpha():
				a = i

		data = self.duration.split(a)
		data.append(a)
		self.dur, self.units = int(data[0]), self.data[data[2]]
		print(f"Setting a timer for {int(data[0]) * self.units} seconds or {self.duration}")
		thread_1 = threading.Thread(target = self.timer())
		thread_1.start()


	def timer(self):
		print("Timer started!")
		print(f"While your timer is running, here is a random quote: \n{quote.Quote().random_quote()[0]}")
		time.sleep(self.dur * self.units)
		print("Times up!!")
		os.system(f"mpv kool.mp3 > /dev/null")

if __name__ == "__main__":
	Main().main()
